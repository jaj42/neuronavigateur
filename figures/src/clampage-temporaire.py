"""Clampage temporaire de l'artère porteuse : tolérance selon la durée (Samson 1994) et gestes."""

from _style import AQUA, INK, INK2, ORANGE, TEXTWIDTH, plt, save

fig, ax = plt.subplots(figsize=(TEXTWIDTH, 2.3))
ax.axvspan(0, 14, ymin=0.1, ymax=0.45, color=AQUA, alpha=0.35, lw=0)
for k in range(17):
    ax.axvspan(14 + k, 15 + k, ymin=0.1, ymax=0.45, color=ORANGE, alpha=0.12 + 0.03 * k, lw=0)
ax.axvspan(31, 40, ymin=0.1, ymax=0.45, color=ORANGE, alpha=0.95, lw=0)
ax.text(7, 0.275, "< 14 min :\nhabituellement tolérée", ha="center", va="center",
        fontsize=7.5, color=INK, transform=ax.get_xaxis_transform())
ax.text(22.5, 0.275, "tolérance décroissante\n(moins bonne après 61 ans\net en mauvais grade)",
        ha="center", va="center", fontsize=7.5, color=INK, transform=ax.get_xaxis_transform())
ax.text(35.5, 0.275, "> 31 min :\ninfarctus\nchez tous", ha="center", va="center",
        fontsize=7.5, color="white", fontweight="bold", transform=ax.get_xaxis_transform())

tr = ax.get_xaxis_transform()
ax.annotate("Pose du clamp : chronomètre lancé,\ndurée annoncée à voix haute ;\n"
            "noradrénaline diluée (5 µg/mL)\ntitrée, sans bolus", xy=(0, 0.47),
            xytext=(0.3, 0.97), xycoords=tr, textcoords=tr, fontsize=7.5, color=INK2,
            va="top", arrowprops=dict(arrowstyle="-|>", color=INK2, lw=0.9))
ax.text(39.7, 0.97, "Au déclampage :\nretour à la pression de base",
        transform=tr, fontsize=7.5, color=INK2, va="top", ha="right")
ax.set_xlim(0, 40)
ax.set_ylim(0, 1)
ax.set_yticks([])
ax.spines["left"].set_visible(False)
ax.grid(False)
ax.set_xticks([0, 5, 10, 14, 20, 25, 31, 35, 40])
ax.set_xlabel("Durée de l'occlusion temporaire (min)")
save(fig, "clampage-temporaire")
