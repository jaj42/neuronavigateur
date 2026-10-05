"""Autorégulation du DSC : plateau normal, plateau déplacé à droite (HTA chronique), perte."""

import numpy as np
from _style import AQUA, BLUE, INK2, ORANGE, TEXTWIDTH, ZONE, plt, save


def plateau(pam, lo, hi, dsc=50.0):
    """DSC passif sous lo et au-dessus de hi, constant entre les deux (raccords lissés)."""
    y = np.where(pam < lo, dsc * pam / lo, dsc + np.clip(pam - hi, 0, None) * 0.9)
    k = 21
    return np.convolve(np.pad(y, k // 2, mode="edge"), np.ones(k) / k, mode="valid")


pam = np.linspace(0, 200, 801)
normal = plateau(pam, 60, 150)
hta = plateau(pam, 85, 175)
perdue = 50 * pam / 80

fig, ax = plt.subplots(figsize=(TEXTWIDTH, 3.1))
ax.axvspan(60, 150, color=ZONE, zorder=0)
ax.text(105, 106, "zone d'autorégulation\n(sujet sain)", ha="center", va="top",
        color=INK2, fontsize=8)
ax.plot(pam, normal, color=BLUE, label="Normal")
ax.plot(pam, hta, color=ORANGE, ls=(0, (6, 2)), label="HTA chronique")
ax.plot(pam, perdue, color=AQUA, ls=(0, (2, 1.5)), label="Autorégulation abolie")

ax.annotate("Normal", (125, 50), xytext=(125, 58), color=BLUE, ha="center",
            fontweight="bold")
ax.annotate("HTA chronique :\nplateau décalé à droite", (165, 50), xytext=(118, 14),
            color=ORANGE, ha="left", fontweight="bold",
            arrowprops=dict(arrowstyle="-", color=ORANGE, lw=0.8))
ax.annotate("Autorégulation abolie :\nDSC passif à la pression", (100, 50 * 100 / 80),
            xytext=(4, 84), color=AQUA, fontweight="bold",
            arrowprops=dict(arrowstyle="-", color=AQUA, lw=0.8))
ax.text(30, 3, "← ischémie", color=INK2, fontsize=8)
ax.text(198, 3, "hyperhémie, œdème →", color=INK2, fontsize=8, ha="right")

ax.set_xlim(0, 200)
ax.set_ylim(0, 110)
ax.set_xlabel("Pression de perfusion cérébrale (≈ PAM) (mmHg)")
ax.set_ylabel("DSC (mL/100 g/min)")
save(fig, "autoregulation")
