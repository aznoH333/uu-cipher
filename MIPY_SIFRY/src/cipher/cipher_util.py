import random
from random import randrange
    
BASE_ALPHABET = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "_"]
CHARACTER_CONVERION_TABLE = {
    "Ě": "E",
    "Š": "S",
    "Č": "C",
    "Ř": "R",
    "Ž": "Z",
    "Ý": "Y",
    "Á": "A",
    "Í": "I",
    "É": "E",
    "Ť": "T",
    "Ň": "N",
    "Ú": "U",
    "Ů": "U",
    "Ó": "O",
    "Ď": "D",
    ".": "_",
    ",": "_",
    "?": "_",
    ";": "_",
    " ": "_"
}



def encrypt(key, text):
    out = ""
    for char in text.upper():
        out += key[BASE_ALPHABET.index(char)]
        
    return out

def decrypt(key, text):
    
    out = ""
    for char in text.upper():
        out += BASE_ALPHABET[key.index(char)]
        
    return out

def sanitize_text(text, include_duplicate_spaces):
    decoded = str(text.upper().replace("\n", ""))
    out = ""
    pushedSpaceLast = False
    for i in range(0, len(decoded)):
        char = decoded[i]
            
        #remap unicode
        if char in CHARACTER_CONVERION_TABLE:
            char = CHARACTER_CONVERION_TABLE[char]
            
            
        #dont include duplicate spaces
        if char == '_' and pushedSpaceLast and not include_duplicate_spaces:
            continue


        #check if is part of the alphabet
        if char in BASE_ALPHABET:
            out += char
            pushedSpaceLast = (char == '_')
            continue

    return out


def generate_random_key():
    output = []

    for char in BASE_ALPHABET:
        output.append(char)

    random.shuffle(output)

    return output

def shuffle_key(key):
    random_1 = randrange(0, len(BASE_ALPHABET))
    random_2 = randrange(0, len(BASE_ALPHABET) - 1)

    if random_2 >= random_1:
        random_2 += 1

    temp = key[random_1]

    key[random_1] = key[random_2]
    key[random_2] = temp

    return key
