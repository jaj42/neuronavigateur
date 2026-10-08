#!/usr/bin/env python3
"""Download the Wikimedia Commons images listed in figures/wikimedia/credits.yml.

For each entry (id, commons, legende), fetch the Commons metadata and a PNG
rendering (SVGs are rasterised by Commons), save it as figures/wikimedia/<id>.png
and write author, licence and URLs back into credits.yml, so credits are never
typed by hand. Also writes annexes/_credits-wikimedia.md, the table included by
the « Crédits des images » annex. --check only verifies that every entry has its image and credits; --annex only
rewrites the annex table from credits.yml; --new only fetches entries whose image is missing
(Commons answers 429 when every image is fetched again). An optional recadrage field
[gauche, haut, droite, bas], in fractions of the image, crops it.
"""

import re
import sys
from pathlib import Path

import requests
import yaml
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
DIR = ROOT / "figures" / "wikimedia"
CREDITS = DIR / "credits.yml"
ANNEX = ROOT / "annexes" / "_credits-wikimedia.md"
API = "https://commons.wikimedia.org/w/api.php"
UA = {"User-Agent": "neuro_starter/0.1 (book build script)"}
WIDTH = 1600
FIELDS = ("fichier", "url", "auteur", "licence", "licence_url")
HEADER = """\
# Images Wikimedia Commons utilisées dans le livre.
# À la main : id, commons (titre exact de la page), legende, recadrage (facultatif).
# Rempli par scripts/wikimedia.py (ne pas éditer) : fichier, url, auteur, licence, licence_url.
"""


def clean(html):
    text = re.sub(r"<[^>]+>", "", html or "")
    return re.sub(r"\s+", " ", text).strip()


def flatten(path):
    """Put transparent images on white, so they read the same in print and dark HTML."""
    im = Image.open(path)
    if im.mode in ("RGBA", "LA", "P"):
        im = im.convert("RGBA")
        bg = Image.new("RGB", im.size, "white")
        bg.paste(im, mask=im.getchannel("A"))
        bg.save(path, optimize=True)


def fetch(entry):
    r = requests.get(API, headers=UA, timeout=30, params={
        "action": "query", "format": "json", "titles": entry["commons"],
        "prop": "imageinfo", "iiprop": "url|extmetadata", "iiurlwidth": WIDTH,
    })
    r.raise_for_status()
    page = next(iter(r.json()["query"]["pages"].values()))
    if "imageinfo" not in page:
        sys.exit(f"{entry['commons']} : introuvable sur Commons")
    info = page["imageinfo"][0]
    meta = info["extmetadata"]
    img = requests.get(info.get("thumburl") or info["url"], headers=UA, timeout=60)
    img.raise_for_status()
    out = DIR / f"{entry['id']}.png"
    out.write_bytes(img.content)
    flatten(out)
    if entry.get("recadrage"):
        im = Image.open(out)
        l, t, r, b = entry["recadrage"]
        im.crop((round(l * im.width), round(t * im.height),
                 round(r * im.width), round(b * im.height))).save(out, optimize=True)
    entry.update({
        "fichier": f"figures/wikimedia/{out.name}",
        "url": info["descriptionurl"],
        "auteur": clean(meta.get("Artist", {}).get("value")),
        "licence": clean(meta.get("LicenseShortName", {}).get("value")),
        "licence_url": clean(meta.get("LicenseUrl", {}).get("value")) or None,
    })
    print(f"{out.relative_to(ROOT)} : {entry['licence']}, {entry['auteur']}")


def annex(entries):
    rows = ["| Figure | Auteur | Licence | Source |", "|---|---|---|---|"]
    for e in entries:
        lic = {"Public domain": "Domaine public"}.get(e["licence"], e["licence"])
        if e.get("licence_url"):
            lic = f"[{lic}]({e['licence_url']})"
        name = e["commons"].removeprefix("File:")
        auteur = e["auteur"].replace("|", "/")
        rows.append(f"| {e['legende'].split(' :')[0].rstrip('.')} | {auteur} | {lic} "
                    f"| [{name}]({e['url']}) |")
    ANNEX.write_text("<!-- Généré par scripts/wikimedia.py, ne pas éditer. -->\n\n"
                     + "\n".join(rows) + "\n")


def main():
    entries = yaml.safe_load(CREDITS.read_text())
    if "--check" in sys.argv:
        bad = [e["id"] for e in entries
               if not all(k in e for k in FIELDS) or not (ROOT / e["fichier"]).exists()]
        sys.exit(f"incomplet : {', '.join(bad)}" if bad else 0)
    if "--annex" not in sys.argv:
        for e in entries:
            if "--new" in sys.argv and (ROOT / e.get("fichier", "-")).is_file():
                continue
            fetch(e)
    annex(entries)
    CREDITS.write_text(HEADER + yaml.safe_dump(entries, allow_unicode=True, sort_keys=False,
                                               width=100))


if __name__ == "__main__":
    main()
