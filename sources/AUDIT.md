# Journal de l'audit des citations (étape 7, non rendu)

Une ligne par affirmation vérifiée : clé, chapitre, affirmation, source consultée, verdict,
correction. Verdicts : ✓ conforme ; ✎ corrigé ; ⏳ en attente (texte intégral à obtenir).
Les constantes de physiologie de manuel (DSC 50 mL/100 g/min, 2–4 % par mmHg de PaCO~2~,
CMRO~2~ 6–7 % par °C…) ne sont pas exigées sourcées.

Textes intégraux ajoutés pendant l'audit (`sources/papers/`) :
- `btf-carney-neurosurgery2017.pdf` : BTF 2016, article *Neurosurgery* 80:6–15 (copie CNS,
  cns.org) ; braintrauma.org ne sert plus le PDF du guide complet (404).
- `sibicc-hawryluk-icm2019.pdf` : SIBICC 2019, PDF Springer en accès libre. Le palier 0
  (Fig. 1) et les paliers 1–3 (Fig. 2) sont des images : ils ne sont pas dans le texte PMC.
- `icp-czosnyka-jnnp2004.pdf` : Czosnyka et Pickard 2004, fourni par l'utilisateur.
- `autoregulation-drummond-anesthesiology1997.pdf` : lettre de Drummond 1997, fournie par
  l'utilisateur (scan ; OCR dans `papers/chandra/autoregulation-drummond-anesthesiology1997/`).

## 7.1 Partie I (chapitres 1–5) et constats déjà notés

| Clé | Ch. | Affirmation | Source lue | Verdict |
|--|--|--|--|--|
| iliff2012 | 1 | Voie paravasculaire « glymphatique », animal | Résumé | ✓ |
| louveau2015 | 1 | Lymphatiques duraux, animal | Résumé | ✓ |
| lukaszewicz2011 | 2 | 1,4 L = 1,2 L parenchyme, 100 mL sang, 100 mL LCR | Texte intégral (chandra) | ✓ |
| mokri2001 | 2 | Doctrine de Monro-Kellie | Résumé | ✓ |
| rosner1995 | 2, 5 | Capteurs PA et PIC référencés au conduit auditif externe | Texte intégral | ✓ (Rosner soignait à plat ; le livre raisonne tête à 30°) |
| drummond1997 | 2 | Limite basse « plutôt 60 à 70 mmHg » | Lettre (scan) | ✎ Drummond : moyenne d'au moins 70 mmHg chez l'adulte normotendu, variabilité énorme, estimation individuelle ≈ 25 % sous la PAM de repos. Texte réécrit |
| payen2007 | 2, 19 | 1 mOsm/L → 19,3 mmHg | Texte intégral | ✓ |
| sfar_solutes2021 | 2 | R3.1 GRADE 2− (colloïdes, albumine) ; R3.2 GRADE 2+ (isotoniques) ; hypotoniques < 280 mOsm/L à éviter | RFE 2021 | ✓ |
| myburgh2007 | 2 | Albumine : surmortalité (33,2 % contre 20,4 % à 24 mois) | Résumé | ✓ |
| asgeirsson1994, grande2006 | 2 | Lund : métoprolol, clonidine, baisse de la pression capillaire | Résumés | ✓ |
| asgeirsson1994, grande2006 | 2 | PPC acceptée jusqu'à 50 mmHg chez l'adulte | Résumés : absent | ✎ chiffre d'Eker 1998 (« 50 mm Hg for adults and 40 mm Hg for children ») : `eker1998` ajouté à la citation |
| eker1998 | 2 | Séries à contrôles historiques | Résumé et texte intégral | ✓ |
| robertson1999 | 2 | PPC > 70 : SDRA × 5, pas de bénéfice neurologique | Résumé | ✓ |
| carney2017 | 2 | PPC 60–70 mmHg | BTF 2016, niveau IIB | ✓ |
| chesnut1993 | 3 | Hypotension (PAS < 90) : + 150 % de mortalité | Résumé | ✓ |
| payen2007 | 3 | Hypocapnie < 30 mmHg chez plus de 80 % des TC graves | Texte intégral | ✓ |
| payen2007 | 3 | PaCO~2~ 35–40 mmHg | Texte intégral (rappel de la conférence ANAES 1998, grade B) | ✎ citation ajoutée au tableau |
| (aucune) | 3 | SpO~2~ > 90 % (non sourcé ; ch. 15, 16 et fiches : ≥ 95 %, non sourcé) | SIBICC Fig. 1 : « Maintain SpO2 ≥ 94% » | ✎ harmonisé à ≥ 94 % avec `hawryluk2019` (ch. 3, 15, 16, fiches mémo) |
| sfar_tcgrave2016 | 3, 16 | Glycémie : ch. 3 « 1,4–2 g/L (8–11) », ch. 16 « 1,4 à 1,8 g/L (8 à 10) » | R10.3 : 8 mM (1,4 g/L) à 10–11 mM (1,8–2 g/L), GRADE 1+ ; l'argumentaire écrit 1,4–1,8 g/L | ✎ libellé de R10.3 partout |
| (aucune) | 3 | Glycémie > 0,8 g/L (non sourcé) | R10.3, argumentaire (hypoglycémies du contrôle strict) | ✎ remplacé par « aucune hypoglycémie » sourcé |
| sfar_tcgrave2016 | 16 | « Natrémie 140–145 mmol/L » sous R10.1 | R10.1 ne donne aucun chiffre (pas d'hypernatrémie prolongée induite) ; protocole `htic` non plus | ✎ 135–145 mmol/L sans hyponatrémie (SIBICC palier 0 « Avoid hyponatremia ») et R10.1 ; idem fiches mémo |
| srlf_cct2016 | 3, 16 | Température 35–37 °C ; « R12.1–R12.3 [@srlf_cct2016] » | R12.x sont les numéros de la RFE TC 2016 ; dans la RFE CCT ce sont R2.1–R2.3 (GRADE 2+) | ✎ numéros attribués à la bonne source |
| sfar_tcgrave2016 | 3 | Seuil 20–25 mmHg ; signes scanner (citernes, > 5 mm, > 25 mL) ; osmothérapie 15–20 min (R7.3) | RFE 2016 | ✓ |
| muizelaar1991 | 3 | Hyperventilation prolongée (25 mmHg, 5 j) aggrave le devenir | Résumé (tronqué) + argumentaire R7.4 | ✎ précisé : à 3 et 6 mois, réponse motrice 4–5 ; `sfar_tcgrave2016` ajouté |
| carney2017 | 3, 5, 15 | Seuil de traitement 22 mmHg | BTF 2016, niveau IIB | ✓ |
| petersen2003 | 4 | Propofol : PIC plus basse, PPC plus haute, moins de gonflement | Résumé | ✓ |
| petersen2003 | 4 | Halogénés utilisables ≤ 1 MAC | Résumé : absent | ✎ citation déplacée ; ≤ 1 MAC appuyé par `matta1999` (sévoflurane + 4 % à 0,5 MAC) |
| matta1999 | 4 | 1,5 MAC : + 17 % (sévo) contre + 72 % (iso) | Résumé | ✓ |
| zeiler2014 | 4 | Kétamine : pas de hausse de PIC chez le patient sédaté ventilé | Résumé | ✓ |
| kovarik1994 | 4 | Succinylcholine sans effet sur la PIC chez le cérébrolésé | Résumé | ✓ |
| sfar_curares2018 | 4 | Succinylcholine contre-indiquée si déficit moteur chronique | R8.9 | ✓ |
| sfar_tcgrave2016 | 4 | Effet maximal 10–15 min, durée 2–4 h ; ≈ 250 mOsm équivalents | Argumentaire R7.3 | ✓ |
| crash2004 | 4 | 10 008 patients, surmortalité | Résumé | ✓ |
| temkin1990 | 4 | Phénytoïne : crises précoces seulement | Résumé | ✓ |
| sfnc_tce2025 | 4 | Prophylaxie : embarrure avec crise, plaie pénétrante avec délabrement | R8.3, R10.4 | ✓ |
| crash3_2019 | 4 | « Réduit les décès chez les légers à modérés, pas chez les plus graves (Glasgow 3, mydriase bilatérale) » | Résumé : critère principal non significatif (RR 0,94) ; Glasgow 3 et mydriase = analyse de sensibilité ; graves RR 0,99 | ✎ réécrit |
| protocole `dexdor` | 4 | Entretien 0,2–1 µg/kg/h (jusqu'à 1,2) | Protocole : table 0,1 à 1,2 µg/kg/h, 1 µg/kg/h pendant l'intubation vigile | ✎ ch. 4 et fiches mémo |
| protocoles `craniotomie`, `preop` | 4 | Dexaméthasone 8 mg à l'induction ; Exacyl 15 mg/kg, H4 | Protocoles | ✓ |
| oddo2023 | 5 | 514 patients, NPi < 3 anormal, associé au devenir | Résumé | ✓ |
| sfnc_tce2025 | 5 | Pupillométrie « recommandée » avant décision | R3 : avis d'experts, « idéalement évaluée par pupillométrie » ; la mydriase ne contre-indique pas seule | ✎ réécrit |
| sfar_tcgrave2016 | 5 | Tableau DVE/capteur : échec 10 %, infection 10 / 2,5 %, hémorragie 2–4 / 0–1 % | Argumentaire R6 | ✓ |
| sfar_tcgrave2016 | 5 | « Risque de mauvais devenir × 3 entre 20 et 40, × 7 au-delà » | Argumentaire R6 : RR 3 (décès ou mauvais devenir) ; > 40 : mortalité × 7 | ✎ précisé |
| chesnut2012 | 5 | BEST-TRIP, 324 patients, Bolivie et Équateur | Résumé | ✓ |
| czosnyka2004 | 5 | P1–P3, ondes de Lundberg (A : ≥ 50 mmHg, 5–20 min ; B : 0,5–2/min) | Texte intégral (`icp-czosnyka-jnnp2004.pdf`, fourni par l'utilisateur) : analyse spectrale de l'onde pulsatile (amplitude croissante avec la PIC), pas de P1–P3 ; ondes lentes de période 20 s à 3 min ; ondes en plateau quand la réserve est basse, vasodilatation maximale, PIC ensuite sous le niveau de départ ; aucun chiffre pour les ondes A | ✎ citation retirée de P1–P3 (forme classique, manuel) ; chiffres des ondes A retirés ; ondes B : 20 s à 3 min ; arrêt des ondes A par la remontée de la PAM attribué à `rosner1995` (Fig. 1, texte) |
| bellner2004 | 5 | 81 patients, PIC = 10,93 × IP − 1,28 | Résumé | ✓ |
| ract2007 | 5 | IP > 1,4, Vd < 20 cm/s ; osmothérapie et noradrénaline | Résumé ; argumentaire R1.4 (Vd < 25 cm/s d'une autre étude) | ✓ ; ✎ « avant même le scanner » absent du résumé : « dès l'admission, sans attendre le monitorage invasif » |
| sfar_tcgrave2016 | 5 | DTC GRADE 2+ (R1.4) ; abandon après dix minutes ; PtiO~2~ 15–20 mmHg et seuils de durée | RFE 2016 | ✓ |
| sfar_hsa2004 | 5, 17 | Vm 120 cm/s ; Lindegaard > 3, > 6 sévère ; + 50 cm/s/j | Texte court (grade E) et long | ✓ ; ✎ ch. 17 « ≥ 3 » → « > 3 » (3 occurrences) |
| hoh2023 | 5 | Vm 120 cm/s | Non relu ici | ✎ retiré au ch. 5 (SFAR 2004 suffit) ; à vérifier au ch. 17 en 7.5 |
| lindegaard1989 | 5, 17 | Seuils 3 et 6 | Résumé : définit l'index, pas de seuil | ✎ cité pour l'index seulement ; seuils attribués à `sfar_hsa2004` |
| czosnyka1997 | 5 | 40 moyennes de 5 s ; PRx positif « au-delà de 0,2 à 0,25 » ; mortalité | Résumé : PRx positif associé à PIC haute et mauvais devenir ; aucun seuil | ✎ seuil retiré |
| steiner2002, aries2012, tas2021 | 5 | PPCopt, devenir, COGiTATE faisable et sûr | Résumés | ✓ |
| okonkwo2017, payen2023 | 5 | BOOST-II 119 patients ; OXY-TC 318, dysfonctions 8 % contre 1 %, hématomes 4 % contre 0 | Résumés | ✓ |
| gopinath1994 | 5 | 116 patients, 90 % contre 55 % | Résumé | ✓ |
| payen2007 | 5 | SvjO~2~ « donne l'alarme avant la mydriase » | Texte : « détection précoce des épisodes d'ischémie secondaire » | ✎ réécrit |
| carney2017 | 5 | SvjO~2~ < 50 % | BTF 2016, niveau III | ✎ ajouté |
| sfar_eeg2010 | 5 | Kétamine, N~2~O ; ischémie, hypothermie, hypoglycémie ; curares ; moniteurs non interchangeables | RFE 2010 (historique) | ✓ |

## 7.2 Partie II, chapitres 6–10 (préop, craniotomie, fosse postérieure, éveillée, épilepsie)

Outils : résumés PubMed (efetch), textes SFAR chandra, texte intégral PMC d'ESETT (efetch
`db=pmc`, qui passe quand Europe PMC renvoie une erreur 500).

| Clé | Ch. | Affirmation | Source lue | Verdict |
|--|--|--|--|--|
| gihp_aod2026 | 6 | Warfarine J-6, fluindione J-5, acénocoumarol J-4, INR la veille (R3.1, 2+) ; vitamine K 2–5 mg PO si INR > 1,2 (R3.2, 2+, accord fort) ; AOD J-5 en neurochirurgie intracrânienne (R3.4, avis d'experts) ; DFG < 50 → chapitre dédié | RFE 2026 | ✓ |
| gihp_aod2026 | 6 | Risque très élevé : toute chirurgie crânienne, rachis avec ouverture durale, DVP, SEEG ; aucune neurochirurgie programmée sous anticoagulant curatif ; reprise vers J10 | RFE 2026, tableau neurochirurgie | ✓ |
| gihp_aod2026 | 6 | Pas de relais dans la FA sans antécédent embolique sous AVK (R5.2, 1−) ; relais si valve mécanique, FA avec AVC/AIT, MTEV < 3 mois (R5.3, R6.1, R7.4) ; pas de relais sous AOD dans la FA (R5.5, 2−) ; risque anaphylactique surtout IV | RFE 2026 | ✓ |
| gihp_aap2018 | 6 | Neurochirurgie intracrânienne : aspirine J-5, clopidogrel/ticagrélor J-7, prasugrel J-9 (accord fort) ; ni HBPM ni AINS en relais ; report après la bithérapie, sinon > 1 mois après stent, > 6 mois après IDM ou stent à haut risque | RFE 2018 | ✓ |
| gihp_mtev2024 | 6 | Bas de contention non retenus en thromboprophylaxie | Tableau : GRADE 1− | ✓ |
| prell2019 | 6 | 108 craniotomies, CPI peropératoire, risque d'ETEV ≈ divisé par 4 | Résumé | ✓ |
| walbert2021 | 6 | Pas de prophylaxie chez le tumoral sans crise (niveau A) ; preuves insuffisantes en péri-opératoire (niveau C) | Résumé | ✓ |
| sfar_diabete2025 | 6 | 5–10 mmol/L ; HbA1c < 3 mois, 6–8 % ; SGLT2 J-3 ; GLP-1 non arrêté (échographie gastrique, ISR) ; insuline lente jamais arrêtée chez le DT1 ; metformine sans prise le matin | Fiches 2025 | ✓ |
| sfar_curares2018 | 6 | « Aucun curare après l'induction » si NIM/PEM | RFE 2018 : neuromonitorage non traité | ✎ citation retirée ; attribué au protocole local (`craniotomie` : « Ne pas curariser après induction ») |
| sfar_hemodynamique2024 | 6, 7 | Monitorage du débit si risque élevé ; PAM ≥ 60–70 mmHg (R1.1, GRADE 2) ; hypertendu > 90 % ou > 70 mmHg (R1.2, avis d'experts) | RFE 2024 | ✓ ; ✎ ch. 6 : R2.1.1 (VES chez le patient à risque élevé, GRADE 2) précisé |
| sfar_oeil2016 | 7, 8 | Occlusion dès la perte du réflexe ciliaire (R1.2) ; gel aqueux sans conservateur pour la tête (R1.4) ; pas de pommade grasse (R1.5) ; têtière sans compression, léger proclive, limiter hypotension/anémie/hypovolémie chez l'homme obèse hypertendu (R3.1, R3.3, R3.4) | RFE 2016 | ✓ ; ✎ ch. 8 : R3.x écrites pour le rachis en ventral, appliquées par analogie (précisé) |
| sfar_atb2023 | 7 | Céfazoline 2 g, 1 g si > 4 h puis /4 h ; clindamycine 900 mg ; biopsie sans ATB ; au plus tôt 60 min avant l'incision (R1.1, GRADE 1) | RFE v3.0 2026, partie 1 | ✓ |
| sfar_solutes2021 | 7 | R3.2 isotoniques GRADE 2+ ; hypotoniques < 280 mOsm/L à éviter ; Ringer lactate : surmortalité chez le TC (HR 1,78) ; pas de position sur équilibrés vs NaCl 0,9 % | RFE 2021 | ✓ |
| petersen2003 | 7 | Sévoflurane : cerveau plus tendu que propofol à l'ouverture | Résumé | ✓ |
| prabhakar2014 | 7 | SSH : moins de cerveaux tendus (RR 0,60), preuve de faible qualité, pas de données de devenir | Résumé | ✓ |
| menegazdealmeida2024 | 7 | 16 ECR ; meilleure détente ; pas de différence sur la durée de séjour ni les déficits | Résumé | ✓ |
| gelb2008 | 7 | 275 patients, PaCO~2~ 25 vs 37, NNT 8, PIC 16,2 → 12,3 mmHg | Résumé | ✓ |
| basali2000 | 7 | 62 % vs 25 % d'HTA ≥ 160/90 dans les 12 h | Résumé | ✓ |
| guilfoyle2013 | 7 | Jusqu'aux deux tiers de douleurs modérées à sévères ; bloc du scalp : moins de douleur et d'opioïdes | Résumé | ✓ |
| sfar_douleur2016 | 7 | « Kétamine pour prévenir l'hyperalgésie au rémifentanil » | R3.8 (GRADE 1+) : chirurgie à risque de douleur intense, patient sous opioïdes au long cours ; rien sur le rémifentanil | ✎ libellé de R3.8 ; dexaméthasone 8 mg = R3.7 (GRADE 2+) |
| sfar_nvpo2007 | 7, 8 | Association d'antiémétiques chez le patient à risque élevé ; ondansétron 4 mg, dropéridol 0,625–1,25 mg | RFE 2007 (historique), grade 1+ | ✓ ; ✎ qualifié d'historique, doses du protocole local |
| gihp_mtev2024 | 7, 10 | « HBPM à H24 après craniotomie » attribué à la RFE ; ch. 10 : « après chirurgie intracrânienne, CPI et HBPM à H24 » | Pas de schéma intracrânien : anticoagulant H12–H24 en chirurgie programmée (2+) ; CPI si anticoagulant contre-indiqué (1+), associée si très haut risque (2+) ; Prell 2019 cité dans l'argumentaire | ✎ ch. 7, ch. 10, fiches mémo, `A_VALIDER.md` n° 23 et `NOTES.md` : H24 = protocole local, RFE = H12–H24 |
| (aucune) | 7 | Table des cibles : SpO~2~ ≥ 95 %, glycémie 5–10 mmol/L présentées comme protocole local | Protocole `craniotomie` : aucun chiffre | ✎ SpO~2~ ≥ 94 % (`hawryluk2019`, comme ch. 3, 15, 16) ; glycémie sourcée `sfar_diabete2025` |
| rath2007 | 8 | 260 patients ; EGV 15,2 % vs 1,4 % ; moins de saignement, plus court, nerfs crâniens bas mieux préservés, devenir comparable | Résumé | ✓ |
| himes2017 | 8 | 1792 interventions ; 1,45 % ; EGV 4,7 %, 1,06 % traitées ; sous-occipital 2,7 % | Résumé | ✓ |
| hagen1984 | 8 | FOP 27 %, plus fréquent chez le jeune | Résumé (27,3 % ; 34,3 % avant 30 ans) | ✓ |
| porter1999 | 8 | Installation progressive ; dépistage du FOP par contraste ; FOP = contre-indication ; KTC à la jonction VCS-OD | Résumé (5–10 min, pantalon pneumatique) | ✎ « en 5 à 10 minutes, pantalon pneumatique » ; remplissage et jambes surélevées présentés comme pratique |
| fathi2009 | 8 | Dépistage et fermeture discutée ; EGV 39 % (fosse postérieure), 12 % (cervical) | Résumé | ✓ |
| papadopoulos1994 | 8 | 2/17 sans FOP avec embolie paradoxale ; EGV 76 % sous ETO | Résumé | ✓ |
| ganslandt2013 | 8 | 600 patients ; ETO 25,6 % vs doppler 9,4 % ; 3,3 % de retentissement ; 0,5 % interrompues | Résumé | ✓ |
| mirski2007 | 8 | Veines non collabables ; volume létal 200–300 mL ou 3–5 mL/kg ; ordre de sensibilité des moniteurs ; KTC multiperforé ; PEP ne prévient pas et favorise l'embolie paradoxale ; conduite à tenir | Texte intégral (`air_embolism-mirski-anesthesiology2007.pdf`, fourni par l'utilisateur) : sinus duraux incompressibles ; 200–300 mL, 3–5 mL/kg ; tableau 4 (ETO 0,02 mL/kg, doppler 0,05, EtN~2~ et EtCO~2~ 0,5, SpO~2~ tardive) ; compression jugulaire, FiO~2~ 100 %, dobutamine, massage ; pointe 2 cm sous la jonction VCS-OD, aspiration 30–60 % (Bunegin-Albin) contre 6–16 % (multilumière) ; Durant et Trendelenburg discutés ; PEP : rôle « mitigé », pas de preuve au-delà de 5 cmH~2~O, embolie paradoxale possible au relâchement ; OHB : preuves limitées | ✓ ; ✎ PEP reformulée (pas de « gradient inversé ») ; rendement de l'aspiration et position de la pointe ajoutés ; Durant présenté comme discuté ; dobutamine sourcée ; OHB nuancée |
| dewitthamer2012 | 9 | > 8000 patients ; déficits sévères 3,4 % vs 8,2 % ; résection complète 75 % vs 58 % ; plus de zones éloquentes | Résumé | ✓ |
| nossek2013 | 9 | 424 patients ; échec 6,4 % (communication 4,2 %, crise 2,1 %) ; aphasie mixte ; antécédent de crises et plusieurs antiépileptiques ; langage à 3 mois ; échecs évitables | Résumé | ✓ |
| stevanovic2016 | 9 | 47 études ; échec 2 %, crises 8 %, conversion 2 % ; pas de différence SAS/MAC pour l'échec | Résumé | ✓ |
| natalini2022 | 9 | MAC : échec 1 % vs 4 %, plus court ; crises 10 % vs 4 % ; biais élevés | Résumé | ✓ |
| goettel2016 | 9 | Dexmédétomidine = propofol-rémifentanil ; événements respiratoires 0 % vs 20 % ; FC plus basse | Résumé | ✓ |
| nossek2013crises | 9 | 477 patients ; 12,6 % ; jeunes, frontal, antécédent de crises ; échec 2,3 % | Résumé | ✓ |
| boetto2015 | 9 | 3,4 % de crises, toutes partielles, arrêtées par le Ringer froid ; intensités basses (2,25 mA) | Résumé | ✓ |
| chernik1990 | 9 | Échelle OAA/S | Résumé (validation) ; items de la composante réactivité : échelle standard | ✓ |
| osborn2010, kulikov2018 | 9 | Bloc du scalp ; SAS et MAC équivalents | Résumés | ✓ |
| protocole `eveillee` | 9 | Dexmédétomidine 1 µg/kg en 20 min puis 1 µg/kg/h ; rémifentanil 1,5 ; kétamine 0,25 mg/kg et 10 mg ; lévétiracétam 500 mg ; atropine 0,25 mg ; G30 % ; dexaméthasone H12, lansoprazole 15 mg ; clobazam 5-5-10 | Protocole | ✓ (doses d'anesthésiques locaux : `TODO-VALIDER` n° 20 déjà posé) |
| wiebe2001 | 10 | 58 % vs 8 % sans crise à 1 an ; meilleure qualité de vie | Résumé | ✓ |
| kacarbayram2021 | 10 | 58 études ; rémifentanil, dexmédétomidine favorables ; propofol, halogénés contradictoires « suppression nette aux fortes concentrations » ; liste à éviter « qui suppriment ou induisent des pointes » | Résumé : titration soigneuse, « undesired effects », pas de détail dose-effet | ✎ libellés alignés sur le résumé ; alfentanil comme activateur retiré (absent du résumé) |
| chui2013 | 10 | ECoG pour délimiter et vérifier ; stimulation corticale ; activation pharmacologique | Résumé : ECoG et activation, pas la stimulation | ✎ citation déplacée sur l'ECoG |
| mullin2016 | 10 | 57 séries ; 1,3 % ; hémorragies 1,0 %, infections 0,8 % ; mortalité 0,3 % | Résumé | ✓ ; ✎ tableau des interventions : « ≈ 1 % » → 1,3 % cité |
| asconape1999 | 10 | 1/875 (0,1 %) selon le fabricant | Résumé | ✓ ; ✎ mécanisme (diffusion aux branches cardiaques) présenté comme hypothèse |
| trinka2015 | 10 | Crise tonico-clonique > 5 min = état de mal ; > 30 min, lésions durables | Texte intégral (`eme-trinka-epilepsia2015.pdf`, fourni par l'utilisateur) : t1 = 5 min (début du traitement), t2 = 30 min (risque de conséquences à long terme, dont la mort neuronale) pour l'état de mal tonico-clonique | ✓ |
| srlf_eme2008 | 10 | Clonazépam 0,015 mg/kg répété à 5 min ; crises successives sans amélioration de la conscience ; séquence rapide, pas de curare de longue durée ; propofol, midazolam, barbituriques dans l'EME réfractaire | RFE 2008 (historique) | ✓ ; ✎ « 1 mg chez l'adulte » → « environ 1 mg » (dose dérivée) |
| kapur2019 | 10 | 384 patients ; 47/45/46 % ; LEV 60 mg/kg (max 4500), fosPHT 20 mg EP/kg (max 1500), VPA 40 mg/kg (max 3000) en 10 min | Résumé + texte intégral PMC7098487 (méthodes) | ✓ |
| protocoles `cortectomie`, `epilepsie_sspi` | 10 | Rivotril 0,03–0,05 mg/kg/24 h × 72 h ; relais 2 mg/j ; cibles de la crise (SpO~2~ 95–99 %, PaCO~2~ 35–45, PAM 70–90, glycémie 1,4–1,8 g/L, Na 135–145, Ca 2,2–2,6, T 36,5–38) | Protocoles | ✓ |

Textes intégraux ajoutés en 7.2 (`sources/papers/`) : `air_embolism-mirski-anesthesiology2007.pdf`
et `eme-trinka-epilepsia2015.pdf`, fournis par l'utilisateur.

Reporté aux sous-étapes suivantes :
- 7.4 : ch. 15 « natrémie normale haute » (non chiffrée, sans source) ; BTF et SIBICC
  recommandation par recommandation (PDF désormais disponibles).
- 7.5 : `hoh2023` pour Vm 120 cm/s au ch. 17.

## 7.3 Partie II, chapitres 11–14 (base du crâne, vasculaire, trijumeau, NRI)

Outils : résumés PubMed (efetch), protocoles `endonasal`, `adenome_micro`, `skullbase`,
`diabete_insipide`, `clippage_anevrysme`, `moya`, `moya_non_moya`, `trijumeau`,
`anevrisme_mycotique`, textes SFAR chandra (antibioprophylaxie 2023 v3.0, thrombectomie 2022,
hémodynamique 2024).

| Clé | Ch. | Affirmation | Source lue | Verdict |
|--|--|--|--|--|
| nemergut2005di | 11 | 881 patients ; DI immédiat 18 %, desmopressine 12 %, persistant 2 % ; fuite de LCR 33 % ; craniopharyngiome, Rathke, microadénome, Cushing | Résumé : 18,3 % des 857 patients sans DI préopératoire | ✓ ; ✎ dénominateur précisé |
| schmitt2000 | 11 | 128 acromégales ; laryngoscopie difficile 26 %, intubation difficile 10 % ; Mallampati 3–4 prédictif mais imparfait | Résumé | ✓ |
| zwagerman2019 | 11 | DLE : fuites 21 % → 8 % après « large ouverture dure-mérienne » | Résumé : 21,2 % contre 8,2 % ; inclusion = brèche > 1 cm², large dissection arachnoïdienne ou ouverture ventriculaire/cisternale ; lambeau nasoseptal | ✎ critères d'inclusion et contexte du lambeau précisés |
| kristof2009 | 11 | 75 % de troubles hydroélectrolytiques ; DI maximal à J2 ; hyponatrémie au plus bas J9–J10 ; transitoires | Résumé | ✓ |
| nemergut2005 | 11 | Signes du Cushing ; PPC nasale proscrite (pneumocéphalie) ; pas de ventilation au masque en pression positive après l'extubation ; plaie carotidienne : pression de perfusion normale, « l'hypotension n'a plus lieu d'être » | Texte intégral (`hypophyse-nemergut-aa2005.pdf`, fourni par l'utilisateur) : HTA, diabète, peau fine, myopathie proximale, ostéoporose ✓ ; SAOS jusqu'à 70 % des acromégales, morphiniques et benzodiazépines avec prudence sous surveillance continue, canule oro- ou nasopharyngée, extubation assise ; **rien** sur la PPC, la pneumocéphalie ni la ventilation au masque ; plaie carotidienne : « deliberate hypotension may improve visualization and help to facilitate repair », tamponnement, ballonnet | ✎ piège PPC réécrit avec `risbud2023` (revue systématique vérifiée PubMed : 267 patients, aucune pneumocéphalie avec reprise précoce < 2 semaines, données limitées) ; masque présenté comme précaution sans donnée solide ; plaie carotidienne : hypotension brève possible pour la réparation, puis pression normale ; fiche et cas corrigés (213 entrées) |
| protocoles `endonasal`, `adenome_micro`, `diabete_insipide` | 11 | Risques (< 1/800, 0,5 %, 1 %, 1 %, 1,8 %, DI 12 %/2 %) ; 40–50 % sécrétants ; 1 h–1 h 30 ; vaccins, Prevenar 20, SARM ; amoxicilline-clavulanate ; installation ; PAM 60–65 ; HSHC ; critères et traitement du DI | Protocoles | ✓ ; ✎ piège « réinjection seulement si la polyurie reprend » absent du protocole (réinjection /12 h sauf Na < 135) : réécrit |
| sfar_atb2023 | 11, 12, 13, 14 | Trans-sphénoïdal : céfazoline 2 g, avis d'experts ; DVE/DLE et fuite de LCR post-traumatique sans ATB ; craniotomie GRADE 2 ; obèse R1.5.1 (GRADE 2, « probablement pas ») ; clindamycine 900 mg ; NRI et thermocoagulation sans ATB (avis d'experts) | RFE v3.0 2026, tableau neurochirurgie | ✓ |
| sfar_hemodynamique2024 | 11, 12 | R1.1, R1.2 | Vérifié en 7.2 | ✓ |
| ucas2012 | 12 | 5720 patients ; 0,95 %/an ; HR 3 (7–9 mm), 9 (10–24 mm) ; communicantes ; sac secondaire | Résumé (HR 3,35 ; 9,09) | ✓ |
| greving2014 | 12 | PHASES ; risque à 5 ans 0,25 % à > 15 % | Résumé | ✓ |
| leipzig2005 | 12 | 1694 anévrysmes ; 7,9 % / 3,8 % ; 10,7 % contre 1,2 % ; clampage temporaire 3,1 % contre 8,6 % | Résumé | ✓ |
| todd2005, hindman2010 | 12 | IHAST 1001 patients, 66 % contre 63 %, bactériémies ; 441 clampages, ni hypothermie ni thiopental/étomidate | Résumés | ✓ |
| samson1994 | 12 | « 100 clampages temporaires » ; < 14 min toléré, > 31 min infarctus ; > 61 ans, mauvais grade | Résumé : 100 patients | ✎ « 100 patients » |
| bebawy2010 | 12 | 0,3–0,4 mg/kg de poids idéal ; 45–60 s de PAS < 60 mmHg ; FA transitoire, troponine | Résumé (médiane 0,34 mg/kg, 57 s ; dose de départ « ≈ 45 s ») | ✓ ; ✎ FA et troponine étaient attribuées à `guinn2011` : citation ajoutée |
| guinn2011 | 12 | Hypotension prolongée après réinjections rapprochées, compressions thoraciques brèves | Résumé | ✓ |
| raabe2005 | 12 | Vert d'indocyanine : information significative dans 9 % des cas, surtout repositionnement du clip | Résumé | ✓ |
| fujimura2009 | 12 | 58 patients, 80 hémisphères, 27,5 % ; adulte, révélation hémorragique ; transitoire | Résumé | ✓ |
| sakamoto1997 | 12 | 368 revascularisations ; 3,8 % ; sévérité et type de chirurgie plus que l'anesthésie | Résumé | ✓ |
| scott2009 | 12 | « Bouffée de fumée » ; maladie/syndrome et affections associées ; enfant ischémique, « adulte jeune » hémorragique ; pleurs et hyperventilation | Texte intégral (`moyamoya-scott-nejm2009.pdf`, fourni par l'utilisateur) : tout y est ; pics vers 5 ans et vers 45 ans ; hémorragie 20 % des adultes contre 2,8 % des enfants | ✓ ; ✎ « adulte jeune » → pics d'âge et chiffres |
| parray2011 | 12 | Réserve épuisée : PA, hypocapnie, vol par l'hypercapnie ; hématocrite | Texte intégral (`moyamoya-parray-jna2011.pdf`, fourni par l'utilisateur) : PA au niveau de base ou au-dessus ; hypocapnie = vasoconstriction, AIT aux pleurs ; hypercapnie dilate les vaisseaux sains (moindre débit dans les territoires malades) ; anémie et polyglobulie | ✓ |
| protocoles `clippage_anevrysme`, `moya`, `moya_non_moya` | 12 | Monitorage, noradrénaline 5 µg/mL sans bolus, vert d'indocyanine 25 mg/10 mL, 3 mL × 2 ; aspirine 100 mg la veille et le matin ; NaCl 0,9 % 1 L/12 h ; cibles (PAM > 90 %, PaCO~2~ 36–40, Hb 10, glycémie 6–10) ; post-op PAM > 80, PAS < 160, urapidil, aspirine 75 mg, HBPM H24 ; complications ; hors pontage | Protocoles | ✓ ; ✎ « KTA avant l'induction si risque élevé » et conduite à tenir devant une rupture absents du protocole : étiquetés « pratique proposée », `TODO-VALIDER` et `A_VALIDER.md` n° 5 complété |
| cruccu2016 | 13 | Classique, secondaire, idiopathique | Résumé | ✓ |
| bendtsen2019 | 13 | IRM (3 séquences) ; contact « fréquent chez le sujet sain » ; CBZ/OXC ; MVD 1re intention si classique ; lésionnel si pas de conflit ou patient trop fragile ; fosphénytoïne/lidocaïne IV ; soutien psychologique | Texte intégral (`trijumeau-bendtsen-ejn2019.pdf`, fourni par l'utilisateur) : IRM forte ; contact fréquent du côté **asymptomatique** des patients (151/175 nerfs), pas chez le sujet sain ; CBZ et OXC fortes ; chirurgie si échec ou intolérance (très faible qualité) ; MVD > radiochirurgie (forte), > autres lésionnelles (faible) ; lésionnel « for those patients who cannot or prefer not to undergo MVD » ; IV en exacerbation avec réhydratation (faible) ; soutien psychologique (très faible qualité) | ✎ « côté non douloureux » ; patient fragile rendu à Bendtsen (le protocole ajoute la répétabilité) ; grades ajoutés à l'encadré |
| kanpolat2001 | 13 | 1600 patients ; 97,6 % ; 57,7 % à 5 ans ; complications (5,7 ; 0,6 ; 4,1 ; 1 ; 0,8 ; 0,8 %) ; benzodiazépines et morphiniques | Résumé | ✓ |
| barker1996 | 13 | 1185 patients ; 70 % à 10 ans ; récidives surtout les deux premières années ; décès 0,2 %, infarctus du tronc 0,1 %, surdité 1 % ; absence de soulagement immédiat = facteur de récidive | Résumé | ✓ |
| schaller1999 | 13 | 125 patients, 11 % ; FC − 38 %, PAM − 48 % ; retour à l'arrêt de la manipulation | Résumé | ✓ ; ✎ « surtout à la ponction et à la lésion » (non sourcé) reformulé comme raisonnement ; atropine 0,5 mg = dose usuelle, protocole muet (n° 31) |
| tang2026 | 13 | 517 procédures ; 59,8 % contre 29,0 % ; atropine × 4 ; « se prête mal » | Résumé : atropine 18,1 % contre 4,8 % ; les auteurs jugent la dexmédétomidine sûre et utile (épargne en propofol et midazolam) ; rien sur le délai de réveil | ✎ conclusion des auteurs ajoutée ; délai de réveil présenté comme raison du choix du service |
| loftus2010 | 13 | Kétamine 0,5 mg/kg puis 10 µg/kg/min ; moins de morphine chez le douloureux chronique dépendant des opioïdes | Résumé : chirurgie du rachis lombaire | ✓ ; ✎ contexte précisé |
| protocole `trijumeau` | 13 | Durées, installation, séquence en quatre temps, sufentanil 2,5–5 µg, pas de V1, 90 %/70 %, DL, NIM sans curare, kétamine IVSE, 4 jours | Protocole | ✓ ; ✎ fiche : « USC (Chippault) » absent du protocole, retiré ; « SpO~2~ > 94 % » non sourcé → « pas de désaturation » |
| guglielmi1991 | 14 | Spires détachables par électrolyse | Résumé (thrombose 70–100 %) | ✓ ; ✎ « les spires remplissent 70 à 90 % du sac » (non sourcé, confondait thrombose et remplissage) retiré |
| molyneux2002, goyal2016 | 14 | ISAT 23,7 % contre 30,6 % ; HERMES NNT 2,6 | Résumés | ✓ |
| (aucune) → vlak2011 | 14 | « Anévrysme chez 1 à 5 % de la population » | Vlak 2011 (méta-analyse, vérifiée PubMed) : 3,2 % (IC 1,9–5,2) sans comorbidité ; polykystose rénale PR 6,9 | ✎ `vlak2011` ajouté (212 entrées) ; « environ 3 %, sept fois plus en cas de polykystose » |
| fifi2013 | 14 | « Selon le test, 5 à 30 % de mauvais répondeurs » ; 96 stents, 36,5 % ; complications | Résumé : aspirine 5,2 %, clopidogrel 36,5 % ; VerifyNow | ✎ fourchette non sourcée remplacée par les chiffres de Fifi |
| gilard2008 | 14 | Oméprazole et clopidogrel, essai randomisé ; « atorvastatine à forte dose aussi » | Résumé : OCLA, coronariens ; rien sur les statines | ✎ statines retirées (cours de 2013, non sourcé) ; population précisée |
| cloft2002 | 14 | 4,1 % contre 0,5 % ; décès ou handicap « un tiers » | Résumé : 38 % (rompus), 29 % (non rompus) | ✎ chiffres exacts |
| abouchebl2010, schonenberger2019, chabanne2023 | 14 | Biais des séries rétrospectives ; méta-analyse : meilleur sous AG, plus d'hypotension (baisse > 20 % de la PAS) ; AMETIS sans différence | Résumés | ✓ |
| maurice2022 | 14 | GASS : pas de différence ; plus de délai ; « recanalisation plus souvent complète » | Résumé : « more often successful », 85 % contre 75 % | ✎ « réussie (85 % contre 75 %) » |
| vandersteen2022 | 14 | « Héparine à dose modérée et aspirine » : plus d'hémorragies | Résumé : HNF (dose faible ou modérée) OR 1,98 ; aspirine OR 1,95 | ✎ « à dose faible ou modérée », risque doublé |
| sfar_thrombectomie2022 | 14 | R1.1.1, R1.1.2, R1.2, R2.1, R2.2–R2.5, R3.1, R3.3, R3.4, R4.1, R4.2 ; conversion en AG associée à un moins bon pronostic | RPP 2022 (toutes avis d'experts, accord fort) ; conversion : argumentaire (SAGA) | ✓ ; ✎ R4.1 = R4.1.1 (arrêt des agents, conditions) et R4.1.2 (extubation) ; orientation : conditions de R4.3 ajoutées |
| ragulojan2019 | 14 | 499 patients ; 1/5 multiples ; > 1/3 rompus ; embolisation croissante ; anévrysme traité avant la valve dans 85 % | Résumé | ✓ |
| delgado2023 | 14 | Prise en charge collégiale (« endocarditis team ») | Texte intégral (`endocardite-delgado-ehj2023.pdf`, fourni par l'utilisateur) : centre de référence avec Endocarditis Team pour l'EI compliquée, classe I B ; tableau 13 : traitement neurochirurgical ou endovasculaire des anévrysmes volumineux, croissants ou rompus (I C) ; § 9.2 : chirurgie cardiaque possible le jour de l'embolisation contre ≈ 2 semaines après clippage, embolisation avant valve envisageable même sans rupture ; cite Ragulojan (85 %) | ✓ ; ✎ classe ajoutée, indications et délai ajoutés |
| protocole `anevrisme_mycotique` | 14 | Épidémiologie, germes, mortalité ; arrêt des bêtabloquants ; tableau des valvulopathies ; adrénaline 10 µg/mL 10–50 mL/h ; isoprénaline 20 µg/mL à 20 mL/h ; glucagon 50 µg/kg puis 1–15 mg/h ; ECMO, Arlequin ; VNI | Protocole | ✓ (n° 12 et 32 déjà posés) |

Textes intégraux ajoutés en 7.3 (`sources/papers/`, fournis par l'utilisateur) :
`trijumeau-bendtsen-ejn2019.pdf`, `endocardite-delgado-ehj2023.pdf`,
`hypophyse-nemergut-aa2005.pdf`, `moyamoya-scott-nejm2009.pdf`, `moyamoya-parray-jna2011.pdf`.
Aucun ⏳ ne reste pour les chapitres 11–14.

## 7.4 Partie III, chapitres 15–16 (HTIC, TC grave)

Outils : textes intégraux BTF 2016 (tableaux 1–3) et SIBICC 2019 (figures 1–2 lues sur
l'image des pages, tableau 1) ; textes SFAR chandra (TC grave 2016, RPP SFNC 2025, TVM 2019,
intubation 2016, anticoagulation en urgence 2024, AAP 2018, anémie 2019, CCT 2016, TC léger
2022, LAT 2025, démarches anticipées ABM 2024) ; résumés PubMed (efetch) ; protocole `htic`.

| Clé | Ch. | Affirmation | Source lue | Verdict |
|--|--|--|--|--|
| carney2017 | 15, 16 | PIC 22 mmHg ; PPC 60–70 mmHg | Texte intégral, tableau 3 : niveau IIB pour les deux ; SvjO~2~ < 50 % niveau III | ✓ ; ✎ niveau IIB ajouté (ch. 15) ; tableau des signes d'HTIC : SvjO~2~ « < 55 % » → « < 50–55 % », comme au ch. 5 |
| hawryluk2019 | 15, 16 | Palier 0 : tête 30–45°, fièvre > 38 °C, SpO~2~, PaCO~2~ normale, PPC ≥ 60, Hb et natrémie | Fig. 1 : SpO~2~ ≥ 94 %, EtCO~2~ monitorée, Hb > 7 g/dL, pas d'hyponatrémie ; **aucune cible de PaCO~2~ au palier 0** | ✎ cellule du palier 0 réécrite |
| hawryluk2019 | 15 | Paliers 1–3 ; liste « à ne pas faire » ; seuils 22 et 60 ; sauter un palier | Fig. 2 (palier 1 : PaCO~2~ 35–38 ; palier 2 : 32–35, curarisation sur essai, MAP Challenge ; palier 3 : barbituriques, hypothermie 35–36 °C, craniectomie), tableau 1, texte | ✓ ; ✎ « 35–38 mmHg » ajouté au palier 1 |
| hawryluk2019 | 15 | MAP Challenge : « monter la PAM de 10 à 15 mmHg en quelques minutes » | Fig. 2 et texte : + 10 mmHg pendant 20 min au plus, rien d'autre ne change | ✎ corrigé |
| hawryluk2019 | 15 | SIBICC « réserve [les bouffées-suppressions] aux barbituriques » | Texte et fig. 2 : barbituriques sur dose test, titrés sur la PIC ; EEG ; **ne pas augmenter la dose une fois les bouffées-suppressions obtenues** (plafond, pas cible) | ✎ réécrit ; commentaire `TODO-VALIDER` et `A_VALIDER.md` n° 34 alignés |
| hawryluk2019 | 16 | Tableau des cibles : « SpO~2~ ≥ 94 %, PaO~2~ > 60 mmHg » attribués à SIBICC | Fig. 1 : SpO~2~ seulement | ✎ PaO~2~ rendue à `@tbl-acsos` |
| sfar_tcgrave2016 | 15, 16 | R1.1 (GRADE 1+), R1.4 (2+), R1.5 (2−), R2.1 (1+), R2.2 (2+), R2.3 (1+), R3.1 (1+), R3.2 (2+), R4.1 (2+), R4.2 (2+), R5.1 (AE), R6.1 (2+), R6.2 (2−), R6.3 (2+), R6.4 (AE), R7.1 (2+), R7.2 (2+), R7.3 (1+), R7.4 (2−), R7.5 (2−), R8.1–R8.2 (AE), R8.3 (2+), R9.1 (2−), R10.1 (2−), R10.2 (1−), R10.3 (1+), R12.1–R12.3 (2+) | RFE 2016 | ✓ (numéros et grades) |
| sfar_tcgrave2016 | 15, 16 | Argumentaires : PIC 20–25 ; PPC > 90 délétère ; hyperventilation sans monitorage de l'oxygénation ; facteurs de risque de dissection ; citernes → PIC > 30 dans > 70 % ; HSA traumatique ; 21 % contre 2,5 % ; 26–74 % de PPC < 70 ; hématome secondaire 50–70 %, HTIC > 40 % ; EtCO~2~ 30–35 ; arrêt quotidien de la sédation ; gestes peu hémorragiques < 24 h | RFE 2016 | ✓ |
| sfar_tcgrave2016 | 16 | « Trois éléments (GRADE 1+, R1.1) : Glasgow, pupilles, signes de localisation » | R1.1 : Glasgow (composante motrice) et pupilles seulement | ✎ deux éléments recommandés, signes de localisation ajoutés hors recommandation |
| sfar_tcgrave2016 | 15 | Sédation « propofol ou midazolam, en évitant les bolus » | Argumentaire R5.1 : aucun agent supérieur ; bolus de midazolam, de morphiniques et barbituriques hypotenseurs | ✎ « aucun agent n'a fait la preuve de sa supériorité » ajouté |
| sfar_tcgrave2016 | 16 | Vasopresseur « noradrénaline, ou phényléphrine et éphédrine en bolus » | Argumentaire R2 : phényléphrine et/ou noradrénaline, voie périphérique au début ; pas d'éphédrine | ✎ éphédrine retirée de la phrase citée |
| sfar_tcgrave2016 | 16 | Prophylaxie antiépileptique « (facteurs de risque, plaie corticale importante) » | Argumentaire R9.1 : facteurs de risque contusion, HSDA, embarrure, fracture ; lévétiracétam préféré à la phénytoïne | ✎ liste de l'argumentaire ; « plaie corticale » relevait de SFNC R10.4 (TC pénétrant), déjà cité |
| sfar_tcgrave2016 | 16 | Craniectomie « au mieux avec les souhaits du patient » (GRADE 2+, R4.2) | R4.2 : discussion multidisciplinaire seulement | ✎ phrase scindée : souhaits hors citation |
| (aucune) | 16 | Contusions qui grossissent « dans les 24 à 72 premières heures » | Non sourcé (la RFE cite Alahmadi 2010 sans ce chiffre) | ✎ « dans les heures et les jours qui suivent » |
| (cours) | 16 | PAM 70–90 mmHg après décompression | Transcription 1 ; aucune recommandation | ✎ étiquetée « enseignement du service », `TODO-VALIDER` (n° 37, déjà posé) |
| sfnc_tce2025 | 16 | Indications HED (R6.1), HSDA (R7.1, R7.3), embarrure (R8.1), BOM (R9.1–R9.4), collégialité (R1.1, R1.2), fragilité, mydriase, délai, anticoagulant, aspirine (R2–R5), TC pénétrant (R10.4) | RPP 2025 : indications et R1–R4 avis d'experts ; R2.1, R5.1, R5.2, R6.4, R6.5 GRADE 2 | ✓ ; ✎ « ce sont des avis d'experts » limité aux indications opératoires ; GRADE 2 ajouté (R6.4–R6.5, R2.1, R5.1, R5.2) |
| sfnc_tce2025 | 16 | Embarrure : « pas d'antibiotique ni d'antiépileptique systématiques » | R8.3 : pas de prophylaxie antiépileptique primaire systématique, secondaire si crise ; rien sur l'antibiotique de l'embarrure (l'argumentaire du champ BOM rappelle : pas d'antibioprophylaxie pour une fracture de la base, SFAR 2023) | ✎ embarrure : R8.3 ; « pas d'antibioprophylaxie » déplacé sur la ligne BOM avec `sfar_atb2023` |
| sfar_tvm2019 | 16 | R1.1 (2+), R2.1 (AE), R2.2 (2+), R8.1 (2+), R5.1 (1−), R3.2 (AE, PAM > 70 une semaine) | RFE 2019 | ✓ |
| sfar_intubation2016 | 16 | R3.1 (2+), R3.2 (2+), R3.3 (1+, rocuronium 1–1,2 mg/kg, sugammadex) | RFE 2016 | ✓ |
| sfmu_anticoagurgence2024 | 15, 16 | R2.1.2 (1+), R2.3.3 (1+ ; INR > 1,2 ; CCP selon INR ou 25 UI/kg ; vitamine K 10 mg), R2.4.3 (2+, idarucizumab 5 g), R2.5.3 (AE, CCP 50 UI/kg sans délai), R2.6.2 et R2.6.6 (protamine) | RFE 2024 ; contrôle de l'INR à 30 min = R2.3.4 (2+) | ✓ ; ✎ R2.3.4 ajouté |
| gihp_aapurgence2018 | 15 | Plaquettes 0,5–0,7 × 10^11^/10 kg « sous aspirine, clopidogrel ou bithérapie » ; aspirine et Glasgow > 8 sans chirurgie ; rien dans les autres cas | RFE 2018 : dose standard pour l'aspirine ; au moins double pour clopidogrel/prasugrel ; ticagrélor < 24 h : transfusion inefficace | ✎ doses par antiagrégant |
| sfar_anemie2019 | 15, 16 | 7–10 g/dL chez le cérébrolésé ; pas de stratégie libérale > 10 g/dL | Fig. 1 (7–10, GRADE 2) ; R2.4 GRADE 2− | ✓ ; ✎ R2.4 et grade ajoutés |
| srlf_cct2016 | 15, 16 | R2.1–R2.3 : 35–37 °C, 34–35 °C si HTIC | RFE 2016 (GRADE 2+) | ✓ |
| sfmu_tcleger2022 | 16 | R2.3, R2.6.1–R2.6.3, R2.7 (avis d'experts) | RPP 2022 | ✓ |
| sfar_lat2025 | 16 | Décision collégiale, tracée, directives anticipées, proches | RFE 2025 (cadre légal rappelé) | ✓ |
| abm_demarches2024 | 16 | Démarche anticipée ; si pas de mort encéphalique, arrêt des traitements « selon la loi » et Maastricht III « peut se discuter » | RBP 2024 : LAT collégiale = prérequis ; sans mort encéphalique, arrêt des traitements selon le protocole du service jusqu'au décès ; Maastricht III relève de protocoles ABM distincts ; rien sur un M-III à la suite d'une démarche anticipée | ✎ réécrit |
| payen2007 | 16 | Hypocapnie, ACSOS la plus fréquente, « créée au transport par un ballon trop généreux » | Texte intégral : PaCO~2~ < 30 chez plus de 80 % des patients, au premier rang des ACSOS ; rien sur le ballon | ✎ chiffres de Payen ; le ballon devient un exemple non cité |
| muizelaar1991, chesnut1993, myburgh2007, crash2004, crash3_2019, temkin1990, chesnut2012, robertson1999, rosner1995, eker1998, asgeirsson1994, grande2006, steiner2002, aries2012, tas2021 | 15, 16 | Voir 7.1 ; CRASH-3 : 12 737, GCS ≤ 12 ou saignement, 18,5 % contre 19,8 %, RR 0,78 légers-modérés, 0,99 graves, occlusions vasculaires identiques ; SAFE-TBI graves 41,8 % contre 22,2 % ; CRASH 10 008 | Résumés | ✓ |
| roberts2012 | 15 | Barbituriques : PIC, pas de bénéfice, hypotension 1 sur 4 | Résumé Cochrane | ✓ |
| feldman1992 | 15 | 30° : PIC baisse sans baisse de PPC ni de DSC | Résumé (22 patients) | ✓ |
| roquilly2021 | 15 | COBI, 370 TC, NaCl 20 % ≥ 48 h, ni moins d'HTIC ni meilleur devenir | Résumé (TC modérés à graves ; HTIC 33,7 % contre 36,3 %) | ✓ |
| lescot2006 | 15 | SSH : déshydrate le tissu sain, pas la contusion | Résumé (14 patients, contusion + 5 mL) | ✓ |
| baharoglu2016 | 15 | PATCH : 190 patients, Glasgow ≥ 8, mortalité et dépendance augmentées | Résumé (OR 2,05) | ✓ |
| sprigg2018 | 15 | TICH-2 : 2325 patients, pas de bénéfice fonctionnel, moins de décès précoces | Résumé | ✓ |
| taccone2024, turgeon2024 | 15, 16 | TRAIN 850, 62,6 % contre 72,6 %, moins d'ischémie ; HEMOTION 742, 68,4 % contre 73,5 %, SDRA 3,3 % contre 0,8 % | Résumés | ✓ |
| bulger2010 | 16 | SSH préhospitalier sans bénéfice | Résumé (patients sans choc) | ✓ |
| cooper2011 | 16 | DECRA 155, bifrontale, OR 2,21, mortalité 19 % contre 18 %, séjour plus court | Résumé | ✓ |
| hutchinson2016 | 16 | RESCUEicp 408, > 25 mmHg, 26,9 % contre 48,9 %, végétatifs 8,5 % contre 2,1 % ; « barbituriques possibles » | Résumé : rien sur les barbituriques | ✓ ; ✎ « barbituriques possibles » retiré |
| hutchinson2023 | 16 | RESCUE-ASDH 450 ; 6,9 % contre 14,6 % ; 12,2 % contre 3,9 % | Résumé | ✓ |
| andrews2015, cooper2018 | 16 | Eurotherm 387, 26 % contre 37 %, arrêt ; POLAR 511, 48,8 % contre 49,1 % | Résumés | ✓ |
| ferro2017 | 15 | Anticoagulation « même en présence d'un saignement intracrânien » ; HBPM ; craniectomie recommandée ; corticoïdes et acétazolamide « non recommandés » | Texte intégral (`tvc-ferro-ejn2017.pdf`, fourni par l'utilisateur) : héparine à dose curative, « also applies to patients with an intracerebral haemorrhage at baseline » (forte, preuve modérée) ; HBPM plutôt qu'HNF sauf réversion rapide nécessaire, p. ex. neurochirurgie (faible) ; décompression si lésions parenchymateuses et engagement imminent (forte) ; corticoïdes (sauf Behçet, maladie inflammatoire) et acétazolamide déconseillés (faible) | ✓ ; ✎ « déconseillés », forces des recommandations et exceptions ajoutées |
| protocole `htic` | 15 | PIC > 15 ; IP > 1,4, Vd < 25 ; PAM 100–120 ; bouffées-suppressions ; 30–45° ; SSH ≈ 6,9 g (≈ 236 mOsm) ; mannitol 150–300 mL ; AIVOC sans halogéné, kétamine ; Hb 7–8 ; plaquettes ; acide tranexamique | Protocole | ✓ |

Texte intégral ajouté en 7.4 (`sources/papers/`, fourni par l'utilisateur) :
`tvc-ferro-ejn2017.pdf`. Aucun ⏳ ne reste pour les chapitres 15–16.

## 7.5 Partie III, chapitres 17–19 (HSA, AVC, dysnatrémies et DVE)

Textes consultés : SFAR HSA 2004 (textes court et long), protocoles `hsa`, `avc`,
`diabete_insipide`, `craniotomie` ; AHA 2026 (`prabhakaran2026`, conversion chandra : 199
recommandations extraites avec classe et niveau, tableaux 4 à 8, sections 6.1–6.5) ; ESO en
texte intégral PMC (`berge2021`, `alamowitch2023`, `vanderworp2021`, `turc2022`, `sandset2026`
dont le tableau 11 lu sur les trois images) ; RPP SFAR 2022 ; HAS 2009 (PDF has-sante.fr) ;
Spasovski 2014, Fried 2016 (PDF de `sources/papers/`) ; IDSA 2017 (PMC) ; résumés PubMed de
tous les articles.

AHA 2023 HSA (`hoh2023`) et NCS 2023 (`treggiari2023`) : d'abord bloqués (403, accès
payant, absents de PMC), puis fournis par l'utilisateur (`hsa-hoh-stroke2023.pdf`,
`hsa-treggiari-ncc2023.pdf`). Aucun ⏳ ne reste pour les chapitres 17–19.

| Clé | Ch. | Affirmation | Source lue | Verdict |
|--|--|--|--|--|
| sfar_hsa2004 | 17 | 50 ans, 60 % de femmes, HTA et tabac ; incidence 5–7/100 000 | Texte court | ✓ ; ✎ la citation couvrait l'incidence mais était placée avant : déplacée |
| sfar_hsa2004 | 17 | WFNS (tableau), grave = III–V (grade D), WFNS préférée à Hunt et Hess « plus subjective » | Texte court | ✓ ; ✎ « plus subjective » absent : « fondée sur une description clinique » |
| sfar_hsa2004 | 17 | PL sans indication si HSA au scanner ; « dangereuse » si hématome ou hydrocéphalie | Texte court : seulement « aucune indication » (grade D) ; la contre-indication est dans le protocole `hsa` | ✎ contre-indication attribuée au protocole |
| sfar_hsa2004 | 17 | Nouveau scanner à toute aggravation (D) ; centre de référence, transfert de senior à senior ; compromis PA (Cushing) ; resaignement > 70 % ; signes scanographiques d'hydrocéphalie ; DVE avant embolisation, protamine ; DVE à 15 cm du CAE ; troponine → échographie ; différer l'exclusion si défaillance, pas la DVE ; crises précoces de mauvais pronostic ; anesthésie (IV si HTIC, pas de forts bolus, immobilité, PPC, clampage bref, hypotension seulement en sauvetage) ; volet large ; évacuation d'un hématome (D) | Texte court | ✓ |
| sfar_hsa2004 | 17, 19 | Vasospasme 30–70 %, J4–J14 ; signes d'accompagnement (fièvre, HTA, leucocytose, hyponatrémie) ; DTC quotidien, Vm 120, Lindegaard > 3 et > 6, + 50 cm/s/j, ACM seule fiable ; nimodipine 360 mg/j 21 j (A), 15 j (D), IV 1–2 mg/h, hypotension corrigée ; PAM 100–120 sans infarctus ; endovasculaire d'autant plus efficace que précoce ; hyponatrémie J4–J10, perte de sel, SIADH « souvent évoquée à tort », pas de restriction, correction rapide jusqu'à 125 ; hypernatrémie : baisse < 12 mmol/L/24 h ; paracétamol, AINS à discuter | Texte court | ✓ |
| sfar_hsa2004 | 19 | Sevrage de la DVE : hors sevrage ventilatoire et vasospasme, PIC 48 h, ondes en plateau nocturnes, scanner avant retrait, anticoagulants 12 h avant et 24 h après, DVP si PIC > 20 ; prélèvement de LCR seulement sur suspicion | Texte long | ✓ |
| protocole `hsa` | 17, 19 | Mortalité ≈ 40 % (42 %), > 25 % de séquelles ; 90 % sur le complexe antérieur ; LCR rosé uniforme, xanthochromique ; bilan ; urapidil ou nicardipine ; resaignement maximal < 24 h ; hydrocéphalie 15–25 % ; DVE avant embolisation, ≥ +15 cmH~2~O, clampage aux transferts et à la toux ; OAP 10 % ; pic J8–J10 ; clippage des sylviens et des collets larges | Protocole | ✓ ; ✎ « artère cérébrale moyenne » ajoutée à la liste des sites du protocole : retirée |
| frontera2006 | 17 | 1355 patients des bras placebo de 4 essais, 33 %, OR 2,2 grade 4, Fisher original non prédictif après ajustement | Résumé | ✓ |
| post2021 | 17 | ULTRA 955, 1 g puis 1 g/8 h ≤ 24 h, resaignement 10 % contre 14 %, bon devenir 60 % contre 64 % | Résumé | ✓ |
| molyneux2002 | 17 | ISAT 23,7 % contre 30,6 % | Résumé | ✓ |
| vergouwen2010 | 17 | Définition de l'ischémie retardée | Résumé | ✓ |
| macdonald2011 | 17 | CONSCIOUS-2 1157, pas d'effet, plus d'hypotension, d'anémie, de complications pulmonaires | Résumé | ✓ |
| pickard1989 | 17 | 554, 60 mg/4 h 21 j, infarctus 22 % contre 33 %, mauvais devenir 20 % contre 33 % | Résumé | ✓ |
| dorhoutmees2012, kirkpatrick2014, wolf2023 | 17 | MASH-2 1204, RR 1,03 ; STASH 803, 40 mg ; EARLYDRAIN 287, 5 mL/h, 28,5 % contre 39,9 %, 32,6 % contre 44,8 % | Résumés | ✓ |
| gathier2018 | 17 | HIMALAIA 41, arrêté, « plus d'effets indésirables graves » | Résumé : RR 2,1 (IC 0,9–5,0) | ✎ « tendance, non significative » |
| english2025, taccone2024 | 17 | SAHaRA 742, 33,5 % contre 37,7 %, RR 0,88 ; TRAIN (7.4) | Résumé | ✓ |
| hoh2023 | 17, 19 | Classes citées : recherche d'HSA (1), PL > 6 h ou déficit (1), scanner < 6 h (2a) ; PA avant exclusion (1, C-EO), réversion des anticoagulants (1), antifibrinolytiques (3, sans bénéfice, A) ; exclusion < 24 h (1), coiling en circulation postérieure (1), évacuation d'hématome (1) ; anesthésie : mannitol ou SSH (2a), glycémie (2a), PA (2a), adénosine (2b), hypothermie (3) ; SDRA (2b) ; euvolémie (2a), minéralocorticoïdes (2a), hypervolémie (3 : Harm), MTEV après exclusion (1), glycémie (2a), CCT (2b) ; angioscanner-perfusion, DTC, EEG continu (2a), monitorage invasif (2b) ; nimodipine (1, A), euvolémie (2a), HTA induite (2b), vasodilatateur IA et angioplastie (2b), statine et magnésium (3, A), augmentation hémodynamique prophylactique (3 : Harm) ; dérivation du LCR (1), dérivation définitive (1) ; crises : EEG continu (2a), prophylaxie avec facteurs de risque (2b), sans (3), phénytoïne (3 : Harm), ≤ 7 j (2a), > 7 j (3) | PDF (`hsa-hoh-stroke2023.pdf`, fourni par l'utilisateur) | ✓ |
| hoh2023 | 17 | Texte : aucune cible de PA, PAS > 160 et méta-analyse, < 160 ou < 180, baisse progressive > 180–200, PAM ≥ 65 ; DCI ≈ 30 % et définition ; ≈ 80 % améliorés sous HTA induite ; PVC non fiable ; hydrocortisone (hyperglycémie, hypokaliémie, hémorragie digestive) ; papavérine (neurotoxicité), nimodipine IA, hypotension et PIC ; hydrocéphalie 15–87 % ; drainage lombaire et DCI ; seuil transfusionnel inconnu ; sidération myocardique, SDRA | PDF | ✓ |
| hoh2023 | 17 | Hydrocéphalie « plus souvent si HIV ou circulation postérieure » citée [@hoh2023] | Absent de l'AHA ; SFAR 2004 (facteurs prédictifs) | ✎ `sfar_hsa2004` ajouté |
| hoh2023 | 17 | DTC : Lindegaard > 3, > 6, + 50 cm/s/j attribués à l'AHA et à la SFAR | AHA : Vm ≥ 120 et Lindegaard ≥ 3 seulement | ✎ « ≥ 3 pour l'AHA » ; > 6 et + 50 cm/s attribués à la SFAR seule |
| hoh2023 | 17 | Milrinone IV dans le traitement de l'ischémie retardée | AHA : utilisée « for DCI prevention », prometteuse | ✎ « pour prévenir l'ischémie retardée » |
| treggiari2023 | 17, 19 | PA : preuves insuffisantes ; antifibrinolytiques, endothéline, statine, magnésium (forte contre) ; nimodipine orale (forte) ; nicardipine IV (forte contre) ; remplissage libéral (conditionnelle contre), euvolémie ciblée (conditionnelle) ; HTA induite, déclencheur des gestes, minéralocorticoïdes, seuil > 7 g/dL, sevrage de la DVE : preuves insuffisantes ; durée courte et gestion de l'hypotension sous nimodipine non établies | PDF (`hsa-treggiari-ncc2023.pdf`) | ✓ ; le compte du résumé (5 fortes, 1 conditionnelle) est cohérent : nimodipine et nicardipine forment une seule question PICO |
| treggiari2023 | 17 | « Preuves insuffisantes pour les inhibiteurs calciques autres que la nimodipine orale par voie IV » | Recommandation 3 : autres que la nicardipine, par voie IV ou intraventriculaire | ✎ reformulé |
| prabhakaran2026 | 18 | HERMES : significatif jusqu'à 7 h 18, chaque heure de retard | Texte | ✓ |
| prabhakaran2026 | 18 | Glycémie avant IVT (1) ; thrombolyse si déficit persistant après correction (1) ; IVT sans imagerie multimodale < 4,5 h (1) ; déficit invalidant quel que soit le NIHSS (1) ; mineur non invalidant (3) ; tableau 4 (hémianopsie, aphasie, marche) ; doses (1), ténectéplase 0,4 (3) ; biologie (2a) ; 185/110 (1) ; < 180/105 24 h (1) ; < 140 après IVT (3) ; après EVT ≤ 180/105 (2a), < 140 délétère (3 : Harm, A) ; IVT + EVT sans attendre (1) ; tableau des indications de thrombectomie (6 lignes) ; AG ou sédation (1) ; antithrombotique < 24 h (2b) ; voies aériennes (1) ; PA sans reperfusion (3, 2b, 1, baisse de 15 %) ; température (1, 3) ; glycémie (1, 2a, 3) ; tête à 0° (3) ; déglutition (1) ; MTEV (1, 2a, bas 3 : Harm) ; crises (3) ; aspirine < 48 h (1) ; anticoagulation précoce de la FA (2a), anticoagulation < 48 h (3) ; œdème : surveillance, transfert, famille (1), osmothérapie en pont (2a), hypothermie, barbituriques, corticoïdes (3 : Harm), glibenclamide (3) ; craniectomie ≤ 60 ans (1, A), > 60 ans (2b), vigilance comme déclencheur (2a), après thrombolyse (2b) ; cérébelleux : DVE (1), craniectomie ≥ 35 mL (1) | 199 recommandations extraites | ✓ |
| prabhakaran2026 | 18 | Tableaux 5 (hémorragie : arrêt, bilan, cryoprécipité pour fibrinogène ≥ 150 mg/dL, acide tranexamique 1 g en 10 min), 6 (angio-œdème), 7 (doses, surveillance /15 min, gestes différés, imagerie H24), 8 (trois groupes du tableau du livre) | Texte | ✓ |
| prabhakaran2026 | 18 | O~2~ sans bénéfice « chez le patient non hypoxémique » (classe 3) | Recommandation 4.1.5 : non hypoxémique **et non candidat à la thrombectomie** | ✎ précision ajoutée (texte et tableau) |
| prabhakaran2026 | 18 | Ténectéplase en « bolus de 5 à 10 s » | Tableau 7 : « push » ; durée absente (ni AHA ni ESO) | ✎ « bolus IV unique » |
| prabhakaran2026 | 18 | « L'aggravation se voit d'abord sur la vigilance » | Absent ; le texte dit : près de 70 % des aggravations dans les 48 premières heures ; baisse de vigilance = déclencheur raisonnable (2a) | ✎ réécrit sur ces deux données |
| berge2021 | 18 | Réveil + mismatch DWI-FLAIR, perfusion 4,5–9 h sans thrombectomie (fortes) ; > 80 ans (forte) ; AVK INR ≤ 1,7 oui, > 1,7 ou inconnu non (fortes) ; AOD < 48 h sans dosage : non (forte) ; anti-Xa < 0,5, TT < 60 s, idarucizumab (consensus 7/9, 8/9) ; PA restant > 185/110 (forte) ; crise (faible) ; pas d'antithrombotique < 24 h (forte) | Texte intégral PMC | ✓ |
| alamowitch2023 | 18 | Ténectéplase préférée si occlusion proximale (forte) ; seringue graduée pour 0,5 mg/kg | Texte intégral PMC | ✓ |
| turc2022 | 18 | IVT avant EVT même en centre de thrombectomie (forte) ; « drip-and-ship » (forte) | Texte intégral PMC | ✓ |
| sandset2026 | 18 | Aucun antihypertenseur préféré ; < 180/105 après EVT (faible) ; pas de baisse active < 140 pendant 24 h (forte, haute qualité) ; éviter les chutes de PAS (forte) ; pas d'HTA induite après TICI 3 (consensus) ; < 140 après IVT déconseillé | Tableau 11 (images) | ✓ |
| vanderworp2021 | 18 | Jusqu'à J7 au moins ; craniectomie ≤ 60 ans (forte), > 60 ans (faible), > 48 h, volet ≥ 12 cm, aphasie (consensus) ; sédation, osmothérapie en bolus, hyperventilation brève, pas de PIC systématique (consensus) ; cérébelleux 43 % contre 18–27 % | Texte intégral PMC | ✓ |
| vanderworp2021 | 18 | Infarctus malin : « plus de la moitié ou des deux tiers du territoire » | Définition ESO : au moins deux tiers | ✎ « au moins les deux tiers » |
| sfar_thrombectomie2022 | 18 | R1.1.1 (AG si NIHSS ≥ 15…), R2.1.1–R2.1.2 (130–180, 130–160), R2.2 (SpO~2~ ≥ 95 %), R2.3 (EtCO~2~ 35–40), R2.5, R3.1, R4.2 (USINV jusqu'à l'imagerie H24) : avis d'experts, accord fort | RPP 2022 | ✓ |
| sfar_thrombectomie2022 | 18 | Cas 1 : « aphasie et NIHSS ≥ 15 » justifient l'AG | R1.1.1 : l'aphasie n'est pas un critère | ✎ « NIHSS ≥ 15 (ici 17) » |
| has_avc2009 | 18 | FAST, SAMU 15 ; IRM la plus performante ; réanimation au cas par cas selon les souhaits du patient ; avis neurochirurgical pour l'infarctus cérébelleux ; CI de l'AMM 2009 (> 80 ans, > 3 h, NIHSS > 25, diabétique avec antécédent d'AVC) | RBP 2009 | ✓ |
| protocole `avc` | 18 | Altéplase 10 % + 90 % ; surveillance /30 min, /h, /2 h ; NaCl 1 L ; scope ; T et glycémie ; diurèse ; ECG ; voie dédiée ; pas de geste invasif ; nicardipine (180/105, paliers de 1 mg/h, 170–180, 160–170, < 160, 6 mg/h, appels) | Protocole | ✓ ; position « 0° > décubitus strict ou 30° » ambiguë : `TODO-VALIDER`, A_VALIDER n° 39 (i) |
| emberson2014, ninds1995, anderson2017, anderson2019, hill2003, sarraj2023, huo2023, mazighi2021, yang2022, nam2023, mistry2023, johnston2019, fischer2023, vahedi2007, juttler2014 | 18 | Tous les chiffres du chapitre (9 essais, 6756 ; 6,8 % contre 1,3 % ; 6,4 % contre 0,6 % ; HeadPoST 11 093 ; ENCHANTED 2196, 14,8 % contre 18,7 % ; 5,1 %, RR 13,6 ; SELECT2 20 % contre 7 % ; ANGEL-ASPECT 6,1 % contre 2,7 % ; tableau des essais de PA ; SHINE 1151, 2,6 % ; ELAN 0,2 % ; 29 → 78 %, 24 → 75 %, 43 % mRS ≤ 3 ; DESTINY II 38 % contre 18 %, aucun mRS 0–2) | Résumés | ✓ |
| spasovski2014 | 19 | Glycémie (1D), osmolalité urinaire (1D), ≤ 100, natriurèse 30 ; classification ; tableau 5 ; tableau du traitement (7.1.1–7.1.3, 7.2.1, 7.4.4.1 1B, 7.4.4.3, 7.1.2.4, 7.5.1) ; urée 0,25–0,50 g/kg/j (2D) ; antagonistes de la vasopressine (1C) ; perte de sel rare | PDF | ✓ |
| spasovski2014, sherlock2006 | 19 | Tableau SIADH/perte de sel : diurèse « basse » dans la SIADH | Tableau 11 : normale à basse | ✎ « normale ou basse » |
| sherlock2006, hannon2014, hannon2013, wijdicks1985, hasan1989, mori1999, chauhan2019, baek2021, bauer2011, lozier2002, zabramski2003, rao2020, chung2022, lomo2025 | 19 | 316, 57 %, 20 %, 21 % après J7, SIADH 69 %, perte de sel 6,5 % ; 100 HSA, 71 %, 8 %, 10 %, 10 %, 0 ; 78 %, DI et mortalité ; 26 restrictions, 21 infarctus ; 91, 63 → 38 % ; 30, 0,3 mg/j ; correction rapide sans surmortalité ; SALSA 178, 17 % contre 24 % ; 7 % et 0,8 % ; facteurs de risque, irrigation, pas de changement systématique ; 1,3 % contre 9,4 % ; sevrage rapide ; SEVDVE 407, 46 % contre 35 % | Résumés | ✓ |
| maggiore2009 | 19 | 130 TC, la moitié, « médiane 150 », HR 3 | Résumé : moyenne 150 | ✎ « moyenne » |
| fried2016 | 19 | Pose (cond., faible) ; coagulopathie (bonne pratique) ; MTEV (forte, faible) ; dose unique (cond., faible) ; pas d'antibiotique pendant toute la durée (forte, faible) ; cathéters imprégnés (forte, modérée) ; prélèvements (cond., faible) ; pas de changement (forte, modérée) ; bundle (forte, modérée) ; antibiotiques intraventriculaires ; sevrage rapide (bonne pratique), Klopfenstein 62,5 % contre 63,4 %, 2,8 j ; retrait dès que possible (bonne pratique) | PDF | ✓ |
| tunkel2017 | 19 | 11,4/1000 jours ; facteurs de risque ; recommandations 13–17, 23, 37 (vancomycine + bêtalactamine antipyocyanique), 55, 56 (clampage 15–60 min), 58–61 (10–14 j), 63 (retrait, forte), 69 (forte, faible), 75 (forte, modérée), 76 (forte) | Texte intégral PMC | ✓ |
| protocole `diabete_insipide` | 19 | Desmopressine « à réinjecter seulement si la polyurie reprend et si la natrémie est ≥ 135 » | Protocole : toutes les 12 h sauf si Na < 135 ; arrêt si densité > 1005 et diurèse < 150 mL/3 h (déjà corrigé au ch. 11 en 7.3) | ✎ aligné sur le protocole |
| (renvoi) | 19 | TC grave : natrémie « plutôt dans la moitié haute » | Ch. 16 (corrigé en 7.1) : 135–145 sans hyponatrémie | ✎ « sans aucune hyponatrémie » (texte et fiche) ; le ch. 15 garde « normale haute » (l. 95 et fiche), à harmoniser en 7.6 |
| protocole `craniotomie` | 19 | 140–145 si diabète insipide | Protocole (« mmHg », n° 1) | ✓ |

## 7.6 Annexes (fiches mémo, scores, abréviations) et harmonisations finales

Chaque ligne des fiches mémo a été comparée au texte corrigé du chapitre auquel elle renvoie
(valeur, source, mention « protocole local ») ; les scores à leur source.

| Clé | Ch. | Affirmation | Source lue | Verdict |
|--|--|--|--|--|
| hawryluk2019 | 15 | « Natrémie normale haute » (l. 95 et fiche pratique), non sourcé | SIBICC palier 0 : « Avoid hyponatremia » ; ch. 16 et 19 : 135–145 sans hyponatrémie | ✎ « 135–145 mmol/L sans hyponatrémie » (texte, avec `hawryluk2019`, et fiche) |
| sfar_thrombectomie2022, prabhakaran2026 | 14 | « En pratique », cas clinique 4, fiche et « À retenir » : PAS 130–160 mmHg après bonne recanalisation | RPP R2.1 : 130–160 (encadré fidèle) ; AHA 2026 : cible < 140 délétère (classe 3) ; ch. 18 : 140–160 | ✎ encadré RPP inchangé ; pratique, cas, fiche et « À retenir » alignés sur le ch. 18 (140–160, 140–180 si TICI < 2b), avec `TODO-VALIDER` (n° 39) |
| (fiches mémo) | annexe | ACSOS : PA, SpO~2~, PaCO~2~, natrémie, glycémie, température, position, Hb | Ch. 3, 15, 16, 19 corrigés | ✓ |
| (fiches mémo) | annexe | Cibles par situation : craniotomie, endonasale, moya-moya, crise en SSPI, HTIC/TC, HSA, thrombectomie, AVC | Ch. 7, 10, 11, 12, 14, 16, 17, 18 | ✓ ; ✎ « AVC après thrombectomie réussie » complété : 140–180 mmHg si TICI < 2b |
| (fiches mémo) | annexe | Seuils : PIC 5–15, 20–22, local 15 ; DTC Vm 60, IP > 1,4, Vd 20–25 ; vasospasme 120 et Lindegaard > 3 ; PtiO~2~ 25–35, 15–20 ; SvjO~2~ 55–75 ; vitesses de correction | Ch. 5, 19 | ✓ |
| (fiches mémo) | annexe | Doses cerveau et PA : SSH, mannitol, NaCl 3 %, nicardipine, nimodipine, dexmédétomidine, dexaméthasone | Ch. 4, 15, 17, 18, 19 | ✓ |
| (fiches mémo) | annexe | Hémostase : CCP, vitamine K 10 mg, INR 30 min, anti-Xa 50 UI/kg, idarucizumab, protamine, acide tranexamique, vitamine K 2–5 mg, altéplase, ténectéplase | Ch. 6, 14, 15, 18 | ✓ |
| (fiches mémo) | annexe | Crises : sérum froid, lévétiracétam 500 mg ; clonazépam 0,015 mg/kg ; deuxième ligne ; Rivotril IVSE | Ch. 9, 10 | ✓ |
| (fiches mémo) | annexe | Bloc : céfazoline, rocuronium, kétamine, atropine, vert d'indocyanine | Ch. 7, 9, 12, 16 | ✓ |
| (fiches mémo) | annexe | Desmopressine 2 µg si diurèse > 400 mL/3 h, densité < 1005, Na > 145 | Ch. 11 et protocole `diabete_insipide` : réinjection /12 h sauf Na < 135 | ✎ réinjection ajoutée |
| (fiches mémo) | annexe | Hydrocortisone : « 100 mg à l'induction si Cushing ; 50 mg × 3/j après » | Ch. 11 : Cushing 100 mg puis 20 mg × 2 puis × 3 ; HSHC 50 mg × 3/j après adénome par voie endonasale (`endonasal`) | ✎ les deux schémas séparés, « protocole local » ; ch. 11 : « schéma propre à la maladie de Cushing » (contresens) → « la maladie de Cushing a son propre schéma » |
| (fiches mémo) | annexe | Délais : arrêts préop, HBPM H24, thrombolyse < 4,5 h, thrombectomie 24 h, chirurgie < 14 j, HSA 24 h, DCI J3–J14, craniectomie, état de mal 5 min, SIADH J7–J10 | Ch. 6, 7, 10, 11, 17, 18 | ✓ ; ✎ thrombolyse : « au-delà ou heure inconnue, selon l'imagerie » ; craniectomie « avant 48 h » → « dans les 48 h, recommandée jusqu'à 60 ans, à discuter au-delà » (AHA 1 / 2b, ESO) |
| gcs_aide2015, teasdale2014 | annexe | Glasgow : cotations, NT, composantes plutôt que total | Aide à l'évaluation ; résumé | ✓ |
| wijdicks2005, iyer2009 | annexe | FOUR : quatre composantes 0–4, total 0–16 ; libellés | Libellés comparés au score publié (texte intégral non relu en 7.6) | ✓ |
| teasdale1988, sfar_hsa2004, frontera2006 | annexe | WFNS ; grave = III–V ; Fisher modifiée (définitions du protocole) | Identiques au ch. 17 (audité en 7.5) | ✓ |
| brott1989, ninds_nihss2003 | annexe | NIHSS : 15 items, 0–42, consignes et cotations | Formulaire NINDS 2003 (lu à la rédaction ; libellés recontrôlés, pas le PDF) | ✓ |
| iyer2009 | annexe | Échelle de Rankin modifiée | Iyer 2009 porte sur le score FOUR : mauvaise source | ✎ `vanswieten1988` (PubMed 3363593, vérifié ; 214 entrées) : six grades 0–5, le grade 6 (décès) ajouté par les essais ; grades 1, 2 et 4 complétés selon van Swieten (2 : « s'occupe de ses affaires sans aide ») |
| (abréviations) | annexe | Sigles utilisés dans le livre et absents de la liste | Recherche automatique dans les chapitres, fiches et scores | ✎ 34 ajouts (ARM, ASA, BNP, ECG, IA/IM/IT, OR, RR, IC 95 %, PVC, SAMU, SDRA, UNV…) ; notation J/H et R expliquée ; « PEEP » (ch. 14) → « PEP » ; « DI » (ch. 7, fiche) développé |

## Étape 10 : position assise rétrogradée (chapitre 8)

Chapitre 8 restructuré : positions latérale, trois-quarts ventrale et ventrale par défaut ; position assise dans un encadré « Pour aller plus loin », sans nouvelle donnée chiffrée. Sources nouvellement mobilisées ou relues :

| Clé | Ch. | Affirmation du livre | Ce que dit la source | Verdict |
|---|---|---|---|---|
| mirski2007 | 8 | Déclin de la position assise ; ventral et « park bench » donnent des conditions suffisantes ; proclive à risque en craniotomie et rachis ; PVC basse augmente le risque ; risque faible à modéré : EtCO~2~ et hémodynamique ; doppler précordial si site nettement surélevé ; compression jugulaire élève la PIC | Texte intégral (pdftotext) : « dramatic decline in use of the sitting position… prone or park bench provides adequate surgical conditions » ; « surgery in the head-up position places the patient at risk for VAE… craniotomy or spine » ; « increased incidence of VAE… low central venous pressure » ; encadré « Recommendation » (EtCO~2~, doppler précordial « strongly considered ») ; compression jugulaire « increase of intracranial pressure » | ✓ |
| rath2007 | 8 | 1,4 % d'embolies en position horizontale | Résumé (déjà vérifié en 7.2) | ✓ |
| porter1999 | 8 | Encadré : hypotension, quadriparésie, atteintes nerveuses périphériques ; FOP = contre-indication ; échographie de contraste | Résumé (PubMed 10325848) : « venous air embolism, quadriparesis and peripheral nerve palsies » ; macroglossie et pneumocéphalie absentes du résumé | ✎ macroglossie et pneumocéphalie laissées sans citation (non attribuées à Porter) |
