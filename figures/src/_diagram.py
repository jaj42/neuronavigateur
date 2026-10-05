"""Small helpers for box-and-arrow diagrams drawn in data coordinates."""

from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
from _style import INK, INK2


def canvas(ax, w, h):
    ax.set_xlim(0, w)
    ax.set_ylim(0, h)
    ax.set_aspect("equal")
    ax.axis("off")


def box(ax, x, y, text, color, w=2.6, h=0.9, fill=0.12, size=8, bold=False):
    """Rounded box centred on (x, y); returns its (x, y, w, h)."""
    ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h,
                                boxstyle="round,pad=0.02,rounding_size=0.15",
                                fc=color + f"{int(fill * 255):02x}", ec=color, lw=1.2))
    ax.text(x, y, text, ha="center", va="center", fontsize=size, color=INK,
            fontweight="bold" if bold else "normal", linespacing=1.15)
    return (x, y, w, h)


def arrow(ax, p, q, color=INK2, rad=0.0, lw=1.2, text=None, tx=0.0, ty=0.0, size=7.5):
    ax.add_patch(FancyArrowPatch(p, q, arrowstyle="-|>", mutation_scale=10, color=color,
                                 lw=lw, connectionstyle=f"arc3,rad={rad}",
                                 shrinkA=2, shrinkB=2))
    if text:
        ax.text((p[0] + q[0]) / 2 + tx, (p[1] + q[1]) / 2 + ty, text, fontsize=size,
                color=INK2, ha="center", va="center")
