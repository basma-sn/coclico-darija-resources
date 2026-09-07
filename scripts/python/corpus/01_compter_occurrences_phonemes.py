import re
from pathlib import Path

TEXTE = """
waħd nnha:r tˤlaqaːt ʃʃəmʃ mʕa lʕʒaːʒ
u kula waħd fihum bda kibaːn ʕla laːxur
ʃʃəmʃ katguːl ana səħ mnk alʕʒaːʒ, kantˤlq dˤdˤoː dja:li u kansˤxn lħaːl
u ħeta ħaʒa makatqdi ʕlija wəla katzəʕzəʕni
lʕʒaːʒ huwa jʒawbha u gaːl liha ama ana kanʒi mʕa ʃʃta u kandir lbrd]
ħəta mn lmdˤalˤat kantˤejərhum
ʔama ila saːqu lija lxəba:r ʒaːj kidiru ʕlija nachra indaːrja f ttəlfaza
bqaw kitlaʒu ʕla ʃkun li fihum səħ mn laːxor
u ʕndo lʒurʔa bəch jbjən lqodˤorat djalu
waħd ʃwija u huwa jduz waħed 	
ʃad tˤriq mn blad bʕida u ʒaj bəch jdˤor flmdina
dak rrˤaʒəl məlwi fwaħed lkabu:tˤ sxuːn djal sˤuf
u səxfaːn haz fidih poʃiːtˤa fiha piʒama u zˤina djal lkisan
u gaʕ lwraq djalu ħit ʒaj jaxod lviza, ʕəndu vol f ʒuʒ simana:t
baɣi jzˤor wəldu fra:nsˤa t͡ʃuwəʃ ʕlih ħit kan mridˤ
u hadak nnha:r ɣadi jduwzu ʕənd saħbu li ʕəndo villa kbira f sˤontˤr vil
dik zˤzˤina djal lkisan ʃraha lih cado
ʃʃəmʃ u lʕʒaːʒ baːn lihum rrˤaʒəl flblan u huma jtaːfqu
ʕla lˤi mʃa ħəta gləʕ rrˤaʒəl kabuːtˤo
u tˤijəħ lih dəkchi li haz fʔidu huwa sˤsˤħiħ fihum
fkr lʕʒaːʒ mzjaːn u gal mʕa rasˤo xasˤo jdir chi ʕasˤifa baʃ jtˤejərˤ lħwajʒ djal rrˤaʒəl
u huwa jbda kisotˤ ʕla ħar ʒəhdu
u dar riħ li tˤijəħ ddˤjor u ʒʒbal
u txləʕ ddʒaj u lɣnm li katrʕa f ʒʒnaːnaːt
dˤalˤm lħal u dˤrb lbərq
walaki:n kulma saːtˤ u kulma ħaːwəl jtˤejrˤ lkabu:tˤ djal rrˤaʒəl
u rrˤaʒəl kiziːd jlwi ʕlih lħwajʒ u kiziːd jzˤijrˤ ʕlih smtˤa djal lkabu:tˤ
u flxər ʕja lʕʒaːʒ u sˤxf bquwat sˤsˤotˤaːn u huwa jhda
u gal ʃʃəmʃ bijni lija ʕlajach gadˤa
ʃʃəmʃ galt lih araːk lfraːʒa daba tʃuf sijadk ʕlach qa:din
u xərʒaːt ʃʃəmʃ u baːnt u tˤlqaːt lħaraːra djalha
ħma lħal ldaraʒat ʔaj waħəd kan xarəʒ dak nnha:r t͡ʃuwetˤ lih wʒhu blħarara
sxan rrˤaʒəl u ʒah sˤsˤahd
u huwa jgul bəʃ nqdi ʃʃɣul dja:li dəɣija xasˤni nħijəd had lkabuːtˤ
qtəlni sˤsˤahd haːd lʒaw mabqina faːhmiːn fih walu
gləʕ lkabuːtˤ djalu u xʃaːh flpoʃiːtˤa mʕa lħwajʒ
tma lʕʒaːʒ mabqaliːh ila jəʕtarəf bilˤa ʃʃəmʃ səħ mnu u bila maʕəndu zˤhar
ʃʃəmʃ ʕʒbha lħal walaki:n lʕʒaːʒ bqa fih lħal bzaːf
u ħəs braːssu dar xataːʔ ldaraʒat bəka mʕah ssma
u hija tsˤob ʃta walaki:n ʃʃəmʃ bqat xarʒa
rrˤaʒəl məskin maʕrəf majdir bqa ɣadi ʃaːd triqu
u hija tħbss ʃʃta u lʒaw wəla zwin u xrj qawsˤa quzəħ blʔalwan djalu
rrˤaʒəl blfrħa sˤona ʕla wlaːdu apel vidjo
bəʃ jwərˤihum lmandˤar lɣariːb u jʕaːwəd lihum ʃnu wqəʕ lih ftriq
u huwa jgul fxaːtru kun dˤaːrbat ʃʃəmʃ u lʕʒaːʒ tawaħd fihum maɣajrbəħ]
ħit bla biːhum bħal had lmandˤar ʕmru kan ɣadi jkuːn
səmʕatu ʃʃəmʃ u lʕʒaːʒ u farˤħu
tsˤaːlħu u gaːlu lbəʕdijathum biːla bsˤħ ʕəndu lħaq maxasˤnaːch ndˤaːrbu
rrˤaʒəl btaːsəm u fkr bila xasu jsˤlˤi waħd ʒuʒ rəkʕaːt məni jwsˤalˤ ldˤarˤ jħməd fiha rəbˤi u jʃəkru
"""

# Liste des phonèmes à compter
PHONEMES = [
    # Voyelles longues
    "iː", "uː", "aː",
    # Emphatiques
    "tˤ", "dˤ", "sˤ", "zˤ", "rˤ",
    # Affriquées
    "t͡ʃ",
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
    ("Les emphatiques",   ["tˤ", "sˤ", "dˤ", "zˤ", "rˤ"]),
    ("Nasales",           ["m", "n"]),
    ("Liquides",          ["l", "r"]),
    ("Approximantes",     ["w", "j"]),
    ("Affriquées",        ["t͡ʃ"]),
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
