# 02_extraire_occurrences_non_emphatiques.praat
# analyse acoustique de l'emphase en arabe marocain
# Etape 2 : extraction des contreparties non emphatiques et des voyelles immediatement adjacentes

form Extraction des contextes non emphatiques
    sentence Code_locuteur A_22
    sentence Fichier_TextGrid A_22_segF.TextGrid
    sentence Fichier_sortie A22_NEMPH.csv
endform

Read from file: Fichier_TextGrid$
tg = selected("TextGrid")

tier = 1
n = Get number of intervals: tier

if fileReadable(Fichier_sortie$)
    deleteFile: Fichier_sortie$
endif

appendFileLine: Fichier_sortie$, "locuteur,index_consonne,consonne_non_emphatique,contrepartie_emphatique,voyelle,position,index_voyelle,debut_voyelle,fin_voyelle,duree_voyelle,contexte_brut"

nbConsonnes = 0
nbPaires = 0

for i from 1 to n
    selectObject: tg
    consonne$ = Get label of interval: tier, i
    consonne$ = replace$(consonne$, " ", "", 0)

    contrepartie$ = ""

    if consonne$ = "t"
        contrepartie$ = "tˤ"
    elsif consonne$ = "d"
        contrepartie$ = "dˤ"
    elsif consonne$ = "s"
        contrepartie$ = "sˤ"
    elsif consonne$ = "z"
        contrepartie$ = "zˤ"
    elsif consonne$ = "r"
        contrepartie$ = "rˤ"
    elsif consonne$ = "l"
        contrepartie$ = "lˤ"
    endif

    if contrepartie$ <> ""
        nbConsonnes = nbConsonnes + 1

        if i > 1
            voyelle$ = Get label of interval: tier, i - 1
            voyelle$ = replace$(voyelle$, " ", "", 0)

            if voyelle$ = "a" or voyelle$ = "a:" or voyelle$ = "i" or voyelle$ = "i:" or voyelle$ = "u" or voyelle$ = "u:" or voyelle$ = "ə" or voyelle$ = "o" or voyelle$ = "e"
                debutV = Get starting point: tier, i - 1
                finV = Get end point: tier, i - 1
                dureeV = finV - debutV
                contexte$ = voyelle$ + "_" + consonne$
                ligne$ = Code_locuteur$ + "," + string$(i) + "," + consonne$ + "," + contrepartie$ + "," + voyelle$ + ",avant," + string$(i - 1) + "," + fixed$(debutV, 6) + "," + fixed$(finV, 6) + "," + fixed$(dureeV, 6) + "," + contexte$
                appendFileLine: Fichier_sortie$, ligne$
                nbPaires = nbPaires + 1
            endif
        endif

        if i < n
            voyelle$ = Get label of interval: tier, i + 1
            voyelle$ = replace$(voyelle$, " ", "", 0)

            if voyelle$ = "a" or voyelle$ = "a:" or voyelle$ = "i" or voyelle$ = "i:" or voyelle$ = "u" or voyelle$ = "u:" or voyelle$ = "ə" or voyelle$ = "o" or voyelle$ = "e"
                debutV = Get starting point: tier, i + 1
                finV = Get end point: tier, i + 1
                dureeV = finV - debutV
                contexte$ = consonne$ + "_" + voyelle$
                ligne$ = Code_locuteur$ + "," + string$(i) + "," + consonne$ + "," + contrepartie$ + "," + voyelle$ + ",apres," + string$(i + 1) + "," + fixed$(debutV, 6) + "," + fixed$(finV, 6) + "," + fixed$(dureeV, 6) + "," + contexte$
                appendFileLine: Fichier_sortie$, ligne$
                nbPaires = nbPaires + 1
            endif
        endif
    endif
endfor

writeInfoLine: "Extraction NEMPH terminee."
appendInfoLine: "Locuteur : ", Code_locuteur$
appendInfoLine: "Consonnes non emphatiques reperees : ", nbConsonnes
appendInfoLine: "Paires consonne-voyelle : ", nbPaires
appendInfoLine: "CSV cree : ", Fichier_sortie$
