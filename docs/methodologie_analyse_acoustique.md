# Méthodologie de l'analyse acoustique

## Chaîne de traitement

1. Segmentation manuelle des enregistrements sous Praat.
2. Présélection automatique des consonnes emphatiques `/tˤ dˤ sˤ zˤ rˤ/` et des voyelles immédiatement adjacentes.
3. Vérification manuelle de l'appartenance de la consonne et de la voyelle au même domaine syllabique.
4. Extraction parallèle des contreparties non emphatiques `/t d s z r /`.
5. Nettoyage des occurrences et suppression des chevauchements problématiques entre EMPH et NEMPH.
6. Regroupement des réalisations longues et brèves selon la qualité vocalique pour l'analyse principale, tout en conservant l'annotation d'origine.
7. Extraction de F1 et F2 au milieu temporel de la voyelle, soit à 50 % de sa durée.
8. Contrôle visuel dans Praat des mesures atypiques.
9. Calcul des moyennes, et différences `F1` et `F2`.

## Paramètres Praat

- Méthode : Burg
- Nombre maximal de formants : 5
- Fenêtre : 25 ms
- Préaccentuation : 50 Hz
- Plafond initial A_22 : 5000 Hz
- Plafond initial S_22 : 5500 Hz
- Point de mesure : 50 % de la durée vocalique

## Important

Le premier script effectue une **présélection par adjacence segmentale**. Il ne réalise pas de segmetation automatique. La validation du domaine syllabique a été effectuée manuellement dans Praat.
