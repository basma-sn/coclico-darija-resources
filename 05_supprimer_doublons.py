# Nettoyage final du dictionnaire darija

def cle_entree(ligne):
    # Récupérer le mot et sa prononciation
    morceaux = ligne.strip().split(maxsplit=1)

    if not morceaux:
        return None

    mot = morceaux[0]
    pron = ""

    if len(morceaux) > 1:
        pron = " ".join(morceaux[1].split())

    return mot, pron


def nettoyer_lignes(lignes):
    # Garder une seule fois chaque mot + prononciation
    deja_vues = set()
    lignes_finales = []
    nb_doublons = 0
    nb_vides = 0

    for ligne in lignes:
        ligne = ligne.rstrip("\n").rstrip("\r")

        # Ignorer les lignes vides
        if ligne.strip() == "":
            nb_vides += 1
            continue

        cle = cle_entree(ligne)

        if cle in deja_vues:
            nb_doublons += 1
            continue

        deja_vues.add(cle)
        lignes_finales.append(ligne)

    return lignes_finales, nb_doublons, nb_vides


def main():
    from google.colab import files

    # Charger le dictionnaire
    print("Choisis le dictionnaire fusionné à nettoyer")
    uploaded = files.upload()

    dict_files = [
        name for name in uploaded.keys()
        if name.lower().endswith(".dict")
    ]

    if len(dict_files) == 0:
        raise ValueError("Aucun fichier .dict n'a été importé.")

    if len(dict_files) > 1:
        raise ValueError("Importe un seul dictionnaire .dict à la fois.")

    fichier_entree = dict_files[0]
    fichier_sortie = "dictionnaire_darija_final.dict"

    # Lire les entrées
    with open(fichier_entree, "r", encoding="utf-8-sig") as f:
        lignes = f.readlines()

    nb_entrees_depart = sum(
        1 for ligne in lignes
        if ligne.strip()
    )

    lignes_finales, nb_doublons, nb_vides = nettoyer_lignes(lignes)

    # Créer le fichier final
    with open(fichier_sortie, "w", encoding="utf-8") as f:
        if lignes_finales:
            f.write("\n".join(lignes_finales) + "\n")

    # Afficher le résultat
    print("\nRésumé")
    print("Entrées au départ :", nb_entrees_depart)
    print("Doublons supprimés :", nb_doublons)
    print("Lignes vides ignorées :", nb_vides)
    print("Entrées finales :", len(lignes_finales))
    print("Fichier créé :", fichier_sortie)

    # Télécharger le dictionnaire
    files.download(fichier_sortie)


if __name__ == "__main__":
    main()
