"""Évolution triphasique après chirurgie hypophysaire : diurèse et natrémie (schéma qualitatif)."""

import numpy as np
from _style import BLUE, INK2, MUTED, ORANGE, TEXTWIDTH, ZONE, plt, save

d = np.linspace(0, 14, 600)


def bump(c, s):
    return np.exp(-((d - c) / s) ** 2)


# Écarts à la normale, unités arbitraires : DI maximal à J2, phase antidiurétique J7–J10
na = 0.8 * bump(1.8, 1.0) - 1.0 * bump(9.5, 1.6)
diu = 1.0 * bump(1.8, 1.0) - 0.45 * bump(8.5, 1.8)
late = d > 11.5
na_di = np.where(late, 0.6 * np.clip((d - 11.5) / 1.5, 0, 1), np.nan)
diu_di = np.where(late, 0.8 * np.clip((d - 11.5) / 1.5, 0, 1), np.nan)

fig, axes = plt.subplots(2, 1, figsize=(TEXTWIDTH, 3.8), sharex=True)
for ax, y, ydi, color, name in ((axes[0], diu, diu_di, ORANGE, "Diurèse"),
                                (axes[1], na, na_di, BLUE, "Natrémie")):
    for a, b in ((0.5, 3.2), (7, 10.5)):
        ax.axvspan(a, b, color=ZONE, lw=0, zorder=0)
    ax.axhline(0, color=MUTED, lw=0.8, ls=(0, (4, 3)))
    ax.plot(d, y, color=color)
    ax.plot(d, np.where(late, y, np.nan) + ydi, color=color, lw=1.4, ls=(0, (3, 2)))
    ax.set_ylim(-1.25, 1.25)
    ax.set_yticks([-0.8, 0, 0.8])
    ax.set_yticklabels(["basse", "normale", "élevée"], fontsize=7.5)
    ax.set_ylabel(name)
    ax.grid(axis="x", visible=False)

tr = axes[0].get_xaxis_transform()
for x, t in ((1.85, "1. Diabète insipide\n(J1–J2)"), (8.75, "2. Phase antidiurétique\n(J7–J10)"),
             (12.6, "3. Retour à la normale\nou DI permanent (tirets)")):
    axes[0].text(x, 1.03, t, transform=tr, ha="center", va="bottom", fontsize=7.5, color=INK2,
                 fontweight="bold")
axes[1].annotate("hyponatrémie : nadir vers J9–J10,\npatient souvent rentré à domicile",
                 xy=(9.5, -1.0), xytext=(3.8, -0.75), fontsize=7.5, color=INK2, va="center",
                 arrowprops=dict(arrowstyle="-", color=INK2, lw=0.8))
axes[1].set_xlim(0, 14)
axes[1].set_xticks(range(0, 15, 2))
axes[1].set_xticklabels([f"J{k}" for k in range(0, 15, 2)])
axes[1].set_xlabel("Jours après la chirurgie")
fig.tight_layout(h_pad=0.6)
save(fig, "di-triphasique")
