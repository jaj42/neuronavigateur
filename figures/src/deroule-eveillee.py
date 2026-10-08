"""Chirurgie éveillée, protocole du service : les six étapes et les sédations (schéma)."""

import numpy as np
from _style import AQUA, BLUE, INK, INK2, MUTED, ORANGE, TEXTWIDTH, ZONE, plt, save

# Étapes : (titre, largeur arbitraire sur le schéma)
steps = [("1. Mise en\ncondition", 2.0), ("2. Installation\néveillé", 1.9),
         ("3. Têtière,\nanesth. locale", 2.1), ("4. Incision,\ncraniotomie", 2.6),
         ("5. Cartographie,\nrésection", 3.2), ("6. Hémostase,\nfermeture", 2.0)]
edges = np.r_[0, np.cumsum([w for _, w in steps])]
s = {i + 1: (edges[i], edges[i + 1]) for i in range(len(steps))}
dura = s[4][0] + 0.85 * (s[4][1] - s[4][0])     # ouverture de la dure-mère
crani = s[4][0] + 0.7 * (s[4][1] - s[4][0])     # fin de la craniotomie

fig, ax = plt.subplots(figsize=(TEXTWIDTH * 0.8, 3.0))
for i, (a, b) in s.items():
    if i % 2:
        ax.axvspan(a, b, color=ZONE, lw=0, zorder=0)
    ax.text((a + b) / 2, 4.55, steps[i - 1][0], ha="center", va="bottom", fontsize=7,
            color=INK, fontweight="bold")

# (ligne, couleur, segments (début, fin, plein ?), libellé)
rows = [
    ("Dexmédétomidine", AQUA, [(s[1][0], s[1][1], True), (s[3][0], crani, True),
                               (s[6][0], s[6][1], False)]),
    ("Rémifentanil", BLUE, [(s[1][0], s[1][1], True), (s[3][0], dura, True),
                            (s[6][0], s[6][1], True)]),
    ("Propofol (titré)", ORANGE, [(s[1][0], s[1][1], True), (s[4][0], dura, True),
                                  (s[6][0], s[6][1], True)]),
]
for k, (name, color, segs) in enumerate(rows):
    y = 3.6 - k * 0.75
    for a, b, full in segs:
        ax.barh(y, b - a, left=a, height=0.45, color=color, alpha=0.75 if full else 0.25,
                lw=0, hatch=None if full else "///", edgecolor=color)
    ax.text(-0.15, y, name, ha="right", va="center", fontsize=7.5, color=INK2)

# Patient éveillé et coopérant
y = 1.25
ax.barh(y, s[2][1] - s[2][0], left=s[2][0], height=0.45, color=MUTED, alpha=0.35, lw=0)
ax.barh(y, s[5][1] - dura, left=dura, height=0.45, color=MUTED, alpha=0.75, lw=0)
ax.text(-0.15, y, "Patient éveillé", ha="right", va="center", fontsize=7.5, color=INK2)
ax.text((dura + s[5][1]) / 2, y, "le « travail »", ha="center", va="center",
        fontsize=7, color="white", fontweight="bold")

# Repères ponctuels
marks = [(s[4][0], "kétamine\n0,25 mg/kg"), (dura, "ouverture de\nla dure-mère"),
         (s[6][0] + 0.25, "morphine\n0,1 mg/kg")]
for x, t in marks:
    ax.plot([x, x], [0.75, 4.0], color=INK2, lw=0.8, ls=(0, (2, 2)))
    ax.text(x, 0.55, t, ha="center", va="top", fontsize=6.5, color=INK2)

ax.set_xlim(0, edges[-1])
ax.set_ylim(-0.35, 5.3)
ax.axis("off")
ax.text(edges[-1], -0.3, "hachures : facultatif", ha="right", va="bottom", fontsize=6.5,
        color=INK2, style="italic")
save(fig, "deroule-eveillee")
