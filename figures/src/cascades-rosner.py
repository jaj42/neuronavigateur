"""Cascades de Rosner : vasodilatatrice (PAM basse) et vasoconstrictrice (PAM remontée)."""

import numpy as np
from _diagram import arrow, box, canvas
from _style import AQUA, INK2, ORANGE, TEXTWIDTH, plt, save

fig, axes = plt.subplots(1, 2, figsize=(TEXTWIDTH, 3.0))


def cascade(ax, color, title, entry, labels, center):
    canvas(ax, 8, 7.4)
    ax.set_ylim(0.9, 7.4)
    ax.set_title(title, loc="left", color=color, fontweight="bold")
    pos = {"ppc": (4, 5.4), "vx": (6.5, 3.5), "vsc": (4, 1.6), "pic": (1.5, 3.5)}
    for k, (x, y) in pos.items():
        box(ax, x, y, labels[k], color, w=2.6, h=1.0)
    order = ["ppc", "vx", "vsc", "pic", "ppc"]
    for a, b in zip(order, order[1:]):
        (x0, y0), (x1, y1) = pos[a], pos[b]
        u = np.array([x1 - x0, y1 - y0]) / np.hypot(x1 - x0, y1 - y0)
        arrow(ax, (x0 + u[0] * 1.15, y0 + u[1] * 0.6), (x1 - u[0] * 1.15, y1 - u[1] * 0.6),
              color=color, rad=-0.15)
    box(ax, 1.3, 6.7, entry, color, w=2.0, h=0.7, fill=0.3, bold=True)
    arrow(ax, (2.3, 6.55), (2.75, 5.85), color=color)
    ax.text(4, 3.5, center, ha="center", va="center", color=INK2, fontsize=8, style="italic")


cascade(axes[0], ORANGE, "Cascade vasodilatatrice", "PAM ↓",
        {"ppc": "PPC ↓", "vx": "vasodilatation\nartériolaire",
         "vsc": "volume sanguin\ncérébral ↑", "pic": "PIC ↑"}, "cercle\nvicieux")
cascade(axes[1], AQUA, "Cascade vasoconstrictrice", "PAM ↑",
        {"ppc": "PPC ↑", "vx": "vasoconstriction\nartériolaire",
         "vsc": "volume sanguin\ncérébral ↓", "pic": "PIC ↓"}, "la PIC\nbaisse")

fig.text(0.5, 0.01, "Condition : compliance basse (haut de la courbe de Langfitt) et "
         "autorégulation conservée. Si elle est abolie,\nremonter la PAM ne fait pas baisser "
         "la PIC : c'est le principe du PRx.", ha="center", va="bottom", fontsize=7.5,
         color=INK2)
fig.tight_layout(w_pad=1.5, rect=(0, 0.1, 1, 1))
save(fig, "cascades-rosner")
