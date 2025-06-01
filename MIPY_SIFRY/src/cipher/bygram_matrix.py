import math
from cipher.cipher_util import BASE_ALPHABET, sanitize_text


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