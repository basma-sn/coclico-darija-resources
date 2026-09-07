# Ressources CoCLiCo-darija

Ce dépôt rassemble les ressources numériques produites dans le cadre d’un stage de Master 2 consacré à la constitution de ressources phonétiques et lexicales pour l’arabe marocain (darija), réalisé au sein du projet **CoCLiCo**.

Il comprend un corpus de parole lue, des segmentations manuelles sous Praat, deux dictionnaires de prononciation en X-SAMPA, ainsi que les scripts Python et Praat utilisés pour la constitution et l’analyse de ces ressources.

Le dépôt documente également une étude acoustique exploratoire consacrée aux effets de l’emphase sur les voyelles en arabe marocain.

## Structure du dépôt

```text
coclico-darija-resources/
├── README.md
├── .gitignore
│
├── data/
│   ├── audio/
│   ├── textgrids/
│   └── dictionaries/
│
├── scripts/
│   ├── praat/
│   │   ├── 01_extraire_occurrences_emphatiques.praat
│   │   ├── 02_extraire_occurrences_non_emphatiques.praat
│   │   └── 03_extraire_F1_F2_50pct.praat
│   │
│   └── python/
│       ├── corpus/
│       │   └── 01_compter_occurrences_phonemes.py
│       │
│       └── dictionary/
│           ├── 01_extraire_mots_texte.py
│           ├── 02_extraire_vocabulaire_sentences_doda.py
│           ├── 03_generer_dictionnaire_xsampa.py
│           ├── 04_fusionner_dictionnaires.py
│           └── 05_supprimer_doublons.py
│
└── docs/
    ├── methodologie_analyse_acoustique.md
    └── structure_csv.md
