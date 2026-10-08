"""Calendrier de l'HSA anévrysmale, de J0 à J21 : complications et traitements."""

from _style import AQUA, BLUE, INK2, MUTED, ORANGE, TEXTWIDTH, ZONE, plt, save

fig, ax = plt.subplots(figsize=(TEXTWIDTH * 0.8, 3.0))

# (libellé, couleur, [(début, fin, opacité)], note)
rows = [
    ("Resaignement", ORANGE, [(0, 1, 0.9), (1, 3, 0.35)], "risque maximal < 24 h"),
    ("Exclusion de l'anévrysme", ORANGE, [(0, 1, 0.9)], "dans les 24 h"),
    ("Hydrocéphalie", BLUE, [(0, 3, 0.8), (3, 14, 0.35), (14, 21, 0.15)],
     "aiguë, puis à tout moment, puis chronique"),
    ("Vasospasme angiographique", AQUA, [(4, 8, 0.4), (8, 10, 0.9), (10, 14, 0.4)],
     "J4–J14, pic J8–J10"),
    ("Dépistage de l'ischémie retardée", AQUA, [(3, 14, 0.25)],
     "examen et Doppler quotidiens"),
    ("Hyponatrémie", BLUE, [(4, 10, 0.5)], "J4–J10 surtout"),
    ("Nimodipine entérale", MUTED, [(0, 21, 0.45)], "60 mg toutes les 4 h, 21 jours"),
]

for i, (label, color, spans, note) in enumerate(rows):
    y = len(rows) - 1 - i
    for a, b, alpha in spans:
        ax.barh(y, b - a, left=a, height=0.62, color=color, alpha=alpha, lw=0)
    ax.text(-0.3, y, label, ha="right", va="center", fontsize=8, color=INK2)
    end = max(b for _, b, _ in spans)
    inside = end - min(a for a, _, _ in spans) > 12
    ax.text(end + 0.25 if not inside else 0.4 if end > 15 else end + 0.25, y, note,
            ha="left", va="center", fontsize=7, color=INK2 if not inside else "#0b0b0b")

for a, b in ((0, 3), (14, 21)):
    ax.axvspan(a, b, color=ZONE, zorder=0, lw=0)
ax.set_xlim(0, 21)
ax.set_ylim(-0.6, len(rows) - 0.4)
ax.set_xticks([0, 1, 3, 4, 8, 10, 14, 21])
ax.set_xticklabels(["J0", "J1", "J3", "J4", "J8", "J10", "J14", "J21"], fontsize=7.5)
ax.set_yticks([])
ax.grid(axis="y", visible=False)
ax.spines["left"].set_visible(False)
for x, t in ((1.5, "J0–J3"), (8.5, "J3–J14"), (17.5, "après J14")):
    ax.text(x, len(rows) - 0.3, t, ha="center", va="bottom", fontsize=7.5, color=INK2,
            fontweight="bold")
save(fig, "calendrier-hsa")
