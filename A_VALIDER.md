# Points à faire valider avant diffusion

Document de travail (non rendu dans le livre). Il rassemble les écarts relevés en rédigeant le livre entre les protocoles du service (`sources/protocoles/`), les recommandations et la littérature, ainsi que les endroits où aucun protocole local n'existe et où le livre a dû proposer une conduite.

**Règle suivie pendant la rédaction :** la pratique locale n'a jamais été modifiée en silence. Quand le livre s'écarte du protocole, ou le complète, il le dit dans le texte et un commentaire `<!-- TODO-VALIDER : … (A_VALIDER n° X) -->` marque l'endroit dans le `.qmd`. Les numéros ci-dessous sont ceux de ces commentaires (et de `sources/NOTES.md`) : ne pas les renuméroter.

**Pour chaque point :** cocher une décision, compléter si besoin, puis le livre sera mis à jour et le commentaire `TODO-VALIDER` retiré. Retrouver les commentaires : `grep -rn "TODO-VALIDER" parties/`.

Types :

- **Coquille** : erreur matérielle dans un protocole (unité, chiffre, calcul) ; le livre a corrigé ou interprété.
- **Écart** : le protocole diffère d'une recommandation ou d'un essai récent ; le livre donne les deux.
- **Lacune** : le protocole ne dit rien (ou il n'y a pas de protocole) ; le livre écrit d'après la littérature.
- **Proposition** : le livre avance une valeur qui n'est ni locale ni recommandée en propre ; à accepter ou remplacer.

## Index par chapitre

| Chapitre | Fichier | Points |
|----|--------|------|
| 4 Pharmacologie | `04-pharmacologie.qmd` | 2, 3 |
| 5 Monitorage | `05-monitorage.qmd` | 6 |
| 6 Préop | `06-preop.qmd` | 8 |
| 7 Craniotomie | `07-craniotomie.qmd` | 1, 2, 3, 13, 16, 17 |
| 8 Fosse postérieure | `08-fosse-posterieure.qmd` | 18 |
| 9 Chirurgie éveillée | `09-chirurgie-eveillee.qmd` | 19, 20 |
| 10 Épilepsie | `10-epilepsie.qmd` | 16, 21, 22, 23 |
| 11 Base du crâne | `11-base-du-crane.qmd` | 24, 25, 26, 27 |
| 12 Vasculaire programmée | `12-vasculaire.qmd` | 4, 5, 28, 29, 30 |
| 13 Trijumeau | `13-trijumeau.qmd` | 31 |
| 14 NRI | `14-nri.qmd` | 12, 14, 15, 32, 33 |
| 15 HTIC | `15-htic.qmd` | 3, 4, 6, 7, 34, 35, 36 |
| 16 TC grave | `16-tc-grave.qmd` | 4, 36, 37 |
| 17 HSA | `17-hsa.qmd` | 4, 9, 10, 38 |
| 18 AVC | `18-avc.qmd` | 11, 39 |
| 19 Dysnatrémies, DVE | `19-dysnatremies-dve.qmd` | 40, 41 |

Les **fiches mémo** (annexe) reprennent des valeurs de ces chapitres et signalent les valeurs locales : toute décision ci-dessous doit aussi y être reportée.

## Points prioritaires

Ceux qui touchent directement une dose, une cible ou une indication écrite dans une fiche pratique :

- n° 4 seuil transfusionnel (quatre chapitres, quatre valeurs) ;
- n° 6 et 7 seuil d'HTIC et PAM sans PIC ;
- n° 34 objectif de bouffées-suppressions ;
- n° 36 indications de l'acide tranexamique ;
- n° 38 cible tensionnelle et nimodipine dans l'HSA ;
- n° 39 surveillance et cible tensionnelle après thrombolyse et thrombectomie, dilution de la nicardipine ;
- n° 41 antibioprophylaxie et surveillance de la DVE.

## Liste des points

### n° 1. Natrémie cible en « mmHg » (coquille)
- **Protocole** `craniotomie` : natrémie cible « 140–145 mmHg ».
- **Livre** (ch. 7) : 140–145 mmol/L.
- **Décision** : ☐ correction validée ☐ autre : ……

### n° 2. Mannitol « 15-200 ml » (coquille)
- **Protocole** `craniotomie` : « Mannitol 15-200 ml » ; `htic` : 150–300 mL.
- **Livre** (ch. 4 et 7) : lu comme 150–250 mL de mannitol 20 %.
- **Question** : quel volume écrire ?
- **Décision** : ☐ 150–250 mL ☐ autre : ……

### n° 3. Quantité de NaCl du SSH maison (coquille)
- **Protocoles** : même recette (3 ampoules de 2 g dans 100 mL de NaCl 0,9 %) décrite « NaCl 6 g » (`craniotomie`) et « env 7 g » (`htic`).
- **Livre** (ch. 4, 7, 15) : 6 g ajoutés, ≈ 6,9 g au total, ≈ 235 mOsm, ≈ 5 % dans 130 mL (et non « 7 % »).
- **Décision** : ☐ formulation du livre validée ☐ autre : ……

### n° 4. Seuil transfusionnel chez le cérébrolésé (écart, proposition)
- **Protocoles** : `htic` 7–8 g/dL ; `moya` et `moya_non_moya` 10 g/dL ; `hsa` aucun seuil.
- **Références** : RFE SFAR anémie 2019 (7–10 g/dL chez le cérébrolésé) ; TRAIN 2024 (stratégie libérale, Hb < 9 g/dL, favorable) ; HEMOTION 2024 (742 TC modérés ou graves, ≤ 10 vs ≤ 7 g/dL : devenir défavorable 68,4 % vs 73,5 %, non significatif ; SDRA 3,3 % vs 0,8 %) ; SAHaRA 2025 dans l'HSA (≤ 10 vs ≤ 8 g/dL : non significatif).
- **Livre** : ch. 15 donne 7–8 (local) et les essais ; ch. 16 propose ≈ 9 g/dL ; ch. 17 propose 8–9 g/dL ; ch. 12 garde 10 g/dL pour le moya.
- **Question** : un seuil de service par situation (HTIC, TC grave, HSA, moya) ?
- **Décision** : HTIC …… TC grave …… HSA …… Moya ……

### n° 5. Adénosine pour l'arrêt circulatoire transitoire (lacune)
- **Protocole** `clippage_anevrysme` : « TODO: krenosin », aucun protocole.
- **Livre** (ch. 12) : d'après la littérature seulement (Bebawy 2010 : 0,3–0,4 mg/kg de poids idéal ; Guinn 2011), avec un encadré « piège » signalant l'absence de protocole local.
- **Question** : l'adénosine est-elle utilisée ? Dose de départ, prérequis (palettes, rythme), qui décide ?
- **Décision** : ☐ non utilisée (retirer la section) ☐ utilisée, protocole : ……

### n° 6. Seuil d'HTIC 15 mmHg (écart)
- **Protocole** `htic` : HTIC définie par PIC > 15 mmHg.
- **Références** : SFAR 2016 20–25 mmHg ; BTF 2016 22 mmHg.
- **Livre** (ch. 5 et 15) : donne les deux.
- **Décision** : ☐ garder 15 ☐ aligner sur 20–22 ☐ autre : ……

### n° 7. « Sans PIC, PAM 100–120 mmHg » (écart)
- **Protocole** `htic` : sans monitorage de la PIC, cibler PAM 100–120 mmHg.
- **Références** : SFAR 2016 (PAS > 110 mmHg avant monitorage, PPC 60–70 mmHg) ; BTF 2016.
- **Livre** (ch. 15) : règle locale citée, encadré des recommandations, conseil de guider par le Doppler transcrânien.
- **Décision** : ☐ garder ☐ modifier : ……

### n° 8. Vitamine K avant chirurgie (écart)
- **Protocole** `craniotomie` : vitamine K 5 mg PO si INR > 1,2.
- **Référence** : RFE GIHP 2026 : 2 à 5 mg PO la veille.
- **Livre** (ch. 6) : donne les deux.
- **Décision** : ☐ garder 5 mg ☐ 2–5 mg la veille ☐ autre : ……

### n° 9. Hypervolémie après sécurisation dans l'HSA (écart)
- **Protocole** `hsa` : « respecter une hypertension artérielle, assurer une volémie adaptée grâce à un apport conséquent de solutés isotoniques ».
- **Références** : AHA 2023, NCS 2023 : euvolémie ; ni hypervolémie ni HTA prophylactique ; triple H abandonnée (SFAR 2004 cité comme historique).
- **Livre** (ch. 17) : euvolémie, HTA induite seulement en cas d'ischémie retardée.
- **Décision** : ☐ formulation du livre validée ☐ autre : ……

### n° 10. Échelle « Fisher » du protocole HSA (coquille)
- **Protocole** `hsa` : tableau intitulé « Fisher », qui est en fait l'échelle de Fisher modifiée ; PL contre-indiquée en cas d'hydrocéphalie aiguë (correct).
- **Livre** (ch. 17 et annexe Scores) : « Fisher modifiée », définitions du protocole.
- **Décision** : ☐ validé (corriger aussi le protocole) ☐ autre : ……

### n° 11. Titration de la nicardipine après thrombolyse (formulation)
- **Protocole** `avc` : titration « pour obtenir PAS 170–180 » avec arrêt si < 160 mmHg ; cible post-thrombolyse < 180/105 mmHg.
- **Livre** (ch. 18) : titration reprise telle quelle (paliers de 1 mg/h toutes les 30 min, maximum 6 mg/h), avec la cible < 180/105 mmHg pendant 24 h écrite à côté. Voir aussi n° 39 (d) pour l'usage après thrombectomie.
- **Décision** : ☐ formulation du livre validée ☐ autre : ……

### n° 12. Arrêt des bêtabloquants avant chirurgie d'anévrysme mycotique (écart)
- **Protocole** `anevrisme_mycotique` : « Faire arrêter les bêtabloquants ».
- **Problème** : risque de rebond à l'arrêt.
- **Livre** (ch. 14) : consigne locale reprise, justifiée par la régurgitation valvulaire (une bradycardie allonge la diastole), avec la mention que l'arrêt se discute.
- **Question** : pour quelles valvulopathies, avec quel délai ?
- **Décision** : ……

### n° 13. Néfopam et dropéridol (harmonisation)
- **Protocoles** : néfopam « possible si absence de risque d'épilepsie » (`craniotomie`) vs « éviction » (`epilepsie_sspi`) ; dropéridol 0,625 mg en neurochirurgie (`preop`).
- **Livre** : ch. 7 « à éviter s'il existe un risque épileptique » ; ch. 10 « ni tramadol ni néfopam ».
- **Décision** : ☐ validé ☐ éviction partout ☐ autre : ……

### n° 14. Thrombectomie : cours de 2013 dépassé (écart)
- **Source** : transcript 2 (cours de NRI de 2013) : stratégie AG vs AL et PAS 140–180 mmHg.
- **Livre** (ch. 14 et 18) : suit la RPP SFAR 2022 et les essais récents ; la stratégie de 2013 est signalée comme dépassée.
- **Décision** : ☐ validé ☐ autre : ……

### n° 15. Stratégie antiagrégante en NRI (lacune)
- **Source** : cours de 2013 (Fondation Rothschild) : test VerifyNow, clopidogrel 150 mg chez les non-répondeurs.
- **Livre** (ch. 14) : principes (non-répondeurs, test, pas de dose de charge isolée, oméprazole, prasugrel, ticagrélor) et l'exemple du cours.
- **Question** : stratégie actuelle de la NRI du service (test ? ticagrélor d'emblée ?) ?
- **Décision** : ……

### n° 16. Ringer lactate chez le cérébrolésé (écart)
- **Protocoles** : « apports balancés recommandés » sans soluté précisé (`craniotomie`) ; « Sérum physiologique/RL 1500 ml/24 h » (`epilepsie_sspi`) ; « RL + sérum physiologique » (`moya`, `moya_non_moya`, voir n° 30).
- **Référence** : RFE solutés 2021, R3.2 : le Ringer lactate est hypotonique (< 280 mOsm/L), à éviter chez le cérébrolésé.
- **Livre** (ch. 7, 10, 12) : cristalloïde équilibré isotonique (Plasmalyte, Isofundine) ou NaCl 0,9 %.
- **Décision** : ☐ validé (retirer le RL des protocoles) ☐ autre : ……

### n° 17. PAM peropératoire « 80–90 % de la PAM préopératoire » (précision)
- **Protocole** `craniotomie` : « objectif 80-90% PAM pré opératoire ».
- **Référence** : RFE hémodynamique 2024 : PAM ≥ 60–70 mmHg chez le non-hypertendu (R1.1) ; > 90 % de l'habituelle ou > 70 mmHg chez l'hypertendu chronique (R1.2).
- **Question** : plancher à 80 % ou à 90 % ?
- **Décision** : ……

### n° 18. Position assise (lacune)
- **Protocole** : aucun ; `craniotomie` cite seulement les « risques liés à la position assise d'embolie gazeuse, hypovolémie relative ».
- **Livre** (ch. 8) : écrit d'après la littérature (Porter 1999, Mirski 2007, Fathi 2009…).
- **Questions** : le service pratique-t-il la position assise ? Dépistage du FOP (ETT de contraste ou ETO) ? ETO peropératoire disponible ? Type de KTC (multiperforé, position) ?
- **Décision** : ……

### n° 19. G30 % en chirurgie éveillée (précision)
- **Protocole** `eveillee` : « Si somnolence ou ralentissement : G30 % 1 ampoule IVL dans pochon 100 ml de sérum phy », sans indication précisée.
- **Livre** (ch. 9) : contrôler la glycémie capillaire avant (patient sous dexaméthasone) et rechercher hypercapnie, crise infraclinique ou phase postcritique.
- **Question** : correction d'une hypoglycémie documentée seulement ?
- **Décision** : ……

### n° 20. Infiltration du scalp en chirurgie éveillée (lacune)
- **Protocole** `eveillee` : « protocole d'infiltration en salle (association lidocaine + ropivacaine) » sans concentrations ni volumes.
- **Livre** (ch. 9) : doses maximales usuelles (lidocaïne 4,5 mg/kg, 7 mg/kg adrénalinée ; ropivacaïne 3 mg/kg ; toxicités additives).
- **Question** : concentrations, volumes et adrénaline du protocole local ?
- **Décision** : ……

### n° 21. Algorithme « RFE/SFAR 2018 » de l'état de mal (lacune)
- **Protocole** `epilepsie_sspi` : « algorithme (RFE/SFAR 2018) » ; ce texte n'est ni dans les sources ni dans le corpus SFAR (seule la RFE SRLF 2008 y figure) ni dans PubMed.
- **Livre** (ch. 10) : ILAE 2015 (définition à 5 min), ESETT 2019 (lévétiracétam 60 mg/kg, fosphénytoïne 20 mg EP/kg, valproate 40 mg/kg), RFE 2008 historique (clonazépam 0,015 mg/kg).
- **Question** : fournir l'algorithme local pour aligner les doses.
- **Décision** : ……

### n° 22. Décroissance du Rivotril après cortectomie (coquille)
- **Protocole** `cortectomie` : relais oral à 2 mg/j puis « décroissance sur 3 semaines (0,5 mg/semaine) » : de 2 mg/j, 0,5 mg par semaine mène à l'arrêt en 4 semaines.
- **Décision** : ☐ 4 semaines à 0,5 mg/semaine ☐ 3 semaines, schéma : ……

### n° 23. Prévention de la MTEV après cortectomie (écart)
- **Protocole** `cortectomie` : « bas anti-thrombose », HBPM préventive à J2 « si aucune complication après scanner ».
- **Références** : RFE GIHP 2024 : CPI, HBPM à H24, pas de bas de contention en prévention ; le ch. 7 (craniotomie) écrit HBPM à H24.
- **Livre** (ch. 10) : donne le protocole et la RFE.
- **Décision** : ☐ aligner sur la RFE (CPI, H24) ☐ garder J2 ☐ autre : ……

### n° 24. Antibioprophylaxie en voie endonasale (écart)
- **Protocole** `endonasal` : amoxicilline-acide clavulanique (vancomycine si SARM, avis infectiologique si BLSE).
- **Référence** : RFE SFAR antibioprophylaxie 2023 (v3.0 2026), voie trans-sphénoïdale : céfazoline 2 g IVL puis 1 g toutes les 4 h (avis d'experts).
- **Livre** (ch. 11) : pratique locale dans le texte, RFE dans l'encadré.
- **Décision** : ☐ garder ☐ passer à la céfazoline ☐ autre : ……

### n° 25. Augmentin postopératoire après gros abord endonasal (écart)
- **Protocole** `skullbase` : « Augmentin postop +/- si gros endonasal ».
- **Référence** : la RFE 2023 ne prolonge pas l'antibioprophylaxie après l'intervention.
- **Question** : indication précise et durée ?
- **Décision** : ……

### n° 26. Hydrocortisone après chirurgie d'adénome (harmonisation)
- **Protocoles** : `endonasal` HSHC 50 mg × 3/j systématique même sans déficit ; `adenome_micro` seulement le schéma Cushing (100 mg à l'induction, puis 20 mg × 2 à J1, puis 20 mg × 3).
- **Référence** : revue AACE 2015 (Woodmansee) : stratégie d'épargne possible si l'axe corticotrope est normal avant l'intervention.
- **Questions** : dose d'induction hors Cushing ? Substitution systématique ou guidée par le cortisol ?
- **Décision** : ……

### n° 27. Hypotension contrôlée en voie endonasale ; proclive (précision)
- **Protocole** `endonasal` : PAM 60–65 mmHg « selon le terrain ».
- **Référence** : RFE hémodynamique 2024 : chez l'hypertendu chronique, PAM > 90 % de l'habituelle ou > 70 mmHg (R1.2).
- **Proclive** : 10–20° (`endonasal`) vs 20–30° (`adenome_micro`) ; le livre (ch. 11) écrit 10–30°.
- **Décision** : plancher chez l'hypertendu …… ; proclive ……

### n° 28. Antibioprophylaxie du moya-moya (écart, coquille probable)
- **Protocole** `moya` : céfazoline 2 g IVL (4 g si obèse) ; si allergie « LINEZOLIDE 900 mg ».
- **Référence** : RFE SFAR 2023 (v3.0 2026) : pas d'augmentation chez l'obèse sauf IMC > 50 kg/m² (R1.5.1, GRADE 2−) ; allergie : clindamycine 900 mg IV pour la craniotomie. 900 mg n'est pas une dose usuelle de linézolide (600 mg) : confusion probable avec la clindamycine.
- **Livre** (ch. 12) : « céfazoline 2 g » et la RFE dans l'encadré.
- **Décision** : ☐ aligner sur la RFE ☐ autre : ……

### n° 29. Aspirine maintenue pour le pontage de moya-moya (écart délibéré ?)
- **Protocole** `moya` : aspirine maintenue si traitement chronique, sinon introduite la veille (100 mg IVL veille et matin), 75 mg à J1.
- **Référence** : RFE GIHP 2018 : de nombreux actes de neurochirurgie intracrânienne sont non réalisables sous aspirine (arrêt J-5, ch. 6).
- **Livre** (ch. 12) : présenté comme une exception délibérée liée au pontage.
- **Décision** : ☐ décision chirurgicale systématique, confirmée ☐ autre : ……

### n° 30. Solutés et Hb dans les protocoles moya (écart)
- **Protocoles** `moya`, `moya_non_moya` : « Solutés balancés RL + sérum physiologique » (voir n° 16) ; Hb 10 g/dL (voir n° 4) ; adénosine non décrite (voir n° 5).
- **Livre** (ch. 12) : « cristalloïde isotonique (NaCl 0,9 % ou soluté balancé isotonique) ».
- **Décision** : ……

### n° 31. Sédation de la thermocoagulation du ganglion de Gasser (lacune)
- **Protocole** `trijumeau` : « sédation légère (propofol IV) » sans dose ni mode d'administration ; rien sur le réflexe trigémino-cardiaque ni sur l'atropine.
- **Livre** (ch. 13) : « bolus titrés de propofol », atropine prête, capnographie aux lunettes. L'absence d'antibioprophylaxie est conforme à la RFE 2023.
- **Questions** : dose habituelle de propofol ? Atropine préparée systématiquement ?
- **Décision** : ……

### n° 32. Isoprénaline et cible de PAM dans l'anévrysme mycotique (écart)
- **Protocole** `anevrisme_mycotique` : isoprénaline « Début vitesse 20 mL/h (dose maximale recommandée) puis baisser qsp FC » (20 µg/mL, soit ≈ 6,7 µg/min d'emblée) ; insuffisance tricuspide : « PAM 90-100 mmHg » sans justification.
- **Problème** : débuter à la dose maximale plutôt que titrer en montant est inhabituel.
- **Livre** (ch. 14) : valeurs reprises comme protocole du service. Voir aussi n° 12.
- **Décision** : ……

### n° 33. Héparine, ACT et plaquettes en NRI (lacune)
- **Source** : cours de 2013 (Fondation Rothschild), pas un protocole du service.
- **Points** : cible d'ACT (2–3 × témoin) et dose d'héparine pour l'embolisation d'anévrysme ; poursuite de l'héparine après la procédure « à la demande des neuroradiologues » ; règle « pas de transfusion plaquettaire sous stent, sauf DVE ou chirurgie urgente » ; test des antiagrégants (n° 14, 15).
- **Livre** (ch. 14) : reprend ces éléments en les attribuant au cours.
- **Décision** : ……

### n° 34. Objectif de bouffées-suppressions dans l'HTIC (écart)
- **Protocole** `htic` : « Sédation : monitorage par EEG et viser Burst Suppression ».
- **Références** : SIBICC 2019 (tableau 1) : pas de propofol à forte dose pour obtenir des bouffées-suppressions (syndrome de perfusion du propofol) ; coma barbiturique au palier 3 (dose test, EEG, pas d'augmentation une fois les bouffées-suppressions obtenues) ; Cochrane barbituriques (Roberts 2012) : pas de bénéfice sur le devenir, hypotension chez 1 patient sur 4.
- **Livre** (ch. 15) : objectif local présenté comme un dernier recours, par barbituriques.
- **Question** : quel agent, à quelle étape ?
- **Décision** : ……

### n° 35. Plaquettes sous antiagrégant sans chirurgie (écart)
- **Protocole** `htic` : pas de transfusion plaquettaire chez le patient sous AAP avec neurolésion (même hématome spontané) si pas de neurochirurgie.
- **Référence** : GIHP 2018 : pas de plaquettes sous aspirine si Glasgow > 8 sans chirurgie (PATCH) ; aucune proposition pour le coma ni pour les inhibiteurs de P2Y~12~.
- **Livre** (ch. 15) : règle du service, avec la portée exacte des recommandations.
- **Décision** : ☐ garder la règle large ☐ restreindre ☐ autre : ……

### n° 36. Indications de l'acide tranexamique (écart)
- **Protocole** `htic` : « indiqué, notamment, en cas d'hématome sous-dural ou intraparenchymateux avec ou sans chirurgie ».
- **Références** : CRASH-3 : bénéfice dans le TC léger à modéré traité dans les 3 h (pas dans le TC grave) ; TICH-2 : pas de bénéfice fonctionnel à J90 dans l'hématome spontané ; RFE anticoagulation 2024 : pas d'efficacité démontrée sous AOD (TICH-NOAC).
- **Livre** (ch. 15 et 16) : donne le protocole et les essais.
- **Question** : traumatique seulement ? Délai ?
- **Décision** : ……

### n° 37. TC grave : pas de protocole local (lacune)
- **Livre** (ch. 16) : SFAR 2016, RPP SFNC 2025, RFE TVM 2019, RFE intubation 2016, BTF 2016, SIBICC 2019 et les essais.
- **Questions** : type de capteur de PIC (DVE ou parenchymateux) ; seuil transfusionnel (n° 4) ; prophylaxie antiépileptique (lévétiracétam ?) ; délai de l'HBPM ; cible de PAM après décompression (le cours du transcript 1 dit PAM 70–90 mmHg, repris dans le chapitre).
- **Décision** : ……

### n° 38. HSA anévrysmale (écarts et lacunes)
Vérifié sur les textes intégraux AHA 2023 et NCS 2023.

- **(a) PA avant sécurisation** : `hsa` « contrôle de l'HTA » par urapidil ou nicardipine sans cible. AHA : médicaments d'action courte, éviter hypotension sévère, HTA et variabilité (classe 1, C-EO), aucune cible validée, baisse progressive si PAS > 180–200, PAM jamais < 65 ; NCS : preuves insuffisantes. Cible locale : ……
- **(b) Nimodipine** : « per os pour une durée de 21 jours » sans dose. AHA : 60 mg × 6/j entéral (classe 1, A) ; IV 1–2 mg/h (SFAR 2004, historique ; NCS : preuves insuffisantes pour l'IV). Conduite en cas d'hypotension (fractionnement 30 mg/2 h ?) : ……
- **(c) Transfusion** : pas de seuil ; le livre propose 8–9 g/dL (voir n° 4).
- **(d) Non traités par le protocole** : drain lombaire (EARLYDRAIN), prophylaxie antiépileptique (AHA : non sans facteur de risque, 2b avec, jamais de phénytoïne), acide tranexamique (AHA classe 3, NCS forte contre), HTA induite (AHA 2b, NCS preuves insuffisantes), traitement endovasculaire de l'ischémie retardée (AHA 2b), milrinone IV. Pratiques locales : ……
- **(e)** OAP « 10 % » et hydrocéphalie « 15–25 % » repris du protocole (AHA : 15–87 % pour l'hydrocéphalie). ☐ garder ☐ corriger

### n° 39. AVC ischémique : feuille post-thrombolyse (écarts et lacunes)
Vérifié sur AHA 2026, ESO 2021–2025 et RPP SFAR 2022.

- **(a) Surveillance** : `avc` /30 min pendant 2 h, /h jusqu'à H6, /2 h jusqu'à H24 ; AHA 2026 (tableau 7) : /15 min pendant et 2 h après, /30 min pendant 6 h, /h jusqu'à H24. ☐ aligner ☐ garder
- **(b) Nicardipine** : « 1 amp de 10mg/ml dans 40ml » à corriger (ampoule de 10 mg/10 mL, soit 10 mg dans 50 mL = 0,2 mg/mL, cohérent avec « 1 mg/h = 5 mL/h ») ; dose de départ non précisée : ……
- **(c)** Seuil d'appel « PAS < 85 mmHg » très bas : ……
- **(d) Après thrombectomie** : la feuille sert aussi, mais sa titration (PAS 170–180, arrêt < 160) ne correspond pas à la RPP SFAR 2022 après TICI ≥ 2b (130–160) ; AHA 2026 (classe 3, délétère) et ESO 2025 (forte) déconseillent une cible < 140 mmHg ; le livre propose 140–160 mmHg après bonne recanalisation, 140–180 sinon. Cible locale : ……
- **(e) Ténectéplase** : protocole écrit pour l'altéplase seulement ; AHA 2026 : ténectéplase 0,25 mg/kg (max 25 mg) au même niveau (classe 1) ; ESO 2023 : préférée avant thrombectomie. ☐ ajouter
- **(f)** Aucun protocole pour l'hémorragie après thrombolyse (AHA : cryoprécipité pour fibrinogène ≥ 1,5 g/L, acide tranexamique 1 g ; produit local : concentré de fibrinogène ?) ni pour l'angio-œdème : ……
- **(g)** Rien sur l'imagerie de H24 avant les antithrombotiques, le test de déglutition, la prévention de la MTEV : ……
- **(h)** Aucun protocole pour l'infarctus sylvien malin : ……

### n° 40. Dysnatrémies (lacune, proposition)
- **(a) NaCl 3 %** : le guide européen (Spasovski 2014) recommande des poches prêtes de 150 mL ; la recette de SSH de l'HTIC (≈ 6,9 g NaCl) n'est pas équivalente (150 mL de NaCl 3 % = 4,5 g). Disponibilité locale ou recette validée par la pharmacie : ……
- **(b) Restriction hydrique** : le livre (ch. 19) propose de ne pas restreindre les apports à la phase aiguë d'une lésion cérébrale, même devant une SIADH, et de traiter par le sel ; le guide européen propose la restriction en première ligne de la SIADH en population générale (2D). ☐ proposition validée ☐ autre : ……

### n° 41. DVE (lacune)
Aucun protocole local hors `hsa` (+15 cmH~2~O, clampage pour les transferts et la toux) ; pas de recommandation SFAR sur la DVE.

- **(a) Antibioprophylaxie à la pose** : SFAR 2023 aucune (avis d'experts) ; NCS 2016 dose unique (conditionnelle) ; IDSA 2017 recommandée (forte). Cathéters imprégnés utilisés (NCS : forte) ? ……
- **(b) Surveillance infirmière** : hauteur par défaut hors HSA ; seuils de débit horaire et journalier qui déclenchent un appel ; fréquence de mesure de la PIC ; conduite en cas de débit nul : ……
- **(c) Sevrage** : progressif ou clampage direct, seuil de PIC de réouverture, scanner avant retrait ; délai entre HBPM et retrait : ……

## Choix de mise en forme à trancher

Ces points ne sont pas médicaux mais demandent une décision de l'auteur :

1. **Coupures de ligne avant « : », « ; » et « % » dans le PDF** (par exemple « ≥ 95 » en fin de ligne et « % » au début de la suivante) : babel-french ne rend pas insécable l'espace avant la ponctuation haute ici. Correction globale (espace insécable dans les sources, ou option de babel) : ☐ oui ☐ laisser.
2. **Puces des listes en tirets cadratins dans le PDF** (étiquette typographique de babel-french, pas un caractère du texte) : passer aux puces standard demande une ligne de LaTeX (`\frenchsetup{StandardItemLabels=true}`). ☐ puces standard ☐ garder les tirets.
3. **Algorithmes Mermaid** : le PDF demande Chromium (`quarto install chromium`, non installé). Sans lui, les algorithmes sont des tableaux ou des figures Matplotlib. ☐ installer Chromium ☐ garder tableaux et figures.
