"""Arbre décisionnel des dysnatrémies du cérébrolésé (DI, SIADH, perte de sel)."""

from _diagram import arrow, box, canvas
from _style import AQUA, BLUE, INK2, MUTED, ORANGE, TEXTWIDTH, plt, save

fig, ax = plt.subplots(figsize=(TEXTWIDTH, 4.6))
canvas(ax, 16, 11.5)

top = box(ax, 8, 10.8, "Dysnatrémie chez le cérébrolésé", MUTED, w=5.6, h=0.8, bold=True)

hyper = box(ax, 4, 9.0, "Na$^+$ > 145 mmol/L", ORANGE, w=3.4, h=0.8, bold=True)
hypo = box(ax, 12, 9.0, "Na$^+$ < 135 mmol/L", BLUE, w=3.4, h=0.8, bold=True)
arrow(ax, (6.5, 10.4), (4.5, 9.4))
arrow(ax, (9.5, 10.4), (11.5, 9.4))

q1 = box(ax, 4, 7.2, "Polyurie > 400 mL/3 h\net densité urinaire < 1005 ?", ORANGE, w=5.0, h=1.0,
         fill=0.05)
arrow(ax, (4, 8.6), (4, 7.7))
di = box(ax, 2.2, 4.6, "Diabète insipide central\n(chirurgie hypophysaire, TC)\n"
         "→ desmopressine 2 µg IV\n→ compenser la diurèse", ORANGE, w=4.2, h=1.9, size=7.5)
autre = box(ax, 6.2, 4.6, "Autres causes :\nosmothérapie (SSH,\nmannitol), apports\n"
            "d'eau insuffisants", MUTED, w=3.4, h=1.9, fill=0.06, size=7.5)
arrow(ax, (3.2, 6.7), (2.3, 5.55), text="oui", tx=-0.45)
arrow(ax, (4.8, 6.7), (5.8, 5.55), text="non", tx=0.45)

q2 = box(ax, 12, 7.2, "Osmolalité plasmatique basse\net natriurèse > 30 mmol/L", BLUE, w=5.0,
         h=1.0, fill=0.05)
arrow(ax, (12, 8.6), (12, 7.7))
q3 = box(ax, 12, 5.6, "Volémie et bilan sodé ?", BLUE, w=4.0, h=0.7, fill=0.05)
arrow(ax, (12, 6.7), (12, 5.95))
csw = box(ax, 10.1, 3.3, "Perte de sel (CSW)\nhypovolémie,\nbilan sodé négatif\n"
          "→ NaCl, ± fludrocortisone", AQUA, w=4.0, h=1.9, size=7.5)
siadh = box(ax, 14.1, 3.3, "SIADH\neuvolémie\n→ restriction hydrique\n(jamais dans l'HSA)",
            BLUE, w=3.6, h=1.9, size=7.5)
arrow(ax, (11.2, 5.25), (10.3, 4.25), text="hypovolémie", tx=-1.1)
arrow(ax, (12.8, 5.25), (13.8, 4.25), text="euvolémie", tx=0.95)

ax.text(8, 0.9, "Hyponatrémie symptomatique (convulsions, HTIC) : NaCl hypertonique en bolus. "
        "Hyponatrémie chronique :\nne pas corriger de plus de 8–10 mmol/L par 24 h "
        "(myélinolyse). Ionogramme sanguin et urinaire répétés.",
        ha="center", va="center", fontsize=7.5, color=INK2)
save(fig, "arbre-natremie")
