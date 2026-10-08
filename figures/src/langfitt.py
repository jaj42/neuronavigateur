"""Courbe pression-volume intracrânienne (Langfitt)."""

import numpy as np
from _style import BLUE, INK2, TEXTWIDTH, ZONE, plt, save

v = np.linspace(0, 100, 500)
pic = 8 + 0.6 * (np.exp(v / 19) - 1)

fig, ax = plt.subplots(figsize=(TEXTWIDTH, 3.0))
ax.axhspan(5, 15, color=ZONE, zorder=0)
ax.text(99, 6, "PIC normale (adulte couché) : 5–15 mmHg", color=INK2, fontsize=8, ha="right")
ax.axhline(22, color=INK2, lw=0.8, ls=(0, (4, 3)))
ax.text(2, 23, "seuil de traitement : 22 mmHg (BTF 2016)", color=INK2, fontsize=8)
ax.plot(v, pic, color=BLUE)

# Même ΔV appliqué à deux endroits de la courbe.
for x0, tx, ty, ha in ((10, 10, 6.5, "left"), (78, 77, 50, "right")):
    x1 = x0 + 8
    p0, p1 = (8 + 0.6 * (np.exp(x / 19) - 1) for x in (x0, x1))
    ax.plot([x0, x1, x1], [p0, p0, p1], color=INK2, lw=1)
    ax.text(tx, ty, f"même ΔV → ΔP ≈ {p1 - p0:.0f} mmHg", color=INK2, fontsize=8,
            ha=ha, va="top")

for x, y, lab in ((18, 42, "1. compensation\n(LCR et sang veineux\nchassés)"),
                  (50, 60, "2. compliance\népuisée"),
                  (68, 68, "3. décompensation")):
    ax.text(x, y, lab, ha="center", va="top", color=BLUE, fontsize=8, fontweight="bold")
ax.set_xlim(0, 100)
ax.set_ylim(0, 72)
ax.set_xticks([])
ax.set_xlabel("Volume intracrânien ajouté (sang, œdème, masse) →")
ax.set_ylabel("PIC (mmHg)")
save(fig, "langfitt")
