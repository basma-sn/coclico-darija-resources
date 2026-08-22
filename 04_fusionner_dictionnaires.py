from google.colab import files

# Charger les dictionnaires
print("Sélectionne les fichiers .dict à fusionner")
uploaded = files.upload()

# Garder seulement les fichiers .dict
dict_filenames = [
    name for name in uploaded.keys()
    if name.lower().endswith(".dict")
]

if len(dict_filenames) == 0:
    raise ValueError("Aucun fichier .dict n'a été sélectionné.")

print(f"\n{len(dict_filenames)} fichier(s) détecté(s) :")

for name in dict_filenames:
    print("-", name)

# Lire toutes les entrées
toutes_les_lignes = []

for nom_fichier in dict_filenames:
    with open(nom_fichier, "r", encoding="utf-8-sig") as f:
        for ligne in f:
            ligne = ligne.rstrip("\n\r")

            # Ignorer seulement les lignes vides
            if ligne.strip() == "":
                continue

            toutes_les_lignes.append(ligne)

nb_lignes_avant = len(toutes_les_lignes)

# Utiliser le mot arabe pour le tri
def cle_de_tri(ligne):
    parties = ligne.split(maxsplit=1)

    if parties:
        return parties[0]

    return ligne

# Trier les entrées
lignes_triees = sorted(
    toutes_les_lignes,
    key=cle_de_tri
)

# Créer le dictionnaire fusionné
nom_fichier_final = "dictionnaire_darija_complet.dict"

with open(nom_fichier_final, "w", encoding="utf-8") as f:
    f.write("\n".join(lignes_triees) + "\n")

# Afficher le résultat
print("\nFusion terminée")
print("Fichiers fusionnés :", len(dict_filenames))
print("Entrées avant fusion :", nb_lignes_avant)
print("Entrées dans le fichier final :", len(lignes_triees))
print("Fichier créé :", nom_fichier_final)

# Vérifier qu'aucune entrée n'a été perdue
if nb_lignes_avant == len(lignes_triees):
    print("Aucune entrée perdue.")
else:
    print("Attention : le nombre d'entrées a changé.")

# Télécharger le fichier
files.download(nom_fichier_final)
