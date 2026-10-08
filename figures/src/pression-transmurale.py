"""Pression transmurale d'un anévrysme rompu : PAM dedans, PIC dehors."""

import numpy as np
from matplotlib.patches import Circle, FancyArrowPatch, Rectangle
from _diagram import arrow, box, canvas
from _style import BLUE, INK, INK2, ORANGE, TEXTWIDTH, plt, save

fig, ax = plt.subplots(figsize=(TEXTWIDTH, 2.85))
canvas(ax, 16, 7.6)
ax.set_ylim(0.6, 7.6)

# Artère porteuse et sac anévrysmal
ax.add_patch(Rectangle((0.3, 0.9), 7.4, 1.1, fc=ORANGE + "30", ec="none"))
ax.plot([0.3, 3.1], [2.0, 2.0], color=ORANGE, lw=1.6)
ax.plot([4.9, 7.7], [2.0, 2.0], color=ORANGE, lw=1.6)
ax.plot([0.3, 7.7], [0.9, 0.9], color=ORANGE, lw=1.6)
cx, cy, r = 4.0, 3.9, 1.75
t = np.linspace(-0.3 * np.pi, 1.3 * np.pi, 200)
xs = np.r_[4.9, cx + r * np.cos(t), 3.1]
ys = np.r_[2.0, cy + r * np.sin(t), 2.0]
ax.fill(np.r_[xs, 4.9], np.r_[ys, 2.0], color=ORANGE + "30", lw=0)
ax.plot(xs, ys, color=ORANGE, lw=1.6)
ax.add_patch(Circle((cx + 0.15, cy + r - 0.05), 0.32, fc="#8b2a12", ec="none"))
ax.annotate("caillot", xy=(cx + 0.4, cy + r + 0.1), xytext=(cx + 1.6, cy + r + 0.5),
            fontsize=7.5, color=INK2, va="center",
            arrowprops=dict(arrowstyle="-", color=INK2, lw=0.8))
ax.text(cx, cy, "PAM", ha="center", va="center", fontsize=10, color=ORANGE, fontweight="bold")
ax.text(1.2, 1.45, "artère porteuse", fontsize=7.5, color=INK2, va="center")

for a in np.deg2rad([20, 160, 200, -20]):
    p0 = (cx + 0.55 * np.cos(a), cy + 0.55 * np.sin(a))
    p1 = (cx + (r - 0.15) * np.cos(a), cy + (r - 0.15) * np.sin(a))
    ax.add_patch(FancyArrowPatch(p0, p1, arrowstyle="-|>", mutation_scale=9, color=ORANGE,
                                 lw=1.3))
for a in np.deg2rad([40, 140, 180, 0]):
    p0 = (cx + (r + 0.9) * np.cos(a), cy + (r + 0.9) * np.sin(a))
    p1 = (cx + (r + 0.12) * np.cos(a), cy + (r + 0.12) * np.sin(a))
    ax.add_patch(FancyArrowPatch(p0, p1, arrowstyle="-|>", mutation_scale=9, color=BLUE,
                                 lw=1.3))
ax.text(cx - r - 1.1, cy + 1.3, "PIC", ha="center", va="center", fontsize=10, color=BLUE,
        fontweight="bold")

# Formule et deux situations
box(ax, 12.0, 6.6, "Pression transmurale = PAM − PIC", INK, w=7.6, h=0.9, fill=0.06,
    bold=True, size=9)
box(ax, 10.0, 4.3, "Laryngoscopie chez un\npatient mal anesthésié :\nPAM ↑", ORANGE, w=3.9,
    h=1.6, size=7.5)
box(ax, 14.0, 4.3, "Drainage rapide du LCR\navant l'exclusion :\nPIC ↓", BLUE, w=3.9, h=1.6,
    size=7.5)
box(ax, 12.0, 1.6, "Pression transmurale ↑ :\nle caillot peut être chassé\n= resaignement",
    ORANGE, w=5.2, h=1.4, fill=0.3, size=8, bold=True)
arrow(ax, (10.0, 3.45), (11.2, 2.35))
arrow(ax, (14.0, 3.45), (12.8, 2.35))
save(fig, "pression-transmurale")
