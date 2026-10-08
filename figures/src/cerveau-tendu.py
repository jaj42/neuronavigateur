"""Devant un cerveau tendu en craniotomie : causes simples d'abord, dans l'ordre."""

from _diagram import arrow, box, canvas
from _style import AQUA, BLUE, INK2, ORANGE, TEXTWIDTH, plt, save

fig, ax = plt.subplots(figsize=(TEXTWIDTH, 3.1))
canvas(ax, 16, 7.6)

steps = [
    ("1. La tête", "flexion, rotation,\nlien de sonde,\nbillot", BLUE),
    ("2. La capnie", "gaz du sang :\nfiltre, sonde coudée,\nbronchospasme", BLUE),
    ("3. La PA", "hypotension\n(vasodilatation) ou\nhypertension\n(hyperhémie)", BLUE),
    ("4. L'anesthésie", "trop légère,\nhalogéné : passer\nen tout IV", BLUE),
    ("5. Oxygénation", "hypoxémie,\nPEP élevée,\nplateau haut", BLUE),
    ("6. Osmothérapie", "SSH ou mannitol\nen 15 min ;\neffet en 10 à 15 min", AQUA),
    ("7. Hyperventilation", "brève, en relais :\nPaCO$_2$ 30–35 mmHg", AQUA),
    ("8. Le chirurgien", "drainage du LCR ;\nimagerie,\ndécompression", ORANGE),
]
w, h = 3.55, 2.2
xs = [2.0, 6.0, 10.0, 14.0]
rows = [5.45, 2.2]
pos = [(xs[i], rows[0]) for i in range(4)] + [(xs[3 - i], rows[1]) for i in range(4)]
for (x, y), (title, body, color) in zip(pos, steps):
    box(ax, x, y, "", color, w=w, h=h, fill=0.1)
    ax.text(x, y + 0.68, title, ha="center", va="center", fontsize=8, fontweight="bold")
    ax.text(x, y - 0.3, body, ha="center", va="center", fontsize=6.8, linespacing=1.15, color=INK2)
for i in range(7):
    (x0, y0), (x1, y1) = pos[i], pos[i + 1]
    if y0 == y1:
        d = w / 2 + 0.03
        s = 1 if x1 > x0 else -1
        arrow(ax, (x0 + s * d, y0), (x1 - s * d, y1))
    else:
        arrow(ax, (x0, y0 - h / 2), (x1, y1 + h / 2))
ax.text(8, 7.15, "Causes simples, à vérifier dans l'ordre (bleu), puis traitements (vert), "
        "puis cause chirurgicale (orange)", ha="center", va="center", fontsize=7.5, color=INK2)
ax.text(8, 0.6, "Gonflement brutal sans cause anesthésique : penser à un hématome à distance "
        "ou à une thrombose veineuse.", ha="center", va="center", fontsize=7.5, color=ORANGE)
save(fig, "cerveau-tendu")
