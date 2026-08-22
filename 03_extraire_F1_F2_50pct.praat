# 03_extraire_F1_F2_50pct.praat
# Projet : analyse acoustique de l'emphase en arabe marocain
# Etape 3 : extraction de F1 et F2 au point median de la voyelle
# Ce script illustre le coeur de la procedure acoustique utilisee.
# Il suppose que les bornes vocaliques ont deja ete validees.

form Extraction F1 F2 a 50 pour cent
    sentence Fichier_audio A_22.wav
    real Plafond_formants 5000
    real Debut_voyelle 0
    real Fin_voyelle 0.1
endform

Read from file: Fichier_audio$
sound = selected("Sound")

tempsMilieu = Debut_voyelle + 0.5 * (Fin_voyelle - Debut_voyelle)

selectObject: sound
formant = To Formant (burg): 0, 5, Plafond_formants, 0.025, 50

selectObject: formant
F1 = Get value at time: 1, tempsMilieu, "Hertz", "Linear"
F2 = Get value at time: 2, tempsMilieu, "Hertz", "Linear"

writeInfoLine: "Temps milieu : ", fixed$(tempsMilieu, 6), " s"
appendInfoLine: "F1 : ", fixed$(F1, 2), " Hz"
appendInfoLine: "F2 : ", fixed$(F2, 2), " Hz"
