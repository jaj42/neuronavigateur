"""Spectres Doppler transcrânien (ACM) : normal, HTIC, vasospasme."""

import numpy as np
from _style import AQUA, BLUE, INK2, ORANGE, TEXTWIDTH, fr, plt, save


def spectre(t, vs, vd):
    """Enveloppe de vitesse sur un cycle : pic systolique rapide puis décroissance diastolique."""
    ph = t % 1.0
    up = np.clip(ph / 0.12, 0, 1)
    decay = np.exp(-np.clip(ph - 0.12, 0, None) / 0.35)
    end = np.exp(-0.88 / 0.35)
    sys = end + (1 - end) * np.sin(up * np.pi / 2) ** 2
    shape = np.where(ph < 0.12, sys, decay)
    notch = 0.08 * np.exp(-0.5 * ((ph - 0.35) / 0.04) ** 2)
    shape = np.clip(shape + notch, 0, 1)
    vmin = shape.min()
    return vd + (vs - vd) * (shape - vmin) / (1 - vmin)


t = np.linspace(0, 2, 800)
cases = [
    ("Normal", BLUE, 100, 45),
    ("HTIC", ORANGE, 110, 12),
    ("Vasospasme", AQUA, 240, 120),
]
fig, axes = plt.subplots(1, 3, figsize=(TEXTWIDTH, 2.5), sharey=True)
for ax, (title, col, vs, vd) in zip(axes, cases):
    v = spectre(t, vs, vd)
    vm = v.mean()
    ip = (vs - vd) / vm
    ax.fill_between(t, 0, v, color=col, alpha=0.25, lw=0)
    ax.plot(t, v, color=col, lw=1.5)
    ax.axhline(vm, color=INK2, lw=0.8, ls=(0, (3, 2)))
    ax.set_title(title, loc="left", color=col, fontweight="bold")
    ax.text(0.03, 0.97, f"Vs {vs:.0f}  Vm {vm:.0f}  Vd {vd:.0f}\nIP = {fr(ip, 2)}",
            transform=ax.transAxes, va="top", fontsize=7.5, color=INK2,
            bbox=dict(fc="white", ec="none", alpha=0.8, pad=1))
    ax.set_xticks([])
axes[0].set_ylabel("Vitesse (cm/s)")
axes[0].set_ylim(0, 280)
axes[1].text(1.0, 135, "Vd effondrée,\nIP > 1,4", ha="center", fontsize=8, color=INK2)
axes[2].text(1.0, 20, "Vm > 120 cm/s\n(sévère > 200)", ha="center", fontsize=8, color=INK2)
fig.tight_layout(w_pad=1.2)
fig.text(0.5, -0.01, "temps (2 cycles cardiaques)", ha="center", color=INK2)
save(fig, "dtc")
