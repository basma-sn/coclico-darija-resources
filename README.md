# CoCLiCo Darija Resources

Ce dépôt rassemble les scripts développés dans le cadre d'un stage de Master 2 consacré à la constitution de ressources phonétiques et lexicales pour l'arabe marocain (darija) au sein du projet **CoCLiCo**, ainsi que les scripts associés à une étude acoustique exploratoire de l'emphase.

Cette version du dépôt est destinée principalement à documenter les méthodes et les traitements présentés dans le mémoire.

## Structure

```text
coclico-darija-resources/
├── README.md
├── .gitignore
├── scripts/
│   ├── praat/
│   │   ├── 01_extraire_occurrences_emphatiques.praat
│   │   ├── 02_extraire_occurrences_non_emphatiques.praat
│   │   └── 03_extraire_F1_F2_50pct.praat
│   └── python/
│       ├── corpus/
│       │   └── 01_compter_occurrences_phonemes.py
│       └── dictionary/
│           ├── 01_extraire_mots_texte.py
│           ├── 02_extraire_vocabulaire_sentences_doda.py
│           ├── 03_generer_dictionnaire_xsampa.py
│           ├── 04_fusionner_dictionnaires.py
│           └── 05_supprimer_doublons.py
└── docs/
    ├── methodologie_analyse_acoustique.md
    └── structure_csv.md
```

## Scripts Praat

Les scripts Praat servent à repérer les contextes emphatiques et non emphatiques dans le tier `phonemes` des TextGrid et à extraire les mesures de F1 et F2 au milieu temporel des voyelles retenues.

Les consonnes emphatiques prises en compte sont `/tˤ dˤ sˤ zˤ rˤ lˤ/`, avec `/t d s z r l/` comme contreparties non emphatiques.

La présélection repose sur l'adjacence segmentale dans le tier phonémique. Les occurrences sont ensuite vérifiées manuellement pour confirmer l'appartenance de la consonne et de la voyelle au même domaine syllabique.

Pour l'extraction acoustique, les mesures sont prises à 50 % de la durée vocalique avec la méthode de Burg. Les paramètres utilisés dans l'étude sont documentés dans `docs/methodologie_analyse_acoustique.md`.

## Scripts Python

### Corpus

`01_compter_occurrences_phonemes.py` compte les occurrences des phonèmes dans la transcription phonémique du texte utilisé pour le corpus.

### Dictionnaire de prononciation

Les scripts du dossier `scripts/python/dictionary/` correspondent aux principales étapes de préparation du dictionnaire :

1. extraction du vocabulaire du texte CoCLiCo ;
2. extraction des mots arabes uniques à partir du fichier `sentences.csv` de DODa ;
3. génération de prononciations en X-SAMPA ;
4. fusion de plusieurs dictionnaires `.dict` ;
5. suppression des doublons stricts tout en conservant les variantes de prononciation.

Le générateur utilise notamment la convention X-SAMPA `G` pour `/ɣ/`.

## Ressources utilisées

Le travail lexical s'appuie sur le texte du corpus CoCLiCo-darija et sur le **Darija Open Dataset (DODa)**.

Les enregistrements audio, les TextGrid, les fichiers CSV de travail et les dictionnaires finaux ne sont pas inclus dans cette version du dépôt. Le dépôt se concentre sur les scripts et la documentation méthodologique associés au mémoire.

## Logiciels

- Praat
- Python 3
- pandas
