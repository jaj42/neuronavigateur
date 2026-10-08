"""AVC ischémique : cœur et pénombre ; bénéfice de la thrombolyse selon le délai (Emberson 2014)."""

import numpy as np
from matplotlib.patches import Circle
from _diagram import canvas
from _style import BLUE, INK, INK2, MUTED, ORANGE, TEXTWIDTH, fr, plt, save

fig, (a1, a2) = plt.subplots(1, 2, figsize=(TEXTWIDTH, 2.9),
                             gridspec_kw={"width_ratios": [1, 1.25]})

# Cœur, pénombre, tissu sain
canvas(a1, 7.4, 6.6)
a1.add_patch(Circle((3.6, 3.4), 3.0, fc=MUTED + "15", ec=MUTED, lw=1))
a1.add_patch(Circle((3.6, 3.4), 2.0, fc=ORANGE + "35", ec=ORANGE, lw=1, ls=(0, (3, 2))))
a1.add_patch(Circle((3.6, 3.4), 0.95, fc=ORANGE, ec="none"))
a1.text(3.6, 3.4, "cœur", ha="center", va="center", fontsize=8, color="white",
        fontweight="bold")
a1.text(3.6, 4.85, "pénombre", ha="center", va="center", fontsize=8, color=INK,
        fontweight="bold")
a1.text(3.6, 5.95, "tissu sain", ha="center", va="center", fontsize=7.5, color=INK2)
a1.annotate("", xy=(5.2, 3.4), xytext=(4.65, 3.4),
            arrowprops=dict(arrowstyle="-|>", color=INK, lw=1.2))
a1.set_title("Cœur et pénombre", loc="left", fontsize=9, fontweight="bold", color=INK)

# Bénéfice de l'altéplase selon le délai
groups = ["< 3 h", "3 à 4,5 h"]
ctrl, alt = [23.1, 30.1], [32.9, 35.3]
x = np.arange(2)
w = 0.36
b1 = a2.bar(x - w / 2, ctrl, w, color=MUTED, label="témoin")
b2 = a2.bar(x + w / 2, alt, w, color=BLUE, label="altéplase")
for bars in (b1, b2):
    for b in bars:
        a2.text(b.get_x() + b.get_width() / 2, b.get_height() + 0.8, fr(b.get_height()) + " %",
                ha="center", va="bottom", fontsize=7, color=INK)
a2.text(2, 3, "> 4,5 h :\nbénéfice non\nsignificatif", ha="center", va="bottom", fontsize=7.5,
        color=INK2)
a2.set_xticks([0, 1])
a2.set_xticklabels(groups)
a2.set_xlim(-0.6, 2.6)
a2.set_ylim(0, 45)
a2.set_ylabel("Sans handicap significatif\nà 3–6 mois (%)")
a2.grid(axis="x", visible=False)
a2.legend(loc="upper right", fontsize=7.5, ncols=2)
a2.set_title("Délai de la thrombolyse", loc="left", fontsize=9, fontweight="bold", color=INK)
fig.tight_layout(w_pad=1.0)
save(fig, "penombre-delai")
