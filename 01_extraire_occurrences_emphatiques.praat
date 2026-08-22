# 01_extraire_occurrences_emphatiques.praat
# Projet : analyse acoustique de l'emphase en arabe marocain
# Étape 1 : présélection automatique des consonnes emphatiques et des voyelles immédiatement adjacentes
# IMPORTANT : ce script ne syllabifie pas le corpus.
# Les occurrences extraites doivent ensuite être validées
# manuellement dans Praat pour vérifier l'appartenance à une même syllabe.


form Présélection des occurrences candidates
    sentence Code_locuteur A_22
    sentence Fichier_TextGrid A_22_segF.TextGrid
    sentence Fichier_sortie candidats_A_22.csv
endform

Read from file: Fichier_TextGrid$
tg = selected("TextGrid")

# Les TextGrids finaux utilisés ici possèdent un seul tier : phonemes.
tier = 1
n = Get number of intervals: tier

# Recréer le fichier CSV à chaque exécution.
if fileReadable(Fichier_sortie$)
    deleteFile: Fichier_sortie$
endif

appendFileLine: Fichier_sortie$, "locuteur,index_consonne,consonne_emphatique,voyelle,position,index_voyelle,debut_voyelle,fin_voyelle,duree_voyelle,contexte_brut"

nbEmphatiques = 0
nbPairesCandidates = 0

for i from 1 to n
    selectObject: tg
    consonne$ = Get label of interval: tier, i
    consonne$ = replace$(consonne$, " ", "", 0)

    if consonne$ = "tˤ" or consonne$ = "dˤ" or consonne$ = "sˤ" or consonne$ = "zˤ" or consonne$ = "rˤ" or consonne$ = "lˤ"
        nbEmphatiques = nbEmphatiques + 1

       
        # Voyelle immédiatement AVANT
        if i > 1
            voyelleAvant$ = Get label of interval: tier, i - 1
            voyelleAvant$ = replace$(voyelleAvant$, " ", "", 0)

            if voyelleAvant$ = "a" or voyelleAvant$ = "a:" or voyelleAvant$ = "i" or voyelleAvant$ = "i:" or voyelleAvant$ = "u" or voyelleAvant$ = "u:" or voyelleAvant$ = "ə" or voyelleAvant$ = "o" or voyelleAvant$ = "e"
                debutV = Get starting point: tier, i - 1
                finV = Get end point: tier, i - 1
                dureeV = finV - debutV
                contexte$ = voyelleAvant$ + "_" + consonne$

                ligne$ = Code_locuteur$ + "," + string$(i) + "," + consonne$ + "," + voyelleAvant$ + ",avant," + string$(i - 1) + "," + fixed$(debutV, 6) + "," + fixed$(finV, 6) + "," + fixed$(dureeV, 6) + "," + contexte$
                appendFileLine: Fichier_sortie$, ligne$
                nbPairesCandidates = nbPairesCandidates + 1
            endif
        endif

     
        # Voyelle immédiatement APRÈS
     
        if i < n
            voyelleApres$ = Get label of interval: tier, i + 1
            voyelleApres$ = replace$(voyelleApres$, " ", "", 0)

            if voyelleApres$ = "a" or voyelleApres$ = "a:" or voyelleApres$ = "i" or voyelleApres$ = "i:" or voyelleApres$ = "u" or voyelleApres$ = "u:" or voyelleApres$ = "ə" or voyelleApres$ = "o" or voyelleApres$ = "e"
                debutV = Get starting point: tier, i + 1
                finV = Get end point: tier, i + 1
                dureeV = finV - debutV
                contexte$ = consonne$ + "_" + voyelleApres$

                ligne$ = Code_locuteur$ + "," + string$(i) + "," + consonne$ + "," + voyelleApres$ + ",apres," + string$(i + 1) + "," + fixed$(debutV, 6) + "," + fixed$(finV, 6) + "," + fixed$(dureeV, 6) + "," + contexte$
                appendFileLine: Fichier_sortie$, ligne$
                nbPairesCandidates = nbPairesCandidates + 1
            endif
        endif
    endif
endfor

writeInfoLine: "Extraction terminée."
appendInfoLine: "Locuteur : ", Code_locuteur$
appendInfoLine: "Nombre total de consonnes emphatiques repérées : ", nbEmphatiques
appendInfoLine: "Nombre de paires consonne-voyelle candidates : ", nbPairesCandidates
appendInfoLine: "CSV créé : ", Fichier_sortie$
appendInfoLine: "Étape suivante : validation manuelle de l'appartenance à la même syllabe."
