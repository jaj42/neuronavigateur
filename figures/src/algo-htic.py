"""Devant une PIC élevée : trois questions, puis l'échelle en paliers du consensus SIBICC."""

from matplotlib.patches import FancyBboxPatch
from _diagram import arrow, box, canvas
from _style import AQUA, BLUE, INK, INK2, MUTED, ORANGE, TEXTWIDTH, plt, save

fig, ax = plt.subplots(figsize=(TEXTWIDTH, 4.6))
canvas(ax, 16.6, 11.4)

# Colonne gauche : les trois questions
box(ax, 3.2, 10.3, "PIC > 22 mmHg\n(ou signes d'engagement)", ORANGE, w=4.6, h=1.0, fill=0.3,
    bold=True)
qs = [
    (8.6, "1. ACSOS corrigées ?\nPA, SpO$_2$, PaCO$_2$, natrémie,\nHb, température, glycémie"),
    (6.6, "2. Le capteur dit-il vrai ?\nzéro, courbe, clinique"),
    (4.6, "3. Cause chirurgicale ?\nscanner : hématome, contusion\nqui gonfle, hydrocéphalie"),
]
prev = 9.8
for y, t in qs:
    box(ax, 3.2, y, t, BLUE, w=5.4, h=1.35, fill=0.08, size=7.5)
    arrow(ax, (3.2, prev), (3.2, y + 0.7))
    prev = y - 0.7
box(ax, 3.2, 2.3, "Chirurgie : évacuation,\nDVE, décompression", ORANGE, w=4.6, h=1.0,
    size=7.5)
arrow(ax, (3.2, prev), (3.2, 2.8), text="oui", tx=0.35)
arrow(ax, (5.9, 4.6), (6.85, 4.6), text="non", ty=0.25)
ax.text(3.2, 0.9, "Refaire ces trois vérifications\nà chaque changement de palier.",
        ha="center", va="center", fontsize=7.5, color=INK2, style="italic")

# Escalier des paliers SIBICC
tiers = [
    ("Palier 0 : socle, pour tous", "tête 30–45°, sédation-analgésie, T° ≤ 38 °C,\n"
     "SpO$_2$ ≥ 94 %, EtCO$_2$, PPC ≥ 60 mmHg,\nHb > 7 g/dL, pas d'hyponatrémie", MUTED),
    ("Palier 1", "PPC 60–70 mmHg ; sédation approfondie ;\nPaCO$_2$ 35–38 mmHg ; "
     "osmothérapie en bolus ;\ndrainage du LCR ; EEG", AQUA),
    ("Palier 2", "PaCO$_2$ 32–35 mmHg ;\ncurarisation, gardée si efficace ;\n"
     "test de la PAM si autorégulation conservée", BLUE),
    ("Palier 3", "barbituriques titrés sur la PIC ;\nhypothermie 35–36 °C ;\n"
     "craniectomie décompressive", ORANGE),
]
x0, y0, w, h = 6.9, 1.3, 7.6, 2.15
for i, (title, body, color) in enumerate(tiers):
    x, y = x0 + i * 0.35, y0 + i * (h + 0.25)
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.15",
                                fc=color + "22", ec=color, lw=1.2))
    ax.text(x + 0.2, y + h - 0.32, title, fontsize=8, color=INK, fontweight="bold", va="center")
    ax.text(x + 0.2, y + 0.82, body, fontsize=7, color=INK2, va="center", linespacing=1.25)
top = y0 + 4 * h + 3 * 0.25
arrow(ax, (15.75, y0), (15.75, top), color=ORANGE, lw=1.6)
ax.text(15.95, (y0 + top) / 2, "intensité et risque croissants", rotation=90, ha="left",
        va="center", fontsize=7.5, color=ORANGE)
ax.text(x0 + 4.3, y0 - 0.45, "PIC non contrôlée : palier suivant (on peut en sauter un)",
        ha="center", va="center", fontsize=7.5, color=INK2)
save(fig, "algo-htic")
