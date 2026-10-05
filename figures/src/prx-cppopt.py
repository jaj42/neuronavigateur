"""PRx en fonction de la PPC : courbe en U et PPC optimale (données simulées)."""

import numpy as np
from _style import BLUE, INK2, ORANGE, TEXTWIDTH, ZONE, fr, plt, save

rng = np.random.default_rng(7)
centres = np.arange(52.5, 100, 5)
copt = 76
prx = 0.00055 * (centres - copt) ** 2 - 0.12 + rng.normal(0, 0.025, centres.size)
err = rng.uniform(0.04, 0.08, centres.size)

x = np.linspace(50, 100, 300)
fit = np.polyval(np.polyfit(centres, prx, 2), x)
xopt = x[np.argmin(fit)]

fig, ax = plt.subplots(figsize=(TEXTWIDTH, 3.0))
ax.axhspan(0.25, 0.6, color=ZONE, zorder=0)
ax.text(51, 0.57, "PRx > 0,25 : réactivité vasculaire altérée", color=INK2, fontsize=8, va="top")
ax.axhline(0, color=INK2, lw=0.8)
ax.bar(centres, prx, width=4.4, color=BLUE, alpha=0.35, edgecolor="none")
ax.errorbar(centres, prx, yerr=err, fmt="none", ecolor=BLUE, elinewidth=0.8, capsize=2)
ax.plot(x, fit, color=ORANGE)
ax.axvline(xopt, color=ORANGE, lw=1, ls=(0, (4, 3)))
ax.annotate(f"PPCopt ≈ {xopt:.0f} mmHg\n(minimum de la courbe)", (xopt, fit.min()),
            xytext=(xopt + 3, -0.3), va="top", color=ORANGE, fontweight="bold", fontsize=8,
            arrowprops=dict(arrowstyle="-", color=ORANGE, lw=0.8))
ax.text(51, -0.47, "← ischémie", color=INK2, fontsize=8)
ax.text(99, -0.47, "hyperhémie →", color=INK2, fontsize=8, ha="right")
ax.set_xlim(50, 100)
ax.set_ylim(-0.5, 0.6)
ax.set_yticks(np.arange(-0.4, 0.61, 0.2), [fr(v) for v in np.arange(-0.4, 0.61, 0.2)])
ax.set_xlabel("PPC (mmHg), classes de 5 mmHg sur les dernières heures")
ax.set_ylabel("PRx (corrélation PAM–PIC)")
save(fig, "prx-cppopt")
