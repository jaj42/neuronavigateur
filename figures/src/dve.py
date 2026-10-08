"""Montage d'une dérivation ventriculaire externe : zéro, hauteur, chambre, poche."""

from matplotlib.patches import Circle, Ellipse, FancyBboxPatch, Rectangle
from _diagram import canvas
from _style import AQUA, BLUE, INK, INK2, MUTED, ORANGE, TEXTWIDTH, plt, save

fig, ax = plt.subplots(figsize=(TEXTWIDTH, 3.2))
canvas(ax, 16, 8.4)

ZERO = 3.6      # niveau du conduit auditif externe (zéro)
CM = 0.2        # 1 cmH2O sur le dessin
H = 15          # hauteur prescrite, cmH2O
top = ZERO + H * CM

# Tête de profil, ventricule et cathéter (point de Kocher)
ax.add_patch(Circle((2.4, ZERO + 0.4), 1.7, fc=MUTED + "18", ec=MUTED, lw=1.2))
ax.add_patch(Ellipse((2.3, ZERO + 0.6), 1.3, 0.55, angle=15, fc=AQUA + "40", ec=AQUA, lw=1))
ax.text(2.0, ZERO - 0.35, "ventricule\nlatéral", ha="center", va="top", fontsize=7, color=INK2)
ax.add_patch(Circle((3.75, ZERO), 0.09, color=INK))
ax.text(3.85, ZERO - 0.15, "CAE", ha="left", va="top", fontsize=7, color=INK2)
cat = [(2.5, ZERO + 0.7), (2.9, ZERO + 2.0), (4.2, ZERO + 2.4), (6.2, ZERO + 2.4),
       (6.2, ZERO + 0.6)]
ax.plot(*zip(*cat), color=AQUA, lw=2)
ax.text(4.3, ZERO + 2.6, "cathéter tunnélisé", fontsize=7, color=INK2)

# Robinet et capteur de pression sur la ligne
ax.add_patch(Circle((6.2, ZERO + 1.5), 0.17, fc="white", ec=INK, lw=1.2))
ax.plot([6.03, 6.37], [ZERO + 1.5, ZERO + 1.5], color=INK, lw=1.2)
ax.text(5.9, ZERO + 1.5, "robinet", ha="right", va="center", fontsize=7, color=INK2)
ax.add_patch(Rectangle((5.65, ZERO + 0.62), 0.55, 0.36, fc=BLUE + "30", ec=BLUE, lw=1))
ax.text(5.55, ZERO + 0.8, "capteur\nde PIC", ha="right", va="center", fontsize=7, color=BLUE)

# Ligne du zéro
ax.plot([0.4, 15.6], [ZERO, ZERO], color=INK2, lw=0.9, ls=(0, (4, 3)))
ax.text(15.6, ZERO - 0.15, "0 cmH$_2$O : conduit auditif\nexterne (trou de Monro)", ha="right",
        va="top", fontsize=7.5, color=INK2)

# Colonne graduée et chambre de recueil
x = 9.6
ax.plot([6.2, 6.2, x], [ZERO + 0.6, ZERO - 0.4, ZERO - 0.4], color=AQUA, lw=2)
ax.plot([x, x], [ZERO - 0.4, top], color=AQUA, lw=2)
for c in range(0, 26, 5):
    y = ZERO + c * CM
    ax.plot([x - 0.5, x - 0.25], [y, y], color=INK2, lw=0.8)
    ax.text(x - 0.6, y, f"{c}", ha="right", va="center", fontsize=6.5, color=INK2)
ax.plot([x - 0.38, x - 0.38], [ZERO, ZERO + 25 * CM], color=INK2, lw=0.8)
ax.text(x - 1.25, ZERO + 12.5 * CM, "cmH$_2$O", rotation=90, ha="center", va="center",
        fontsize=7, color=INK2)
ax.plot([x, x + 0.6], [top, top], color=AQUA, lw=2)
ax.add_patch(FancyBboxPatch((x + 0.6, top - 1.8), 1.0, 1.95,
                            boxstyle="round,pad=0.02,rounding_size=0.12",
                            fc="white", ec=INK2, lw=1.1))
ax.add_patch(Rectangle((x + 0.62, top - 1.78), 0.96, 0.5, fc=AQUA + "40", ec="none"))
for k in range(3):
    ax.add_patch(Circle((x + 0.95, top - 0.25 - 0.32 * k), 0.06, color=AQUA))
ax.text(x + 1.75, top - 0.9, "chambre\ngraduée", va="center", fontsize=7, color=INK2)

# Hauteur prescrite
ax.annotate("", xy=(x + 3.2, top), xytext=(x + 3.2, ZERO),
            arrowprops=dict(arrowstyle="<->", color=ORANGE, lw=1.4))
ax.plot([x + 0.6, x + 3.4], [top, top], color=ORANGE, lw=0.9, ls=(0, (2, 2)))
ax.text(x + 3.4, (ZERO + top) / 2, "hauteur\nprescrite\n+15 cmH$_2$O\n≈ 11 mmHg",
        va="center", fontsize=8, color=ORANGE, fontweight="bold")

# Poche
ax.plot([x + 1.1, x + 1.1], [top - 1.8, ZERO - 1.9], color=INK2, lw=1.2)
ax.add_patch(FancyBboxPatch((x + 0.5, ZERO - 3.4), 1.2, 1.5,
                            boxstyle="round,pad=0.02,rounding_size=0.3",
                            fc=AQUA + "20", ec=INK2, lw=1.1))
ax.text(x + 1.9, ZERO - 2.65, "poche", va="center", fontsize=7, color=INK2)

save(fig, "dve")
