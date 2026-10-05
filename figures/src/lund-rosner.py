"""Deux logiques opposées : cascade vasodilatatrice (Rosner) et forces de Starling (Lund)."""

import numpy as np
from matplotlib.patches import FancyArrowPatch, Rectangle
from _diagram import arrow, box, canvas
from _style import AQUA, BLUE, INK2, ORANGE, TEXTWIDTH, plt, save

fig, (a1, a2) = plt.subplots(1, 2, figsize=(TEXTWIDTH, 3.4))

# Rosner : boucle PPC ↓ → vasodilatation → VSC ↑ → PIC ↑ → PPC ↓
canvas(a1, 8, 7)
a1.set_title("Rosner : autorégulation conservée", loc="left", color=BLUE,
             fontweight="bold")
pos = {"ppc": (4, 5.7), "vd": (6.5, 3.7), "vsc": (4, 1.7), "pic": (1.5, 3.7)}
labels = {"ppc": "PPC ↓", "vd": "vasodilatation\nartériolaire",
          "vsc": "volume sanguin\ncérébral ↑", "pic": "PIC ↑"}
for k, (x, y) in pos.items():
    box(a1, x, y, labels[k], BLUE, w=2.6, h=1.05)
order = ["ppc", "vd", "vsc", "pic", "ppc"]
for a, b in zip(order, order[1:]):
    (x0, y0), (x1, y1) = pos[a], pos[b]
    d = np.array([x1 - x0, y1 - y0])
    u = d / np.linalg.norm(d)
    arrow(a1, (x0 + u[0] * 1.15, y0 + u[1] * 0.6), (x1 - u[0] * 1.15, y1 - u[1] * 0.6),
          color=BLUE, rad=-0.15)
a1.text(4, 3.7, "cercle\nvicieux", ha="center", va="center", color=INK2, fontsize=8,
        style="italic")
a1.text(0.1, 0.35, "↑ PAM → vasoconstriction → VSC ↓ → PIC ↓\n"
        "Cible : PPC ≥ 70 mmHg (remplissage, vasopresseurs)",
        fontsize=7.5, color=INK2, va="center")

# Lund : capillaire, BHE rompue, filtration selon Starling
canvas(a2, 8, 7)
a2.set_title("Lund : BHE rompue, forces de Starling", loc="left", color=ORANGE,
             fontweight="bold")
a2.add_patch(Rectangle((0.6, 3.1), 6.8, 1.0, fc=ORANGE + "22", ec="none"))
for y in (3.1, 4.1):
    xs = np.linspace(0.6, 7.4, 18)
    for i, (xa, xb) in enumerate(zip(xs[:-1], xs[1:])):
        if i % 2 == 0:
            a2.plot([xa, xb], [y, y], color=ORANGE, lw=1.5)
a2.text(4, 3.6, "capillaire (paroi lésée)", ha="center", va="center", fontsize=8,
        color=INK2)
for x in (1.3, 2.5):
    a2.add_patch(FancyArrowPatch((x, 4.2), (x, 5.3), arrowstyle="-|>", mutation_scale=10,
                                 color=ORANGE, lw=1.5))
a2.text(1.9, 5.85, "Pc : filtration\n→ œdème", ha="center", va="center", fontsize=8,
        color=ORANGE, fontweight="bold")
for x in (5.5, 6.7):
    a2.add_patch(FancyArrowPatch((x, 5.3), (x, 4.2), arrowstyle="-|>", mutation_scale=10,
                                 color=AQUA, lw=1.5))
a2.text(6.1, 5.85, "πc : réabsorption\noncotique", ha="center", va="center", fontsize=8,
        color=AQUA, fontweight="bold")
a2.text(4, 4.75, "tissu cérébral", ha="center", va="center", fontsize=8, color=INK2,
        style="italic")
a2.text(0.1, 1.7, "↓ Pc : métoprolol, clonidine ; PPC acceptée 50–60 mmHg\n"
        "πc maintenue : albumine, transfusion ; bilan neutre\n"
        "Ni mannitol, ni hyperventilation, ni vasopresseurs",
        fontsize=7.5, color=INK2, va="center")

fig.tight_layout(w_pad=1.5)
save(fig, "lund-rosner")
