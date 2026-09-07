# -*- coding: utf-8 -*-

import os
import re
import pandas as pd

# Fichiers

INPUT_FILE = "vocabulaire_unique_2.csv"
OUTPUT_FILE = "D22.dict"


# Exceptions
# Certains mots passent mal avec les règles générales
# On met ici leur prononciation corrigée
# Plusieurs variantes peuvent être gardées pour un même mot

EXCEPTIONS = {'و': ['u'],
 'ما': ['m a'],
 'لا': ['l a:'],
 'واش': ['w a S'],
 'آش': ['a: S'],
 'أش': ['a S'],
 'أنا': ['? a n a', 'n a'],
 'حنا': ['X\\ n a'],
 'نتا': ['n t a', 'n t i n a', 't a', 't a j a'],
 'هو': ['h u w a'],
 'هيا': ['h i j a'],
 'هوما': ['h u m a'],
 'في': ['f i:', 'f i', 'f'],
 'من': ['m @ n', 'm n'],
 'على': ['?\\ l a'],
 'إلى': ['l'],
 'ب': ['b i', 'b @'],
 'ل': ['l i', 'l'],
 'ف': ['f'],
 'مع': ['m ?\\ a'],
 'بلا': ['b @ l a'],
 'بعد': ['b ?\\ d', 'b a ?\\ d'],
 'قبل': ['q b @ l'],
 'هنا': ['h n a'],
 'تما': ['t @ m m a'],
 'دابا': ['d a: b a'],
 'درك': ['d @ r k', 'd r u k', 'd r u k a'],
 'بكري': ['b @ k r i:'],
 'فوق': ['f u q', 'f u g'],
 'تحت': ['t @ X\\ t'],
 'قدام': ['q @ d a: m', 'g d @ a: m', 'q u d a: m'],
 'ورا': ['w r a'],
 'وسط': ['w @ s_?\\ @ t_?\\'],
 'بين': ['b i: n'],
 'راه': ['r a: h'],
 'راني': ['r a: n i:'],
 'ياك': ['j a: k', 'j a: k i'],
 'إيه': ['? i j j @ h', '? i j @ h'],
 'آه': ['? a: h'],
 'واه': ['w a: h'],
 'نعام': ['n ?\\ a m'],
 'والو': ['w a: l u'],
 'بزاف': ['b @ z a: f'],
 'مزيان': ['m @ z j a: n'],
 'غير': ['G i r'],
 'إلا': ['? i l l a'],
 'حتى': ['X\\ @ t t a'],
 'باش': ['b a: S'],
 'ولكن': ['w a l a k i n'],
 'لي': ['l l i'],
 'كيما': ['k i: m a'],
 'بحال': ['b @ X\\ a: l'],
 'كان': ['k a: n'],
 'كانت': ['k a: n @ t'],
 'كانو': ['k a: n u'],
 'كنا': ['k n a', 'k u n a'],
 'كنتو': ['k n t u', 'k u n t u'],
 'كنتي': ['k n t i'],
 'كا': ['k a'],
 'كاين': ['k a: j @ n'],
 'كاينة': ['k a: j n a'],
 'كاينين': ['k a: j n i: n'],
 'مكاينش': ['m a k a: j n S'],
 'ديال': ['d j a: l'],
 'ديالي': ['d j a: l i'],
 'ديالك': ['d j a: l @ k'],
 'ديالنا': ['d j a: l n a'],
 'ديالهم': ['d j a: l h @ m'],
 'ديالو': ['d j a: l u'],
 'ديالها': ['d j a: l h a'],
 'هاد': ['h a: d'],
 'هادا': ['h a: d a'],
 'هادي': ['h a: d i'],
 'هادو': ['h a: d u'],
 'عند': ['?\\ @ n d'],
 'عندي': ['?\\ @ n d i'],
 'عندك': ['?\\ @ n d @ k'],
 'عندو': ['?\\ @ n d u'],
 'عندنا': ['?\\ @ n d n a'],
 'عندهم': ['?\\ @ n d h @ m'],
 'فين': ['f i: n'],
 'منين': ['m n i: n'],
 'كيفاش': ['k i f a: S'],
 'علاش': ['?\\ l a: S'],
 'شحال': ['S X\\ a: l'],
 'إمتى': ['? i m t a'],
 'شي': ['S i'],
 'خاص': ['x a: s_?\\'],
 'خاصك': ['x a: s_?\\ @ k'],
 'خاصو': ['x a: s_?\\ u'],
 'بغا': ['b G a'],
 'بغيت': ['b G i: t'],
 'اللي': ['? @ l l i'],
 'اسيوية': ['a s i j a w i j a'],
 'الدوا': ['d d w a']}


# Correspondances arabe vers X-SAMPA

DICSAMPA = {
    "ب": "b",
    "ت": "t",
    "ث": "t",
    "ج": "Z",
    "ح": "X\\",
    "خ": "x",
    "د": "d",
    "ذ": "d",
    "ر": "r",
    "ز": "z",
    "س": "s",
    "ش": "S",
    "ص": "s_?\\",
    "ض": "d_?\\",
    "ط": "t_?\\",
    "ظ": "z_?\\",
    "ع": "?\\",
    "غ": "G",
    "ف": "f",
    "ق": "q",
    "ك": "k",
    "ل": "l",
    "م": "m",
    "ن": "n",
    "ه": "h",

    # Graphies marocaines et emprunts
    "پ": "p",
    "ڤ": "v",
    "ڥ": "v",
    "گ": "g",
    "ڭ": "g",
    "ڨ": "g",
    "چ": "tS",

    "ا": "a",
    "ى": "a",
}


# Harakat et signes

FATHA = "\u064e"
DAMMA = "\u064f"
KASRA = "\u0650"
SUKUN = "\u0652"
SHADDA = "\u0651"
TANWIN_FATH = "\u064b"
TANWIN_DAMM = "\u064c"
TANWIN_KASR = "\u064d"
TATWEEL = "\u0640"

HARAKAT = {
    FATHA: "a",
    DAMMA: "u",
    KASRA: "i",
    TANWIN_FATH: "a n",
    TANWIN_DAMM: "u n",
    TANWIN_KASR: "i n",
}

# Garder une seule voyelle quand une haraka marque déjà la longueur
LONGUES = {
    (FATHA, "ا"): "a:",
    (DAMMA, "و"): "u:",
    (KASRA, "ي"): "i:",
}


# Article ال

CORONALES = {
    "ت", "ث", "د", "ذ", "ر", "ز", "س", "ش",
    "ص", "ض", "ط", "ظ", "ل", "ن"
}


def apply_article_rule(word):
    # Exemple : الدار -> ددار ; الكتاب -> لكتاب
    if not word.startswith("ال") or len(word) <= 2:
        return word

    first = word[2]

    if first in CORONALES:
        return first + word[2:]

    return "ل" + word[2:]


def normalize_word(word):
    word = word.replace(TATWEEL, "")
    word = word.replace("ؤ", "ءو")
    word = word.replace("ئ", "ءي")
    return word


def is_arabic_letter(ch):
    return bool(re.match(r"[\u0621-\u064A\u067E\u06A4\u06A5\u06AF\u06AD\u0686\u06A8]", ch))


def previous_letter(word, index):
    j = index - 1
    while j >= 0:
        if is_arabic_letter(word[j]):
            return word[j]
        j -= 1
    return ""


def has_previous_haraka(word, index, haraka):
    j = index - 1
    while j >= 0:
        if word[j] == haraka:
            return True
        if is_arabic_letter(word[j]):
            return False
        j -= 1
    return False


def fix_arabizi(text):
    # Quelques résidus x/X utilisés pour ش dans certaines données.
    AR = r"\u0600-\u06FF\u0750-\u077F\uFB50-\uFDFF\uFE70-\uFEFF"
    text = re.sub(r"\bxi\b", "شي", text, flags=re.IGNORECASE)
    text = re.sub(rf"[xX](?=[{AR}])", "ش", text)
    text = re.sub(rf"(?<=[{AR}])[xX]", "ش", text)
    return text


# و et ي

def transcribe_waw(word, i):
    if has_previous_haraka(word, i, DAMMA):
        return "u:"
    if i == 0:
        return "w"
    if previous_letter(word, i):
        return "u"
    return "w"


def transcribe_ya(word, i):
    if has_previous_haraka(word, i, KASRA):
        return "i:"
    if i == 0:
        return "j"
    if previous_letter(word, i):
        return "i"
    return "j"


# Transcription d’un mot

def word_to_sampa(word):
    word = normalize_word(word)
    word = apply_article_rule(word)

    phones = []
    i = 0

    while i < len(word):
        ch = word[i]

        # Voyelles longues : بُو -> b u: et pas b u u:
        if i + 1 < len(word) and (ch, word[i + 1]) in LONGUES:
            phones.append(LONGUES[(ch, word[i + 1])])
            i += 2
            continue

        if ch in HARAKAT:
            phones.extend(HARAKAT[ch].split())
            i += 1
            continue

        if ch == SUKUN:
            i += 1
            continue

        # Shadda : on répète le phonème précédent.
        if ch == SHADDA:
            if phones:
                phones.append(phones[-1])
            i += 1
            continue

        if ch == "ة":
            phones.append("a")
            i += 1
            continue

        if ch == "ء":
            phones.append("?")
            i += 1
            continue

        # Hamza avec alif.
        if ch in ["أ", "إ"]:
            next_char = word[i + 1] if i + 1 < len(word) else ""

            if next_char == DAMMA:
                phones.extend(["?", "u"])
                i += 2
                continue

            if next_char == KASRA or ch == "إ":
                phones.extend(["?", "i"])
                i += 2 if next_char == KASRA else 1
                continue

            if next_char == FATHA:
                if i + 2 < len(word) and word[i + 2] == "ا":
                    phones.extend(["?", "a:"])
                    i += 3
                else:
                    phones.extend(["?", "a"])
                    i += 2
                continue

            phones.extend(["?", "a"])
            i += 1
            continue

        if ch == "آ":
            phones.extend(["?", "a:"])
            i += 1
            continue

        if ch == "و":
            phones.append(transcribe_waw(word, i))
            i += 1
            continue

        if ch == "ي":
            phones.append(transcribe_ya(word, i))
            i += 1
            continue

        if ch == "ا":
            if has_previous_haraka(word, i, FATHA):
                phones.append("a:")
            else:
                phones.append("a")
            i += 1
            continue

        if ch in DICSAMPA:
            phones.append(DICSAMPA[ch])
            i += 1
            continue

        i += 1

    return " ".join(phones)


# Prononciations retenues

def pronunciations_for_word(word):
    # Les exceptions passent toujours avant les règles générales.
    if word in EXCEPTIONS:
        return list(dict.fromkeys(EXCEPTIONS[word]))

    pron = word_to_sampa(word)
    variantes = [pron] if pron else []

    # Variante trouvée dans le premier code pour la négation ma...ch.
    if word.startswith("ما") and word.endswith("ش") and pron:
        variantes.append(pron + " i")

    return list(dict.fromkeys(variantes))


# Création du dictionnaire

def create_dictionary(csv_file=INPUT_FILE, output_file=OUTPUT_FILE):
    df = pd.read_csv(csv_file, encoding="utf-8-sig")

    if "mot_arabe" not in df.columns:
        raise ValueError("La colonne 'mot_arabe' est absente du fichier CSV.")

    all_words = set()

    for line in df["mot_arabe"].dropna():
        line = fix_arabizi(str(line))
        words = re.findall(r"[\u0600-\u06FF]+", line)

        for word in words:
            if word.strip():
                all_words.add(word.strip())

    all_words = sorted(all_words)

    with open(output_file, "w", encoding="utf-8") as out:
        for word in all_words:
            for pron in pronunciations_for_word(word):
                if pron:
                    out.write(f"{word}\t{pron}\n")

    print("Nombre de mots uniques :", len(all_words))
    print("Dictionnaire créé :", output_file)

    return output_file


# Colab
# Si le CSV manque, Colab ouvre la fenêtre d’upload


if __name__ == "__main__":
    colab_files = None

    try:
        from google.colab import files as colab_files
    except ImportError:
        pass

    if not os.path.exists(INPUT_FILE):
        if colab_files is None:
            raise FileNotFoundError(
                "vocabulaire_unique_2.csv est introuvable. Mets-le dans le même dossier que le script."
            )

        print("Choisis le fichier vocabulaire_unique_2.csv")
        colab_files.upload()

    create_dictionary(INPUT_FILE, OUTPUT_FILE)

    if colab_files is not None:
        colab_files.download(OUTPUT_FILE)
