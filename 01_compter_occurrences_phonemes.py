import re
from pathlib import Path

TEXTE = """
waħd nnha:r tˤlaqaːt ʃʃəmʃ mʕa lʕʒaːʒ
u kulˁa waħd fihum bda kibaːn ʕla laːxur
ʃʃəmʃ katguːl ana səħ mnk alʕʒaːʒ, kantˤlq dˤdˤoː dja:li u kansˤxn lħaːl
u ħəta ħaja makatqdi ʕlija wəla katzʕzʕni
lʕʒaːʒ huwa jʒawbha u gaːl liha ama ana kanʒi mʕa ʃʃta u kandir lbrd
ħəta mn lmdˤəlˤat kantˤijərhum
ama ila saːqu lija lxba:r ʒaːj kidiru ʕlija nachra indaːrja f ttlfaza
bqaw kitlaʒu ʕla ʃkun li fihum səħ mn laːxur
u ʕndo lʒurʔa bəch jbjən lqodˤorat djalu
waħd ʃwija u huwa jduz waħd rrˤaʒəl
ʃad tˤriq mn blad bʕida u ʒaj bəch jdˤor flmdina
dak rrˤaʒəl məlwi fwaħd lkabu:tˤ sxuːn djal sˤuf
u sxfaːn haz fidih poʃiːtˤa fiha piʒama u zˤina djal lkisan
u gaʕ lwraq djalu ħit ʒaj jaxud lviza, ʕəndu vol f ʒuʒ simana:t
baɣi jzˤor wldu fra:nsˤa t͡ʃuwəʃ ʕlih ħit kan mridˤ
u hadak nnha:r ɣadi jduwzu ʕənd saħbu li ʕəndo villa kbira f sˤontˤr vil
dik zˤzˤina djal lkisan ʃraha lih cado
ʃʃəmʃ u lʕʒaːʒ baːn lihum rrˤaʒəl flblan u huma jtaːfqu
ʕla lˤi mʃa ħəta gləʕ rrˤaʒəl kabuːtˤo
u tˤijəħ lih dəkchi li haz fʔidu huwa ssˤħiħ fihum
fkr lʕʒaːʒ mzjaːn u gal mʕa rasˤo xasˤo jdir chi ʕasˤifa baʃ jtˤijrˤ lħwajʒ djal rrˤaʒəl
u huwa jbda kisotˤ ʕla ħər ʒhdu
u dar riħ li tˤijəħ ddˤjor u ʒʒbal
u txləʕ ddʒaj u lɣnm li katrʕa f ʒʒnaːnaːt
dˤlˤm lħal u dˤrb lbrq
walaki:n kulma saːtˤ u kulma ħaːwəl jtˤijrˤ lkabu:tˤ djal rrˤaʒəl
u rrˤaʒəl kiziːd jlwi ʕlih lħwajʒ u kiziːd jzˤijrˤ ʕlih smtˤa djal lkabu:tˤ
u flxər ʕja lʕʒaːʒ u sˤxf bquwat sutˤaːn u huwa jhda
u gal ʃʃəmʃ bijni lija ʕlajach gadˤa
ʃʃəmʃ galt lih araːk lfraːʒa daba tʃuf sijadk ʕlach qa:din
u xərʒaːt ʃʃəmʃ u baːnt tˤlqaːt lħaraːra djalha
ħma lħal ldaraʒat ʔaj waħd kan xarəʒ dak nnha:r t͡ʃuwətˤ lih wʒhu blħarara
sxn rrˤaʒəl u ʒah sˤsˤhd
u huwa jgul bəʃ nqdi ʃʃɣul dja:li dəɣija xasˤni nħijd had lkabuːtˤ
qtlni sˤsˤhd haːd lʒaw mabqina faːhmiːn fih walu
gləʕ

"""

# Liste des phonèmes à compter
PHONEMES = [
    # Voyelles longues
    "iː", "uː", "aː",
    # Emphatiques
    "tˤ", "dˤ", "sˤ", "zˤ", "rˤ", "lˤ",
    # Affriquées
    "t͡ʃ", "d͡ʒ",
    # Occlusives
    "p", "b", "t", "d", "k", "g", "q", "ʔ",
    # Nasales
    "m", "n",
    # Fricatives
    "f", "s", "ʃ", "x", "ħ", "h",
    "v", "z", "ʒ", "ɣ", "ʕ",
    # Liquides
    "r", "l",
    # Approximantes
    "w", "j",
    # Voyelles brèves
    "o", "i", "u", "ə", "a",
]

# Compter les occurrences
phonemes_tries = sorted(PHONEMES, key=len, reverse=True)
compteur = {ph: len(re.findall(re.escape(ph), TEXTE)) for ph in phonemes_tries}
total = sum(compteur.values())

# Regrouper les résultats
CATEGORIES = [
    ("Occlusives",        ["b", "d", "t", "k", "g", "q", "ʔ", "p"]),
    ("Fricatives",        ["f", "s", "ʃ", "x", "ħ", "h", "v", "z", "ʒ", "ɣ", "ʕ"]),
    ("Les emphatiques",   ["tˤ", "sˤ", "dˤ", "zˤ", "rˤ", "lˤ"]),
    ("Nasales",           ["m", "n"]),
    ("Liquides",          ["l", "r"]),
    ("Approximantes",     ["w", "j"]),
    ("Affriquées",        ["t͡ʃ", "d͡ʒ"]),
    ("Voyelles brèves",   ["a", "i", "u", "ə", "o"]),
    ("Voyelles longues",  ["aː", "iː", "uː"]),
]

# Afficher les résultats
print("\nLes occurrences\n")
for nom_cat, phones in CATEGORIES:
    print(nom_cat)
    for ph in phones:
        nb = compteur.get(ph, 0)
        print(f"* /{ph}/: {nb}")
    print()
