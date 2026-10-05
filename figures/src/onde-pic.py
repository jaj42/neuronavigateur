"""Morphologie de l'onde de PIC : P1 > P2 > P3 (compliance normale) vs P2 > P1 (compliance basse)."""

import numpy as np
from _style import BLUE, INK2, ORANGE, TEXTWIDTH, plt, save


def g(t, mu, s):
    return np.exp(-0.5 * ((t - mu) / s) ** 2)


def beat(t, a1, a2, a3):
    return a1 * g(t, 0.12, 0.045) + a2 * g(t, 0.30, 0.07) + a3 * g(t, 0.50, 0.06)


t = np.linspace(0, 0.8, 400)
cases = [
    ("Compliance normale", BLUE, (1.0, 0.7, 0.45), 10, 4),
    ("Compliance basse", ORANGE, (0.75, 1.15, 0.55), 25, 9),
]
fig, axes = plt.subplots(1, 2, figsize=(TEXTWIDTH, 2.6), sharey=True)
for ax, (title, col, amps, base, amp) in zip(axes, cases):
    y = base + amp * beat(t, *amps)
    tt = np.concatenate([t, t + 0.8])
    ax.plot(tt, np.concatenate([y, y]), color=col)
    for mu, lab in ((0.12, "P1"), (0.30, "P2"), (0.50, "P3")):
        i = np.argmin(abs(t - mu))
        ax.annotate(lab, (t[i], y[i]), xytext=(0, 6), textcoords="offset points",
                    ha="center", color=INK2, fontsize=8, fontweight="bold")
    ax.set_title(title, loc="left", color=col, fontweight="bold")
    ax.set_xticks([])
    ax.set_xlabel("temps (2 cycles cardiaques)")
axes[0].set_ylabel("PIC (mmHg)")
axes[0].text(0.8, 18.5, "P1 (percussion) > P2 (tidal) > P3 (dicrote)", color=INK2,
             fontsize=8, ha="center")
axes[1].text(0.8, 39, "P2 > P1 : cerveau peu compliant", color=INK2, fontsize=8, ha="center")
axes[0].set_ylim(5, 42)
fig.tight_layout(w_pad=2)
save(fig, "onde-pic")
