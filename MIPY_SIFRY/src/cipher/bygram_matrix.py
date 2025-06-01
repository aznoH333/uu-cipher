import math
from cipher.cipher_util import BASE_ALPHABET, sanitize_text


def get_bygrams(text: str) -> list:
    """
    Extracts bygrams from the given text and returns them as a list.

    A bygram is a pair of consecutive characters in the text. This function 
    first sanitizes the input text to ensure it contains only valid characters 
    from the BASE_ALPHABET. It then iterates through the sanitized text, 
    creating bygrams by combining each character with the next one.

    Parameters:
        text (str): The input text from which bygrams will be extracted.

    Returns:
        list: A list of bygrams (two-character strings) derived from the input text.
    """
    text = sanitize_text(text)
    
    out = []

    for i in range(0, len(text) - 1):
        out.append(text[i] + text[i+1])

    return out


def create_bygram_matrix(bygrams: list) -> dict:
    """
    Constructs a bygram frequency matrix from a list of bygrams.

    This function initializes a matrix (dictionary) where each key is a 
    possible bygram formed from the characters in BASE_ALPHABET. The values 
    represent the count of occurrences of each bygram in the provided list. 
    If a bygram appears 0 times, its value is set to 1 to prevent errors 
    during logarithmic calculations.

    Parameters:
        bygrams (list): A list of bygrams for which the frequency matrix will be created.

    Returns:
        dict: A dictionary representing the bygram matrix, with bygrams as keys and their 
              occurrence counts as values.
    """
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

def make_matrix_relative(matrix: dict) -> dict:
    """
    Normalizes the values in a bygram matrix to create a relative frequency matrix.

    This function divides each value in the input matrix by the total sum of 
    all values in the matrix. The resulting matrix will have values that sum 
    to 1, representing the relative frequency of each bygram.

    Parameters:
        matrix (dict): A dictionary representing the bygram matrix with counts.

    Returns:
        dict: A normalized matrix where each value represents the relative frequency 
              of the corresponding bygram, summing to 1.
    """
    total_element_count = 0
    for key in matrix.keys():        
        total_element_count += matrix[key] - 1
    for key in matrix.keys():
        matrix[key] /= total_element_count



    return matrix


def plausability(text: str, relative_matrix: dict) -> float:
    """
    Calculates the plausibility score of the given text based on a relative bygram matrix.

    This function evaluates how plausible the input text is by comparing its 
    bygram distribution to the provided relative matrix. A higher score indicates 
    that the text is more plausible according to the statistical model represented 
    by the matrix.

    Parameters:
        text (str): The input text for which the plausibility score will be calculated.
        relative_matrix (dict): A dictionary representing the relative bygram matrix.

    Returns:
        float: A plausibility score, where higher values indicate greater plausibility 
               of the text based on the bygram distribution.
    """
    
    text_matrix = create_bygram_matrix(get_bygrams(text))

    outcome = 0
    for i in BASE_ALPHABET:
        for j in BASE_ALPHABET:
            outcome += math.log(relative_matrix[i + j]) * text_matrix[i + j]

    return outcome