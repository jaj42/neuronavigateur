# Plan : « Starter kit » neuro-anesthésie-réanimation pour internes (Quarto book → PDF A4)

## Context
New anesthesiology interns starting in neurosurgery need a quick reference that also teaches: it should start with general physiology and then cover specific cases. It should be in French and illustrated, with references. Sources:
- `sources/transcripts_cours.txt` → 2 audio transcripts (≈52 kB: neuro-anatomy, physiology, pathophysiology, anesthetic agents, an extradural hematoma case; ≈60 kB: interventional neuroradiology / NRI). They contain transcription errors, so they're used as a knowledge base to rewrite from, never quoted.
- `sources/additional.txt`: Lund vs Rosner, CPPopt/PRx, key refs (Asgeirsson 1994, Grände 2006, Robertson 1999, Steiner 2002, Aries 2012, COGiTATE 2021, wrongly dated 2023 in the file).
- `sources/papers/*.pdf`: key articles supplied as full text: Payen 2007 (ACSOS, *Ann Fr Anesth Reanim*), Rosner 1995 (PPC, *J Neurosurg*), Eker 1998 (Lund concept, *Crit Care Med*), Lukaszewicz 2011 (water and brain injury, *Curr Opin Anaesthesiol*). `sources/papers/chandra/<nom>/<nom>.md` holds their markdown conversions (read in full; notes in `sources/NOTES.md`, section « Articles »).
- `sources/protocoles/*.qmd`: 18 local protocols (préop, craniotomie, HTIC, HSA, clippage, moya ×2, endonasal, adénome, base du crâne, DI, éveillée, cortectomie, épilepsie SSPI, dexmédétomidine, trijumeau, anévrisme mycotique, AVC thrombolyse).

Author: Jona JOACHIM.

User decisions: rewrite the protocols into teaching chapters, each ending in a "fiche pratique"; remove personal names and phone numbers but keep the local workflow; A4 with LaTeX (lualatex, installed) plus an HTML output; figures generated in the repo plus Wikimedia CC images with attribution.

## Working conventions
- **Git:** commit directly on the main branch (`master`; there is no `main`). No feature branches.
- **No em dash** (U+2014) anywhere: book content, notes, comments, commit messages, this plan. Use a colon, a semicolon, commas or parentheses instead. En dashes in numeric ranges (60–70 mmHg) are fine.
- **No more raw LaTeX than necessary.** Configure the PDF through `_quarto.yml` options (fonts, geometry, class options) and write content in Markdown/Quarto syntax that works for both PDF and HTML. There is no `preamble.tex`. Subscripts are written in Markdown (`PaCO~2~`, `CMRO~2~`, `N~2~O`), because TeX Gyre Pagella has no glyphs for Unicode subscripts (« ₂ » renders as an empty box).

**Gap:** no protocol exists for severe TBI (TC grave). That chapter is written from guidelines (SFAR 2016 TC grave, BTF 2016, SIBICC 2019) and from the extradural case in transcript 1.

## Project layout (root: `neuro_starter/`)
```
_quarto.yml            # book; lang: fr; pdf (lualatex, A4, scrbook, TeX Gyre Pagella/Heros) + html (cosmo/darkly)
                       # project.render limited to index.qmd, parties/, annexes/ (sources/ is not rendered)
index.qmd              # Avant-propos, mode d'emploi (shows every box type + fiche pratique)
parties/NN-slug.qmd    # 19 chapters, ids #sec-<slug> (e.g. #sec-htic), stubs with Objectifs / À retenir
annexes/*.qmd          # references (bibliography, before the appendices), fiches-memo, scores, abreviations, credits-images
figures/build.py       # runs figures/src/*.py → figures/*.pdf/.png
figures/src/*.py       # one matplotlib script per figure; _style.py, _diagram.py = shared helpers
figures/wikimedia/     # downloaded CC images + credits.yml
scripts/               # sfar_bib.py (SFAR @misc entries; --check), wikimedia.py (images + credits annex; --check)
sources/               # every source document lives here, never at the root; not rendered
  transcripts_cours.txt  # URLs of the 2 audio transcripts
  transcripts/         # t1_neuro_bases.txt, t2_nri.txt (downloaded cache)
  additional.txt       # Lund vs Rosner, CPPopt notes
  protocoles/          # the 18 local protocols, untouched originals
  papers/              # full-text PDFs of key articles; chandra/ = markdown conversions
  NOTES.md             # reading notes on every source: content → chapter, transcription errors, names to remove, discrepancies
references.bib         # verified via PubMed MCP (PMID + DOI fields)
vancouver.csl          # from zotero.org/styles/vancouver
styles/custom.scss     # small HTML tweaks only
_book/                 # output (git-ignored, like .quarto/ and the kept .tex)
```

**Source documents:** all input material (transcripts, protocols, notes, recommendations copied into the repo) goes in `sources/`, never at the project root. The root holds only the book itself (`_quarto.yml`, `index.qmd`, `parties/`, `annexes/`, figures, bib, styles, scripts).

## Book outline
**Partie I : Bases** (mostly from transcript 1)
1. Anatomie utile : lobes, méninges/espaces, polygone de Willis, territoires, drainage veineux, LCS (production, circulation, résorption).
2. Physiologie : DSC/CMRO₂ coupling, autoregulation (plateau, shift to the right), CO₂/O₂ reactivity, PPC = PAM − PIC, Monro-Kellie, Langfitt curve, BHE and edema types.
3. Physiopathologie : primary vs secondary injury, ACSOS, HTIC, types of herniation, Cushing reflex.
4. Pharmacologie : effects of propofol, halogenated agents, N₂O, ketamine, opioids (remifentanil), curares, dexmédétomidine (from `dexdor.qmd`), osmotherapy (SSH vs mannitol), dexaméthasone, antiepileptics, tranexamic acid.
5. Monitorage : PIC (values, waveforms), DTC (IP, Vd), EEG/BIS/PSI, PtiO₂, SvjO₂, PRx/CPPopt, NIM/PEM.

**Partie II : Bloc opératoire**
6. Consultation et préop (`preop`, `craniotomie`): neuro exam, steroids, antithrombotics, labs, bleeding risk.
7. Craniotomie programmée (`craniotomie`): brain relaxation, brain protection, agents, positioning, monitoring, PONV/pain.
8. Fosse postérieure, position assise, embolie gazeuse.
9. Chirurgie éveillée (`eveillee`).
10. Chirurgie de l'épilepsie (`cortectomie`, `epilepsie_sspi`).
11. Base du crâne et voie endonasale (`endonasal`, `adenome_micro`, `skullbase`) + diabète insipide (`diabete_insipide`).
12. Chirurgie vasculaire programmée : clippage, Moya-moya with and without bypass (`clippage_anevrysme`, `moya`, `moya_non_moya`).
13. Névralgie du trijumeau (`trijumeau`).
14. Neuroradiologie interventionnelle (transcript 2 + `anevrisme_mycotique`).

**Partie III : Urgences et réanimation**
15. HTIC aiguë (`htic`) + encadré « Lund vs Rosner, CPPopt » (`sources/additional.txt`).
16. Traumatisme crânien grave : prehospital to ICU, ACSOS targets, tiered ICP therapy (SIBICC), decompressive craniectomy (DECRA/RESCUEicp), tranexamic acid (CRASH-3), hypothermia (Eurotherm/POLAR), transfusion (TRAIN), plus the extradural hematoma case from transcript 1.
17. HSA anévrysmale (`hsa`): WFNS/Fisher, DVE, vasospasm/DCI, nimodipine.
18. AVC ischémique : thrombectomy and post-thrombolysis monitoring (`avc`).
19. Dysnatrémies (DI, SIADH, CSW) and DVE management.

**Annexes** : one-page fiches mémo (targets, doses, dilutions), scores (GCS, FOUR, WFNS, Fisher modifié, NIHSS), abréviations, image credits, bibliography.

## Pedagogical devices (consistent across chapters)
- Opening box « Objectifs » (3–5 items) and closing box « À retenir ».
- Boxes are standard Quarto callouts with a French `title`, default colors (no custom LaTeX):
  `important` = Objectifs, `caution` = À retenir, `tip` = Astuce, `warning` = Piège, `note` = Pour aller plus loin (`collapse="true"`).
- A final « Fiche pratique » for each surgical/ICU situation: a `::: {.fiche-pratique}` div holding a two-column table in a fixed order: objectifs / monitorage / induction-entretien / cibles / pièges / post-op.
- Short clinical cases with questions; answers in a collapsible block (HTML) or at the end of the chapter (PDF).
- Inline citations `[@key]`, Vancouver CSL.
- Cross-references with `@sec-…`, `@fig-…`, `@tbl-…`; Quarto adds the word (« Annexe C », « Tableau 1 »), so don't write it again in the sentence.

## Figures
- Matplotlib (`figures/src/*.py`, one script per figure, run by a `make figures` / `figures/build.py` step before render): autoregulation plateau (normal vs shifted vs lost), DSC vs PaCO₂/PaO₂, Langfitt curve, ICP waveform P1/P2/P3 (normal vs poor compliance), DTC waveforms (normal / HTIC / vasospasm), PRx-vs-CPP U-curve (CPPopt), Lund vs Rosner Starling schematic, natremia decision tree.
- Mermaid (rendered by Quarto): algorithms for tiered ICP therapy, HSA management, DI diagnosis, extradural case flow.
- Wikimedia Commons CC/PD images (circle of Willis, lobes, herniation types, meninges, ventricles). License and author are recorded in `figures/wikimedia/credits.yml`, which drives the « Crédits images » annex and the figure captions.

## Content rules
- Rewrite in clear French and fix the transcription errors (e.g., « col détachable de Guglielmi » for the transcript's "Google EMI"; "Plot" is a speaker name and gets dropped).
- Remove personal names (Dr Francine, Dr Chassoux, Dr Lévé…) and phone numbers (55148). Keep local units and workflows (USC Chippault, staff vasculaire du mardi…).
- **Protocol/guideline discrepancies:** never silently change local practice. Mark each one with a `% TODO-VALIDER` comment and collect them in `A_VALIDER.md` for the user. Already spotted:
  - Natremia target written "140–145 mmHg" (unit typo).
  - Mannitol "15-200 ml" (typo).
  - SSH: 6 g in `craniotomie` vs ~7 g in `htic`.
  - Transfusion threshold 7–8 g/dL vs TRAIN 2024 (liberal strategy favored in acute brain injury).
  - `clippage_anevrysme` contains "TODO: krenosin".
  - The full list (15 items so far, incl. the 2013 NRI transcript being outdated for stroke, hypervolemia in `hsa`, ICP threshold 15 vs 22 mmHg, vitamin K dose) is in `sources/NOTES.md` and seeds `A_VALIDER.md`.
- Every journal reference is checked with the PubMed MCP (`lookup_article_by_citation` / `get_article_metadata`) before it goes into `references.bib`. Nothing is cited from memory alone.

## Recommandations françaises (SFAR et sociétés associées)
Full-text source: `/home/jaj/devel/sfar_recommendations/output/chandra/<année>/<doc>/<doc>.md`. URLs come from `/home/jaj/devel/sfar_recommendations/output/discovery.json`. Match each document on `filename` without its extension, then cite its `landing_url`, or its `download_url` when `landing_url` is null.

Rules:
- The most recent document wins. When an older SFAR text conflicts with a newer one, or with a recent international guideline or trial, the book follows the newer source and cites the older one only as « historique ».
- Each recommendation is cited as `@misc` in `references.bib`, with author = société(s), title, year, note = RFE/RPP, url, and urldate. A small script `scripts/sfar_bib.py` builds these entries from `discovery.json` so the URLs are never typed by hand.
- Key recommendations are quoted in a « Ce que disent les recommandations » box: the wording is paraphrased faithfully and the grade is given (accord fort, G1+/G2+, avis d'experts).
- Where a local protocol departs from a recommendation, the gap is flagged in `A_VALIDER.md`.

| Doc (année, type) | Chapitre(s) | URL |
|---|---|---|
| Prise en charge neurochirurgicale des TCE de l'adulte et de l'enfant à la phase initiale (2025, RPP SFNC/ANARLF/SFAR) + fiche de synthèse | 16 TC grave, 3 | https://sfar.org/prise-en-charge-neurochirurgicales-des-traumatismes-cranio-encephaliques-de-ladulte-et-de-lenfant-a-la-phase-initiale/ |
| Prise en charge des traumatisés crâniens graves à la phase précoce (2016, RFE) | 15 HTIC, 16 TC grave | https://sfar.org/prise-en-charge-des-traumatises-craniens-graves-a-la-phase-precoce/ |
| Traumatisme crânien léger de l'adulte (2022, RPP) | 16 (encadré TC léger / HSD du sujet âgé) | https://sfar.org/prise-en-charge-des-patients-presentant-un-traumatisme-cranien-leger-de-ladulte/ |
| Traumatisme vertébromédullaire (2019, RFE) + fiche | 16 (rachis cervical du TC), annexe | https://sfar.org/prise-en-charge-des-patients-presentant-ou-a-risque-de-traumatisme-vertebromedullaire/ |
| Anesthésie pour thrombectomie (2022, RPP) | 14 NRI, 18 AVC | https://sfar.org/prise-en-charge-anesthesique-peri-procedurale-dune-revascularisation-cerebrale-par-thrombectomie/ |
| HSA grave (2004, RFE) | 17 HSA, historique only; the chapter mainly follows recent international guidelines (NCS 2023, AHA 2023, verified via PubMed) | https://sfar.org/hemorragie-sous-arachnoidienne-hsa-grave/ |
| Gestion des anticoagulants pour une procédure invasive programmée (2026, RFE GIHP) | 6 préop. INR ≤ 1,2 et vitamine K 2–5 mg la veille for intracranial neurosurgery; arrêt AOD prolongé | https://sfar.org/gestion-des-anticoagulants-pour-une-procedure-invasive-programmee/ |
| Gestion de l'anticoagulation en contexte d'urgence (2024, RFE) + algorithmes | 15, 16 (réversion immédiate en cas d'hémorragie intracrânienne) | https://sfar.org/gestion-de-lanticoagulation-dans-un-contexte-durgence/ |
| AAP, procédure programmée (2018, RFE) | 6 préop. Last dose before intracranial surgery: aspirine J-5, clopidogrel/ticagrélor J-7, prasugrel J-9 | https://sfar.org/gestion-agents-antiplaquettaires-procedure-invasive-programmee/ |
| AAP, procédure non programmée ou hémorragie (2018, RFE) | 15, 16 (transfusion plaquettaire et neurochirurgie urgente) | https://sfar.org/gestion-des-agents-antiplaquettaires-en-cas-de-procedure-invasive-non-programmee-ou-dhemorragie/ |
| Prévention de la MTEV péri-opératoire (2024, RFE GIHP) | 7, 19 (HBPM post-craniotomie) | https://sfar.org/prevention-de-la-maladie-thromboembolique-veineuse-peri-operatoire/ |
| Antibioprophylaxie en chirurgie et médecine interventionnelle (2023, v3.0 2026) | 7, 11, 14 (neurochir., endonasal, DVE) | https://sfar.org/antibioprophylaxie-en-chirurgie-et-medecine-interventionnelle/ |
| Choix du soluté de remplissage en situation critique (2021, RFE): champ « cérébrolésés » | 2, 4, 15, 16 (pas d'hypotoniques, pas d'albumine) | https://sfar.org/choix-du-solute-pour-le-remplissage-vasculaire-en-situation-critique/ |
| Contrôle ciblé de la température (2016, RFE) | 15, 16 (CCT 35–37 °C chez le TC grave) | https://sfar.org/controle-cible-de-la-temperature-en-reanimation-hors-nouveau-nes/ |
| Gestion et prévention de l'anémie en soins critiques (2019, RFE) | 16 (seuil transfusionnel; compare with TRAIN 2024 → A_VALIDER) | https://sfar.org/gestion-et-prevention-de-lanemie-hors-hemorragie-aigue-chez-le-patient-adulte-de-soins-critiques/ |
| Optimisation hémodynamique périopératoire (2024, RFE) | 7 (monitorage du débit, objectifs de PA) | https://sfar.org/optimisation-hemodynamique-perioperatoire-adulte-dont-obstetrique/ |
| Réactualisation douleur postopératoire (2016, RFE) | 7 (analgésie post-craniotomie) | https://sfar.org/reactualisation-de-la-recommandation-sur-la-douleur-postoperatoire/ |
| Curarisation et décurarisation (2018, RFE) | 4, 7 (monitorage, NIM/PEM sans curare) | https://sfar.org/curarisation-et-decurarisation-en-anesthesie/ |
| Protection oculaire (2016, RFE) | 7 (installation, procubitus) | https://sfar.org/protection-oculaire-en-anesthesie-et-reanimation/ |
| Patient diabétique en péri-opératoire (2025, fiches) | 6 (corticothérapie et hyperglycémie) | https://sfar.org/download/prise-en-charge-du-patient-diabetique-en-peri-operatoire/?wpdmdl=122568 |
| Intubation et extubation du patient de réanimation (2016, RFE) | 16 (ISR du TC grave) | https://sfar.org/intubation-et-extubation-du-patient-de-reanimation/ |
| Limitation et arrêt des traitements en soins critiques (2025, RFE) | 16 (TC dépassés, décision collégiale) | https://sfar.org/decisions-de-limitation-et-darret-de-traitements-lat-en-soins-critiques-de-ladulte/ |
| Démarches anticipées en vue de don d'organes (2024, RBP) | 16, 19 (coma grave sans perspective, Maastricht III) | https://sfar.org/wp-content/uploads/2024/10/RBP-deimarches-anticipeies_12_10_24.pdf |
| Older texts, cited as « historique » only and replaced by newer sources where these exist: monitorage EEG de la profondeur d'anesthésie (2010), NVPO (2007), états de mal épileptiques (2008), MTEV (2011, superseded by 2024) | 4, 7, 10 | URLs from `discovery.json` |

## Execution order
1. ✅ Download the transcripts to `sources/transcripts/`, then read them in full along with all the protocols. Notes in `sources/NOTES.md`.
2. ✅ Scaffold: `_quarto.yml`, `index.qmd`, CSL, stub chapters and annexes, two PubMed-verified test references (robertson1999, asgeirsson1994), clean test render (PDF + HTML).
   Findings: babel handles French with lualatex (no `babel-french.ldf` needed); always run a full `quarto render`, since rendering one format alone wipes `_book/`.
3. ✅ Build `references.bib`: run `scripts/sfar_bib.py` for the SFAR entries and verify the journal entries via PubMed. Read the relevant sections of each SFAR markdown before writing the chapter that cites it.
   Done: 30 `@misc` entries for SFAR and partner societies (keys `sfar_*`, `sfnc_*`, `sfmu_*`, `gihp_*`, `srlf_*`, `abm_*`), generated by `scripts/sfar_bib.py` into a BEGIN/END SFAR block of `references.bib`; `--check` validates every URL against `discovery.json`. The RFE/RPP label goes in the `type` field (printed « [RFE] »). 18 journal entries verified via PubMed (PMID, DOI, NLM journal abbreviation, full author list): Lund/CPPopt refs, BTF 2016, SIBICC, DECRA, RESCUEicp, CRASH-3, Eurotherm, POLAR, TRAIN, SAFE-TBI, NCS/AHA 2023 HSA, nimodipine. Further journal refs are added chapter by chapter through the same PubMed check.
   Findings: `vancouver.csl` puts its name options on `<style>`, which pandoc 3.6 ignores (names came out « C. S. Robertson », no et al.); fixed with an explicit `<name>` in the author macro. Never write `and others` in the bib (pandoc prints it literally): give the full author list and let the CSL truncate. COGiTATE is 2021 (Tas, J Neurotrauma), not 2023.
   The 4 articles in `sources/papers/` are verified via PubMed and in `references.bib` (`payen2007`, `rosner1995`, `eker1998`, `lukaszewicz2011`; 52 entries in all). Their markdown conversions (`sources/papers/chandra/`) are read in full and summarized in `sources/NOTES.md` (« Articles »: key figures, chapter mapping, what is historical and must not be taught as a current target, e.g. PPC > 70, head flat, albumin). Four primary studies they rest on were verified via PubMed and added: `chesnut1993` (hypotension/hypoxia, TCDB), `muizelaar1991` (prolonged hyperventilation RCT), `bulger2010` (prehospital hypertonic saline, negative RCT), `lescot2006` (SSH shrinks healthy tissue, not contusions); 56 entries in all.
   Findings: Payen 2007 quotes hypotension as « mortalité ×10 », the primary source (Chesnut 1993) says +150 %: cite the primary source for numbers. The `.webp` figures of the conversions are copyrighted: redraw, never reuse.
4. ✅ Generate the figures and download the Wikimedia images with their credits.
   Done: `figures/build.py` runs every `figures/src/*.py` (helpers `_style.py`, `_diagram.py`) and writes `figures/<nom>.pdf` + `.png`: `autoregulation`, `reactivite-co2-o2`, `langfitt`, `onde-pic`, `dtc`, `prx-cppopt` (simulated data), `lund-rosner`, `arbre-natremie` (DI criteria taken from the local protocol). Figures are referenced without an extension (`![...](../figures/langfitt)`): `default-image-extension` is `pdf` for the PDF format and `png` for HTML, so the PDF gets vector graphics. Generated files are committed, so a render does not require running the scripts first.
   Wikimedia: `scripts/wikimedia.py` reads `figures/wikimedia/credits.yml` (hand-written: id, Commons title, French caption), downloads a PNG rendering flattened onto white, writes author/licence/URL back into the yml and generates `annexes/_credits-wikimedia.md`, which the « Crédits des images » annex includes (`--check`, `--annex`). Images: `willis`, `lobes`, `meninges`, `ventricules` (English labels), `sinus-veineux` (Gray 488, Latin labels), `engagements` (numbered 1–6, numbers explained in the caption).
   Findings: matplotlib embeds TeX Gyre Heros as Type 3 (renders correctly; `pdf.fonttype: 42` produces a font-type mismatch with this CFF font, so it is not used). The Commons photo `Dural venous sinuses.svg` has inconsistent numbering and was replaced by Gray 488. Always look at a Wikimedia image before writing its caption. Mermaid algorithms are written with the chapters (step 5).
5. Write Partie I, then II, then III, then the annexes. Render after each part.
   In progress: Partie I is written (chapters 1–5: anatomie, physiologie, physiopathologie, pharmacologie, monitorage) and renders cleanly (PDF + HTML, no unresolved reference). Chapter 5 covers clinical exam and pupillometry, ICP (DVE vs parenchymal probe, zero, thresholds, waveform, Lundberg waves), DTC (IP/Vd, vasospasm, Lindegaard), PRx/CPPopt, PtiO~2~, SvjO~2~, NIRS, BIS/PSI and continuous EEG, PEM/PES/NIM; figures `onde-pic`, `dtc`, `prx-cppopt`. Next: Partie II, starting with chapter 6 (préop: `preop`, `craniotomie`; SFAR GIHP AOD 2026, AAP 2018, diabète 2025).
   Sources read for Partie I: transcript 1 in full, `dexdor`, `craniotomie`, `htic`, and the SFAR texts on TC grave 2016 (R1.4, R6–R10), solutés 2021 (R3.1–3.2), curares 2018 (R8.9), EEG 2010 (historique), SFNC 2025 (R8.3, R10.4, R12.3).
   17 journal refs added after a PubMed check (73 entries in all): `drummond1997`, `petersen2003`, `matta1999`, `zeiler2014`, `crash2004`, `temkin1990`, `kovarik1994`, `czosnyka1997`, `czosnyka2004`, `ract2007`, `chesnut2012` (BEST-TRIP), `okonkwo2017` (BOOST-II), `payen2023` (OXY-TC), `mokri2001`, `iliff2012`, `louveau2015`, `lindegaard1989`. Entries are built from the PubMed esummary data, never typed by hand. BOOST-3 is not in PubMed: do not cite it. Chapter 5 added `gopinath1994` (SvjO~2~), `bellner2004` (IP vs PIC), `oddo2023` (ORANGE, NPi) (76 entries in all). Sources read for chapter 5: `htic`, `preop`, `craniotomie` (monitorage sections), transcript 2 (BIS 0 / BSR 100 % during an NRI rupture), SFAR TC grave 2016 (R1.4, R6.1–R6.4, R7.1–R7.2), SFNC 2025 (R3, pupillométrie), EEG 2010 (historique).
   Conventions settled while writing: « Ce que disent les recommandations » is a `callout-note` without `collapse`; case answers sit in a `callout-note title="Réponses" collapse="true"` at the end of the case (expanded in the PDF); discrepancies are marked with an HTML comment `<!-- TODO-VALIDER : … -->` in the `.qmd`; the separator line of a pipe table sets its column widths (`|--|-----|`), needed for any table with long cells; never write « en/de la @sec-… » (Quarto inserts « Chapitre »), use « au @sec-… » or a parenthesis. Part I chapters have no fiche pratique (not a clinical situation).
   Findings: Mermaid needs Chromium for the PDF (`quarto install chromium`, not installed yet); ask the user before installing, or draw the algorithms another way. babel-french prints itemize bullets as em dashes in the PDF (a typographic label, not a character in the text); switching to standard labels would take one line of raw LaTeX (`\frenchsetup{StandardItemLabels=true}`), to be decided with the user. Pandoc reads `(@label) ` or `@label)` at the start of a line as an example-list marker: the cross-reference then prints « (1) », and since the PDF merges all chapters it breaks the same reference in every chapter. Never let a line start with a parenthesized `@sec-`/`@fig-` reference; check with `grep -nE "^\s*\(?@[A-Za-z0-9_-]+\)\s" parties/*.qmd`. The local SSH recipe (3 × 2 g in 100 mL NaCl 0,9 %) is ≈ 6,9 g NaCl, ≈ 235 mOsm, ≈ 5 % in 130 mL, not « 7 % »: the book says so.
6. Write `A_VALIDER.md`, then do a final render.

## Verification
- `quarto render` gives a clean PDF + HTML: no LaTeX errors, no `?@fig`/`???` unresolved citations or cross-references (grep the log and the `.tex`).
- Inspect sample pages of the PDF with Read (pages tool) to check figures, callouts, tables, French typography and the fiche layout.
- `grep -riE "Francine|Chassoux|LEVE|55148"` on the output returns nothing (full list of names and numbers in `sources/NOTES.md`).
- `grep -rnP "\x{2014}"` on everything except `sources/protocoles/` returns nothing.
- Every journal bib entry has a PMID/DOI that matches PubMed metadata. Every SFAR entry's URL appears verbatim in `discovery.json`, which a script checks.
- Hand `A_VALIDER.md` to the user for medical sign-off.
