# 04_extraire_F1_F2_depuis_occurrences.praat
# Projet : CoCLiCo-darija - étude acoustique de l'emphase
# Objet : extraire automatiquement F1 et F2 au point médian (50 %) de chaque
#         occurrence vocalique déjà sélectionnée et validée dans un CSV.
#
# Principe adapté de procédures existantes d'analyse vocalique sous Praat :
# - McCloy & McGrath, SemiAutoFormantExtractor
#   https://github.com/drammock/praat-semiauto
# - J. M. Riebold, Arpabet Vowel Analyzer
#   https://github.com/jmriebold/Praat-Tools
# - W. Elvira García, vowel scripts
#   https://github.com/wendyelviragarcia/vowels
#
# Le script NE détecte PAS lui-même le contexte emphatique/non emphatique.
# Il lit un fichier d'occurrences déjà nettoyé contenant au minimum :
#   locuteur, condition, index_voyelle, voyelle_annotee, voyelle_analyse,
#   realisation, debut_voyelle, fin_voyelle, inclure_analyse_principale
#
# Utilisation recommandée : une exécution par locuteur et par condition.
# Paramètres utilisés dans l'étude :
#   H22/A22 : plafond des formants = 5000 Hz
#   S22/F22 : plafond des formants = 5500 Hz
#   5 formants ; fenêtre = 0.025 s ; préaccentuation = 50 Hz

form: "Extraction automatique F1 F2 a 50 pour cent"
    infile: "Fichier audio", "A_22.wav"
    infile: "Fichier occurrences", "A22_EMPH_analyse_nettoye.csv"
    outfile: "Fichier sortie", "H22_EMPH_formants.csv"
    positive: "Plafond formants", "5000"
endform


# 1. LECTURE DU FICHIER D'OCCURRENCES ET DU SON

occurrences = Read Table from comma-separated file: fichier_occurrences$
sound = Read from file: fichier_audio$


# 2. ANALYSE FORMANTIQUE DU SON ENTIER
#    Paramètres : Burg ; 5 formants ; fenêtre 25 ms ; préaccentuation 50 Hz.


selectObject: sound
formant = To Formant (burg): 0, 5, plafond_formants, 0.025, 50


# 3. FICHIER DE SORTIE

writeFileLine: fichier_sortie$, "locuteur,condition,index_voyelle,voyelle_annotee,voyelle_qualite,realisation,debut_voyelle,fin_voyelle,temps_milieu,F1_Hz,F2_Hz"

nombre_lignes = object[occurrences].nrow
nombre_mesurees = 0
nombre_ignorees = 0
nombre_indefinies = 0


# 4. PARCOURS DE TOUTES LES OCCURRENCES DU CSV

for ligne from 1 to nombre_lignes

    inclure$ = object$ [occurrences, ligne, "inclure_analyse_principale"]

    # Seules les occurrences validées pour l'analyse principale sont mesurées.
    if inclure$ = "oui"

        locuteur$ = object$ [occurrences, ligne, "locuteur"]
        condition$ = object$ [occurrences, ligne, "condition"]
        indexV = object [occurrences, ligne, "index_voyelle"]
        voyelle_annotee$ = object$ [occurrences, ligne, "voyelle_annotee"]
        voyelle_analyse$ = object$ [occurrences, ligne, "voyelle_analyse"]
        realisation$ = object$ [occurrences, ligne, "realisation"]
        debutV = object [occurrences, ligne, "debut_voyelle"]
        finV = object [occurrences, ligne, "fin_voyelle"]

        # Regroupement phonologique retenu dans l'étude :
        # [a:] -> /a/, [i:] -> /i/, [u:] -> /u/ ;
        # une réalisation [o] déjà classée comme /u/ dans voyelle_analyse
        # reste donc dans la catégorie /u/.
        voyelle_qualite$ = ""
        if voyelle_analyse$ = "a" or voyelle_analyse$ = "a:"
            voyelle_qualite$ = "a"
        elsif voyelle_analyse$ = "i" or voyelle_analyse$ = "i:"
            voyelle_qualite$ = "i"
        elsif voyelle_analyse$ = "u" or voyelle_analyse$ = "u:"
            voyelle_qualite$ = "u"
        elsif voyelle_analyse$ = "ə"
            voyelle_qualite$ = "ə"
        endif

        # Une occurrence dont la catégorie n'appartient pas à /a i u ə/
        # n'entre pas dans l'analyse principale.
        if voyelle_qualite$ <> ""

            # Point médian de la voyelle : début + 0,5 x durée.
            tempsMilieu = debutV + 0.5 * (finV - debutV)

            # Lecture des deux premiers formants au même instant.
            selectObject: formant
            f1 = Get value at time: 1, tempsMilieu, "Hertz", "Linear"
            f2 = Get value at time: 2, tempsMilieu, "Hertz", "Linear"

            # Les valeurs indéfinies sont explicitement conservées comme telles.
            if f1 = undefined or f2 = undefined
                f1$ = "--undefined--"
                f2$ = "--undefined--"
                nombre_indefinies = nombre_indefinies + 1
            else
                f1$ = fixed$ (f1, 6)
                f2$ = fixed$ (f2, 6)
            endif

            ligne_sortie$ = locuteur$ + "," + condition$ + "," + fixed$ (indexV, 0) + "," + voyelle_annotee$ + "," + voyelle_qualite$ + "," + realisation$ + "," + fixed$ (debutV, 6) + "," + fixed$ (finV, 6) + "," + fixed$ (tempsMilieu, 6) + "," + f1$ + "," + f2$
            appendFileLine: fichier_sortie$, ligne_sortie$

            nombre_mesurees = nombre_mesurees + 1
        else
            nombre_ignorees = nombre_ignorees + 1
        endif

    else
        nombre_ignorees = nombre_ignorees + 1
    endif
endfor

# 5. NETTOYAGE ET RAPPORT

removeObject: formant, sound, occurrences

writeInfoLine: "Extraction terminée."
appendInfoLine: "Fichier audio : ", fichier_audio$
appendInfoLine: "Fichier d'occurrences : ", fichier_occurrences$
appendInfoLine: "Fichier créé : ", fichier_sortie$
appendInfoLine: "Occurrences mesurées : ", nombre_mesurees
appendInfoLine: "Occurrences ignorées : ", nombre_ignorees
appendInfoLine: "Mesures indéfinies : ", nombre_indefinies
appendInfoLine: "Plafond des formants : ", plafond_formants, " Hz"
