# Le Neuronavigateur

*Neuro-anesthésie-réanimation : le kit de démarrage de l'interne*

- **Lire en ligne :** <https://jaj42.github.io/neuronavigateur/>
- **Télécharger le PDF (A4) :** <https://jaj42.github.io/neuronavigateur/le-neuronavigateur.pdf>

## Le projet

*Le Neuronavigateur* est un livret pédagogique en français destiné aux internes d'anesthésie-réanimation
qui débutent en neurochirurgie. Il sert à la fois de référence rapide et de support d'apprentissage :
il part de l'anatomie et de la physiologie cérébrales, puis aborde les situations concrètes du bloc
opératoire, de la neuroradiologie interventionnelle et de la réanimation.

Le contenu s'appuie sur les protocoles du service, sur les recommandations françaises (SFAR et sociétés
associées) et internationales (BTF, SIBICC, AHA, NCS…), et sur la littérature. Les références ont été
vérifiées sur PubMed.

> **Avertissement.** Ce document est un outil pédagogique. Il ne remplace ni les protocoles validés du
> service, ni l'avis du senior. Les points qui attendent une validation médicale sont listés dans
> [`A_VALIDER.md`](A_VALIDER.md).

## Sommaire

**Partie I : Bases.** Anatomie utile, physiologie, physiopathologie, pharmacologie, monitorage.

**Partie II : Bloc opératoire.** Consultation et préopératoire, craniotomie programmée, fosse postérieure,
chirurgie éveillée, chirurgie de l'épilepsie, base du crâne et voie endonasale, chirurgie vasculaire
programmée (anévrysmes, moya-moya), névralgie du trijumeau, neuroradiologie interventionnelle.

**Partie III : Urgences et réanimation.** HTIC aiguë, traumatisme crânien grave, hémorragie
sous-arachnoïdienne anévrysmale, AVC ischémique, dysnatrémies et dérivation ventriculaire externe.

**Annexes.** Fiches mémo (cibles, doses, dilutions), scores, abréviations, crédits des images,
bibliographie.

Chaque chapitre s'ouvre sur des objectifs, se termine par un encadré « À retenir » et, pour les chapitres
cliniques, par une fiche pratique.

## Construire le livre

Le livre est écrit avec [Quarto](https://quarto.org) (format *book*) et produit deux sorties : un PDF A4
(LuaLaTeX, polices TeX Gyre) et un site HTML.

```bash
quarto render              # PDF + HTML dans _book/
quarto render --to html    # HTML seul
quarto preview             # aperçu local avec rechargement automatique
```

Les figures sont générées par des scripts matplotlib et déjà incluses dans le dépôt. Pour les
régénérer après modification d'un script de `figures/src/` :

```bash
python figures/build.py
```

Chaque push sur `main` déclenche le workflow [`.github/workflows/publish.yml`](.github/workflows/publish.yml),
qui rend le livre et le publie sur GitHub Pages.

## Organisation du dépôt

| Chemin | Contenu |
|---|---|
| `_quarto.yml` | configuration du livre (chapitres, formats PDF et HTML) |
| `index.qmd` | avant-propos et mode d'emploi |
| `parties/` | les 19 chapitres |
| `annexes/` | bibliographie, fiches mémo, scores, abréviations, crédits des images |
| `figures/` | figures générées (`src/` : scripts) et images Wikimedia sous licence libre (`wikimedia/`) |
| `references.bib`, `vancouver.csl` | bibliographie et style de citation |
| `scripts/` | outils de vérification (entrées SFAR, crédits des images) |
| `sources/` | documents sources : protocoles, transcriptions de cours, notes de lecture (non rendus) |
| `styles/` | ajustements CSS de la version HTML |

## Auteur

Jona JOACHIM
