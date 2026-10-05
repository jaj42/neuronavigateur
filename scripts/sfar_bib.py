#!/usr/bin/env python3
"""Generate the @misc entries for French recommendations (SFAR and partners).

Titles, years, types and URLs come from discovery.json, so no URL is ever
typed by hand. Each document is identified by its file name without the
extension. The entries replace the block between the SFAR markers in
references.bib; the journal entries outside that block are left untouched.

Usage:
    scripts/sfar_bib.py           # rewrite the SFAR block of references.bib
    scripts/sfar_bib.py --check   # check every @misc url against discovery.json
"""

import datetime
import json
import re
import sys
from pathlib import Path

SFAR = Path("/home/jaj/devel/sfar_recommendations/output")
DISCOVERY = SFAR / "discovery.json"
ROOT = Path(__file__).resolve().parent.parent
BIB = ROOT / "references.bib"
BEGIN = "% BEGIN SFAR (généré par scripts/sfar_bib.py, ne pas éditer à la main)"
END = "% END SFAR"

SOCIETIES = {
    "SFAR": "Société française d'anesthésie et de réanimation (SFAR)",
    "ANARLF": "Association de neuro-anesthésie réanimation de langue française (ANARLF)",
    "SFNC": "Société française de neurochirurgie (SFNC)",
    "SFMU": "Société française de médecine d'urgence (SFMU)",
    "SRLF": "Société de réanimation de langue française (SRLF)",
    "GIHP": "Groupe d'intérêt en hémostase périopératoire (GIHP)",
    "GFHT": "Groupe français d'études sur l'hémostase et la thrombose (GFHT)",
    "SPILF": "Société de pathologie infectieuse de langue française (SPILF)",
    "SFO": "Société française d'ophtalmologie (SFO)",
    "SFD": "Société francophone du diabète (SFD)",
    "SOFMER": "Société française de médecine physique et de réadaptation (SOFMER)",
    "ABM": "Agence de la biomédecine",
}

# key, file stem, societies (authoring ones only, in title-page order), note
DOCS = [
    ("sfnc_tce2025", "RPP-Trauma-cranio-encephaliques-V1-finalisee",
     ["SFNC", "ANARLF", "SFAR"], "RPP"),
    ("sfnc_tce2025_fiche", "Figure-1-Fiche-synthese-FR",
     ["SFNC", "ANARLF", "SFAR"], "RPP, fiche de synthèse"),
    ("sfar_tcgrave2016", "RFE-ANREA-Prise-en-charge-des-traumatises-craniens-graves-a-la-phase-precoce",
     ["SFAR", "ANARLF", "SFNC"], "RFE"),
    ("sfmu_tcleger2022", "RPP-Trauma-cranien-leger_pour-mise-sur-site_autorship-complet",
     ["SFMU", "SFAR"], "RPP"),
    ("sfar_tvm2019", "rfe-trauma-vertebro-medulaire",
     ["SFAR", "ANARLF", "SFMU"], "RFE"),
    ("sfar_tvm2019_fiche", "rfe-vertebro-medullaire-fiche-synthese",
     ["SFAR", "ANARLF", "SFMU"], "RFE, fiche de synthèse"),
    ("sfar_thrombectomie2022", "RPP-thrombectomie-2022_version-definitive-octobre-2022",
     ["SFAR", "ANARLF"], "RPP"),
    ("sfar_hsa2004", "2a_SFAR_texte-court_Hemorragies-sous-arachnoidienne",
     ["SFAR", "ANARLF"], "RFE, texte court"),
    ("gihp_aod2026", "RFE-20.4.2026-deifinitif-et-validei",
     ["GIHP", "SFAR"], "RFE"),
    ("sfmu_anticoagurgence2024", "RFE-gestion-de-lanticoagulation-dans-un-contexte-durgence_23.02.2024-1",
     ["SFMU", "SFAR", "GIHP"], "RFE"),
    ("sfmu_anticoagurgence2024_algo", "Algorithmes_RFE-gestion-de-lanticoagulation-dans-un-contexte-durgence_2024",
     ["SFMU", "SFAR", "GIHP"], "RFE, algorithmes"),
    ("gihp_aap2018", "2_Gestion-des-agents-antiplaquettaires-pour-une-procedure-invasive-programmee",
     ["GIHP", "GFHT", "SFAR"], "Propositions"),
    ("gihp_aapurgence2018", "rfe-gestion-des-agents-antiplaquettaires",
     ["GIHP", "GFHT", "SFAR"], "Propositions"),
    ("gihp_mtev2024", "240516-Txt-definitif-",
     ["GIHP", "SFAR"], "RFE"),
    ("sfar_atb2023", "RFE-antibioprophylaxie-2023_V3.0_pour-mise-sur-site-juin-2026_sans-code-CCAM",
     ["SFAR", "SPILF"], "RFE, version 3.0 (2026)"),
    ("sfar_solutes2021", "RFE-SFAR-SFMU-Solute%CC%81s-de-remplissage_finale_220921",
     ["SFAR", "SFMU"], "RFE"),
    ("srlf_cct2016", "rfe-controle-cible-de-la-temperature-en-reanimation",
     ["SRLF", "SFAR"], "RFE"),
    ("sfar_anemie2019", "rfe-gestion-anemie-reanimation",
     ["SFAR", "SRLF"], "RFE"),
    ("sfar_hemodynamique2024", "2024_RFE-optimisation-hemodynamique-perioperatoire_adulte-dont-obstretriqueV2-1",
     ["SFAR"], "RFE"),
    ("sfar_douleur2016", "RFE-ANREA-Reactualisation-de-la-recommandation-sur-la-douleur-postoperatoire",
     ["SFAR"], "RFE"),
    ("sfar_curares2018", "2_RFE-CURARE-3",
     ["SFAR"], "RFE"),
    ("sfar_oeil2016", "Protection-oculaire-en-Anesthesie-et-Reanimation-1",
     ["SFAR", "SFO", "SRLF"], "RFE"),
    ("sfar_diabete2025", "Fiches-simplifiees-19122025-",
     ["SFAR", "SFD"], "Fiches simplifiées"),
    ("sfar_intubation2016", "Intubation-et-extubation-du-patient-en-reanimation-ANREA",
     ["SFAR", "SRLF"], "RFE"),
    ("sfar_lat2025", "RFE-LAT-final-mai-2026-",
     ["SFAR", "SOFMER"], "RFE"),
    ("abm_demarches2024", "RBP-deimarches-anticipeies_12_10_24",
     ["ABM"], "RBP"),
    # Historique: cited only as superseded texts.
    ("sfar_eeg2010", "2_SFAR_Monitorage-de-ladequation-profondeur-de-lanesthesie-a-partir-de-lanalyse-de-lEEG-cortical",
     ["SFAR"], "RFE, historique"),
    ("sfar_nvpo2007", "2_AFAR_Prise-en-charge-des-nausees-et-vomissements-postoperatoires",
     ["SFAR"], "RFE, historique"),
    ("srlf_eme2008", "3_REANIMATION_Prise-en-charge-en-situation-durgence-et-en-reanimation-des-etats-de-mal-epileptiques-de-ladulte-et-de-lenfant",
     ["SRLF"], "RFE, historique"),
    ("sfar_mtev2011", "2_AFAR_Prevention-de-la-maladie-thromboembolique-veineuse-postoperatoire-copie",
     ["SFAR"], "RFE, historique"),
]


def load_documents():
    docs = json.loads(DISCOVERY.read_text())["documents"]
    by_stem = {}
    for d in docs:
        if d.get("filename"):
            by_stem.setdefault(Path(d["filename"]).stem, d)
    return docs, by_stem


def entry(key, doc, societies, note, today):
    url = doc["landing_url"] or doc["download_url"]
    authors = " and ".join("{" + SOCIETIES[s] + "}" for s in societies)
    fields = [
        ("author", authors),
        ("title", "{" + doc["title"].strip() + "}"),
        ("year", str(doc["year"])),
        ("type", note),
        ("url", url),
        ("urldate", today),
    ]
    body = ",\n".join(f"  {k:<7} = {{{v}}}" for k, v in fields)
    return f"@misc{{{key},\n{body}\n}}\n"


def generate():
    _, by_stem = load_documents()
    today = datetime.date.today().isoformat()
    out, missing = [], []
    for key, stem, societies, note in DOCS:
        doc = by_stem.get(stem)
        if doc is None:
            missing.append(stem)
            continue
        md = SFAR / "chandra" / str(doc["year"]) / stem / f"{stem}.md"
        if not md.exists():
            print(f"warning: no markdown for {key} ({md})", file=sys.stderr)
        out.append(entry(key, doc, societies, note, today))
    if missing:
        sys.exit("not found in discovery.json: " + ", ".join(missing))

    block = BEGIN + "\n\n" + "\n".join(out) + "\n" + END + "\n"
    bib = BIB.read_text()
    pattern = re.compile(re.escape(BEGIN) + r".*?" + re.escape(END) + r"\n?", re.S)
    bib = pattern.sub(lambda _: block, bib) if pattern.search(bib) else bib.rstrip() + "\n\n" + block
    BIB.write_text(bib)
    print(f"{len(out)} SFAR entries written to {BIB.name}")


def check():
    docs, _ = load_documents()
    known = {u for d in docs for u in (d["landing_url"], d["download_url"]) if u}
    bib = BIB.read_text()
    bad = 0
    for key, body in re.findall(r"@misc\{(\w+),(.*?)\n\}", bib, re.S):
        m = re.search(r"url\s*=\s*\{([^}]*)\}", body)
        if not m or m.group(1) not in known:
            print(f"{key}: url not in discovery.json")
            bad += 1
    print("ok" if not bad else f"{bad} bad url(s)")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    check() if "--check" in sys.argv else generate()
