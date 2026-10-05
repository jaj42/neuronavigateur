"""Shared style for the book's matplotlib figures.

Every script imports this module, draws one figure and calls save(fig, name),
which writes figures/<name>.pdf (PDF book) and figures/<name>.png (HTML book).
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager

OUT = Path(__file__).resolve().parent.parent

# TeX Gyre Heros = the book's sans font; fall back to DejaVu Sans if missing.
for f in font_manager.findSystemFonts():
    if "texgyreheros-" in Path(f).name:
        font_manager.fontManager.addfont(f)
FAMILY = "TeX Gyre Heros" if any(
    "TeX Gyre Heros" == e.name for e in font_manager.fontManager.ttflist
) else "DejaVu Sans"

# Categorical slots, fixed order (validated: CVD ΔE ≥ 9, direct labels everywhere).
BLUE = "#2a78d6"
ORANGE = "#eb6834"
AQUA = "#1baf7a"
INK = "#0b0b0b"
INK2 = "#52514e"
MUTED = "#8a8985"
GRID = "#e4e3df"
ZONE = "#f1f0ec"

plt.rcParams.update({
    "font.family": FAMILY,
    "font.size": 9,
    "axes.titlesize": 10,
    "axes.labelsize": 9,
    "axes.labelcolor": INK2,
    "axes.edgecolor": MUTED,
    "axes.linewidth": 0.8,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.grid": True,
    "grid.color": GRID,
    "grid.linewidth": 0.6,
    "xtick.color": INK2,
    "ytick.color": INK2,
    "lines.linewidth": 2,
    "legend.frameon": False,
    "mathtext.fontset": "custom",
    "mathtext.rm": FAMILY,
    "mathtext.it": f"{FAMILY}:italic",
    "mathtext.bf": f"{FAMILY}:bold",
    "mathtext.cal": FAMILY,
    "mathtext.sf": FAMILY,
    "figure.dpi": 100,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.05,
    "axes.formatter.use_locale": False,
})

# Width of the text block in the A4 PDF (210 − 2 × 25 mm).
TEXTWIDTH = 160 / 25.4


def fr(x, nd=1):
    """Format a number with a French decimal comma."""
    return f"{x:.{nd}f}".replace(".", ",")


def save(fig, name):
    fig.savefig(OUT / f"{name}.pdf")
    fig.savefig(OUT / f"{name}.png", dpi=200)
    plt.close(fig)
    print(f"figures/{name}.pdf, .png")
