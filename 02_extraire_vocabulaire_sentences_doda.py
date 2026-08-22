import pandas as pd
import re

# Charger le fichier
df = pd.read_csv("sentences.csv")

# Compter les caractères arabes
def compter_arabe(texte):
    if pd.isna(texte):
        return 0

    return len(re.findall(r'[\u0600-\u06FF]', str(texte)))

# Trouver la colonne qui contient le plus d'arabe
scores = {}

for col in df.columns:
    scores[col] = df[col].astype(str).apply(compter_arabe).sum()

colonne_arabe = max(scores, key=scores.get)

print("Colonne arabe détectée :", colonne_arabe)

# Garder les phrases qui contiennent de l'arabe
expressions_arabes = (
    df[colonne_arabe]
    .dropna()
    .astype(str)
    .str.strip()
)

expressions_arabes = expressions_arabes[
    expressions_arabes.str.contains(
        r'[\u0600-\u06FF]',
        regex=True
    )
]

# Extraire les mots arabes
mots = set()

for phrase in expressions_arabes:
    mots_phrase = re.findall(
        r'[\u0600-\u06FF]+',
        phrase
    )

    for mot in mots_phrase:
        if mot.strip():
            mots.add(mot.strip())

# Trier les mots
mots_uniques = sorted(mots)

print("Nombre de mots uniques :", len(mots_uniques))

# Créer le CSV
df_mots = pd.DataFrame({
    "mot_arabe": mots_uniques
})

df_mots.to_csv(
    "vocabulaire_unique_2.csv",
    index=False,
    encoding="utf-8-sig"
)

print("Fichier créé : vocabulaire_unique_2.csv")
