import math
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

def sanitize_text(text):
    decoded = str(text.upper().replace("\n", "_"))
    out = ""
    for i in range(0, len(decoded)):
        char = decoded[i]
            
        #remap unicode
        if char in CHARACTER_CONVERION_TABLE:
            char = CHARACTER_CONVERION_TABLE[char]
            


        #check if is part of the alphabet
        if char in BASE_ALPHABET:
            out += char
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


def get_bygrams(text):
    text = sanitize_text(text)
    
    out = []

    for i in range(0, len(text) - 1):
        out.append(text[i] + text[i+1])

    return out


def create_bygram_matrix(bygrams):
    out = {}

    for i in BASE_ALPHABET:
        for j in BASE_ALPHABET:
            out[i + j] = 0

    
    for bygram in bygrams:
        out[bygram] += 1

    for key in out.keys():
        if out[key] == 0:
            out[key] = 1

    return out

def make_matrix_relative(matrix):
    total_element_count = 0
    for key in matrix.keys():        
        total_element_count += matrix[key] - 1
    for key in matrix.keys():
        matrix[key] /= total_element_count



    return matrix


def plausability(text, relative_matrix):
    text_matrix = create_bygram_matrix(get_bygrams(text))

    outcome = 0
    for i in BASE_ALPHABET:
        for j in BASE_ALPHABET:
            outcome += math.log(relative_matrix[i + j]) * text_matrix[i + j]

    return outcome


def text_correctness(original_text, decrypted_text):
    output = 0
    
    for i in range(0, len(original_text)):
        if original_text[i] != decrypted_text[i]:
            output += 1

    output /= len(original_text)

    return 1 - output