# Ressources CoCLiCo-darija

Ce dépôt rassemble les ressources numériques produites dans le cadre d’un stage de Master 2 consacré à la constitution de ressources numériques pour l’arabe marocain (darija), réalisé au sein du projet **CoCLiCo**.

Il comprend un corpus de parole lue, des segmentations manuelles sous Praat, deux dictionnaires de prononciation en X-SAMPA, ainsi que les scripts Python et Praat utilisés pour la constitution et l’analyse de ces ressources.

Le dépôt documente également une étude acoustique exploratoire consacrée aux effets de l’emphase sur les voyelles en arabe marocain.

---

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
```

---

## Données et ressources produites

### Enregistrements audio

Le dossier `data/audio/` contient les quatre enregistrements de parole lue réalisés dans le cadre du corpus CoCLiCo-darija.

Les locuteurs sont identifiés à l’aide des codes anonymisés suivants :

- H22
- H27
- F22
- F25

Les fichiers sont fournis au format WAV.

### Segmentations manuelles

Le dossier `data/textgrids/` contient les segmentations manuelles réalisées sous Praat pour les locuteurs H22 et F22.

Les fichiers TextGrid comportent un niveau d’annotation phonémique utilisé comme matériel de référence pour le traitement automatique ainsi que pour l’étude acoustique de l’emphase présentée dans le mémoire.

### Dictionnaires de prononciation

Le dossier `data/dictionaries/` contient deux dictionnaires de prononciation en X-SAMPA :

- un dictionnaire corrigé de **2 844 entrées**, relu et corrigé manuellement ;
- un dictionnaire étendu de **43 253 entrées**, offrant une couverture lexicale plus importante mais dont la validation reste partielle.

Ces ressources ont été préparées afin de permettre leur utilisation dans **SPPAS** pour le traitement automatique de l’arabe marocain.

---

## Scripts Praat

Les scripts du dossier `scripts/praat/` servent à repérer les contextes emphatiques et non emphatiques dans le niveau d’annotation `phonemes` des fichiers TextGrid et à extraire les mesures acoustiques de F1 et F2.

Les consonnes emphatiques prises en compte dans l’étude acoustique sont `/tˤ dˤ sˤ zˤ/`, comparées à leurs contreparties non emphatiques `/t d s z/`.

La présélection repose sur l’adjacence segmentale dans le niveau phonémique. Les occurrences obtenues sont ensuite vérifiées manuellement afin de confirmer l’appartenance de la consonne et de la voyelle au même domaine syllabique.

Les mesures de F1 et F2 sont effectuées à **50 % de la durée de la voyelle** à l’aide de la méthode de Burg implémentée dans Praat. Les paramètres utilisés sont documentés dans `docs/methodologie_analyse_acoustique.md`.

---

## Scripts Python

### Corpus

Le script `scripts/python/corpus/01_compter_occurrences_phonemes.py` permet de compter les occurrences des phonèmes dans la transcription du texte utilisé pour constituer le corpus de parole lue.

### Dictionnaire de prononciation

Les scripts du dossier `scripts/python/dictionary/` correspondent aux principales étapes de préparation des dictionnaires :

1. 1. extraction du vocabulaire de la fable d'Ésope enrichie ;
2. extraction des mots arabes uniques à partir du fichier `sentences.csv` de DODa ;
3. génération de propositions de prononciation en X-SAMPA ;
4. fusion de plusieurs dictionnaires `.dict` ;
5. suppression des doublons strictement identiques tout en conservant les variantes de prononciation.

Le générateur utilise notamment la convention X-SAMPA `G` pour représenter `/ɣ/`.

---

## Documentation

Le dossier `docs/` contient des informations complémentaires concernant :

- la méthodologie de l’analyse acoustique ;
- la structure des fichiers CSV utilisés lors du traitement des données.

---

## Ressources externes utilisées

Les ressources lexicales mobilisées pour la construction du dictionnaire comprennent notamment le **Darija Open Dataset (DODa)**.

Les traitements acoustiques et les segmentations ont été réalisés avec **Praat**, tandis que les scripts de traitement de corpus et de dictionnaires ont été développés en **Python**.

---

## Logiciels et outils

- **Praat**
- **Python 3**
- **pandas**
- **SPPAS**

---

## Projet

Ce dépôt accompagne le mémoire de Master 2 :

**Construction de ressources numériques pour le traitement automatique de l’arabe marocain**

Projet **CoCLiCo**

ATILF, CNRS et Université de Lorraine

Année universitaire **2025-2026**
