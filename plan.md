# Plan — « Starter kit » neuro-anesthésie-réanimation pour internes (Quarto book → PDF A4)

## Context
New anesthesiology interns starting in neurosurgery need a quick reference that also teaches: it should start with general physiology and then cover specific cases. It should be in French and illustrated, with references. Sources:
- `transcripts_cours.txt` → 2 audio transcripts (≈52 kB: neuro-anatomy, physiology, pathophysiology, anesthetic agents, an extradural hematoma case; ≈60 kB: interventional neuroradiology / NRI). They contain transcription errors, so they're used as a knowledge base to rewrite from, never quoted.
- `additional.txt`: Lund vs Rosner, CPPopt/PRx, key refs (Asgeirsson 1994, Grände 2006, Robertson 1999, Steiner 2002, Aries 2012, COGiTATE 2023).
- `protocoles/*.qmd`: 18 local protocols (préop, craniotomie, HTIC, HSA, clippage, moya ×2, endonasal, adénome, base du crâne, DI, éveillée, cortectomie, épilepsie SSPI, dexmédétomidine, trijumeau, anévrisme mycotique, AVC thrombolyse).

User decisions: rewrite the protocols into teaching chapters, each ending in a "fiche pratique"; remove personal names and phone numbers but keep the local workflow; A4 with LaTeX (lualatex, installed) plus an HTML output; figures generated in the repo plus Wikimedia CC images with attribution.

**Gap:** no protocol exists for severe TBI (TC grave). That chapter is written from guidelines (SFAR 2016 TC grave, BTF 2016, SIBICC 2019) and from the extradural case in transcript 1.

## Project layout (root: `neuro_starter/`)
```
_quarto.yml            # book; lang: fr; pdf (lualatex, A4, scrbook) + html
index.qmd              # Avant-propos, mode d'emploi, abréviations
parties/01-...qmd      # chapters (below)
annexes/*.qmd          # fiches, scores, doses, crédits images
figures/src/*.py       # matplotlib scripts → figures/*.pdf/.png
figures/wikimedia/     # downloaded CC images + credits.yml
sources/transcripts/   # downloaded transcripts (cache, not rendered)
references.bib         # verified via PubMed MCP
preamble.tex           # callout colors, headers, French typo (babel/polyglossia)
protocoles/            # untouched originals
```

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
15. HTIC aiguë (`htic`) + encadré « Lund vs Rosner, CPPopt » (`additional.txt`).
16. Traumatisme crânien grave : prehospital to ICU, ACSOS targets, tiered ICP therapy (SIBICC), decompressive craniectomy (DECRA/RESCUEicp), tranexamic acid (CRASH-3), hypothermia (Eurotherm/POLAR), transfusion (TRAIN), plus the extradural hematoma case from transcript 1.
17. HSA anévrysmale (`hsa`): WFNS/Fisher, DVE, vasospasm/DCI, nimodipine.
18. AVC ischémique : thrombectomy and post-thrombolysis monitoring (`avc`).
19. Dysnatrémies (DI, SIADH, CSW) and DVE management.

**Annexes** : one-page fiches mémo (targets, doses, dilutions), scores (GCS, FOUR, WFNS, Fisher modifié, NIHSS), abréviations, image credits, bibliography.

## Pedagogical devices (consistent across chapters)
- Opening box « Objectifs » (3–5 items) and closing box « À retenir ».
- Callouts: `tip` = Astuce, `warning` = Piège/Danger, `note` = Pour aller plus loin (key papers).
- A final « Fiche pratique » for each surgical/ICU situation, in a fixed layout: objectifs / monitorage / induction-entretien / cibles / pièges / post-op.
- Short clinical cases with questions; answers in a collapsible block (HTML) or at the end of the chapter (PDF).
- Inline citations `[@key]`, Vancouver CSL.

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
- Every reference is checked with the PubMed MCP (`lookup_article_by_citation` / `get_article_metadata`) before it goes into `references.bib`. Nothing is cited from memory alone.

## Execution order
1. Download the transcripts to `sources/transcripts/`, then read them in full along with all the protocols.
2. Scaffold: `_quarto.yml`, `preamble.tex`, `index.qmd`, CSL, empty chapters, a test render.
3. Build `references.bib` (verified).
4. Generate the figures and download the Wikimedia images with their credits.
5. Write Partie I, then II, then III, then the annexes. Render after each part.
6. Write `A_VALIDER.md`, then do a final render.

## Verification
- `quarto render` gives a clean PDF + HTML: no LaTeX errors, no `?@fig`/`???` unresolved citations or cross-references (grep the log and the `.tex`).
- Inspect sample pages of the PDF with Read (pages tool) to check figures, callouts, tables, French typography and the fiche layout.
- `grep -riE "Francine|Chassoux|LEVE|55148"` on the output returns nothing.
- Every bib entry has a PMID/DOI that matches PubMed metadata.
- Hand `A_VALIDER.md` to the user for medical sign-off.
