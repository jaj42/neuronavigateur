"""DSC en fonction de la PaCO2 et de la PaO2."""

import numpy as np
from _style import BLUE, INK2, ORANGE, TEXTWIDTH, ZONE, plt, save

fig, (a1, a2) = plt.subplots(1, 2, figsize=(TEXTWIDTH, 2.8), sharey=True)

# PaCO2 : relation quasi linéaire entre 20 et 80 mmHg (≈ 1,25 mL/100 g/min par mmHg).
co2 = np.linspace(10, 100, 500)
lin = 50 + 1.25 * (co2 - 40)
dsc = 25 + 75 / (1 + np.exp(-(co2 - 50) / 9.5))
dsc = np.where((co2 > 22) & (co2 < 78), lin, dsc)
# raccord continu
dsc = np.convolve(np.pad(dsc, 15, mode="edge"), np.ones(31) / 31, mode="valid")
a1.axvspan(35, 45, color=ZONE, zorder=0)
a1.plot(co2, dsc, color=BLUE)
a1.plot([40], [50], "o", ms=6, color=BLUE, mec="white", mew=1.5)
a1.annotate("PaCO$_2$ 40 → DSC 50", (40, 50), xytext=(48, 32), color=INK2, fontsize=8,
            arrowprops=dict(arrowstyle="-", color=INK2, lw=0.6))
a1.text(14, 95, "≈ 2 à 4 % de DSC\npar mmHg de PaCO$_2$", color=INK2, fontsize=8, va="top")
a1.set_xlim(10, 100)
a1.set_xlabel("PaCO$_2$ (mmHg)")
a1.set_ylabel("DSC (mL/100 g/min)")
a1.set_title("Réactivité au CO$_2$", loc="left", color=BLUE, fontweight="bold")

# PaO2 : plateau au-dessus de ~60 mmHg, vasodilatation en dessous.
o2 = np.linspace(20, 300, 600)
dsc2 = 50 + 60 * np.exp(-(o2 - 20) / 18)
a2.axvspan(20, 60, color=ZONE, zorder=0)
a2.plot(o2, dsc2, color=ORANGE)
a2.text(62, 105, "hypoxémie (< 60 mmHg) :\nvasodilatation", ha="left", va="top", color=INK2, fontsize=8)
a2.text(180, 55, "pas d'effet notable\nau-dessus de ~60 mmHg", ha="center", va="bottom",
        color=INK2, fontsize=8)
a2.set_xlim(20, 300)
a2.set_ylim(0, 115)
a2.set_xlabel("PaO$_2$ (mmHg)")
a2.set_title("Réactivité à l'O$_2$", loc="left", color=ORANGE, fontweight="bold")
fig.tight_layout(w_pad=2)
save(fig, "reactivite-co2-o2")
