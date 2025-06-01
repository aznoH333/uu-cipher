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





def sanitize_text(text: str) -> str:
    """
    Cleans and prepares a given text for encryption or decryption.

    This function processes the input text to ensure that it contains only 
    characters from the defined BASE_ALPHABET. It converts all characters to 
    uppercase and replaces newline characters with underscores (to avoid accidental word merging). 
    Any characters not found in the BASE_ALPHABET are either converted using the 
    CHARACTER_CONVERSION_TABLE or discarded if they cannot be converted.

    Parameters:
        text (str): The input text that needs to be sanitized. This can include 
                    any characters, including special characters and whitespace.

    Returns:
        str: A sanitized string containing only characters from BASE_ALPHABET. 
             All characters are uppercase, and any unrecognized characters are 
             removed. Newline characters are replaced with underscores.
    """
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


def generate_random_key() -> list:
    """
    Generates a randomized permutation of the base alphabet.

    This function creates a new list containing a shuffled version of the 
    characters defined in BASE_ALPHABET. The resulting list can be used as 
    a key for encryption or decryption processes.

    Returns:
        list: A list containing a randomized iteration of the characters 
              from BASE_ALPHABET. The order of characters in the list is 
              shuffled, providing a unique key for encryption or decryption.
    """
    output = []

    for char in BASE_ALPHABET:
        output.append(char)

    random.shuffle(output)

    return output

def shuffle_key(key: list) -> list:
    """
    Swaps two random letters in a given key.

    This function takes a list representing a key (a randomized permutation 
    of the base alphabet) and randomly selects two distinct positions within 
    the list. It then swaps the characters at these positions.

    Parameters:
        key (list): A list of characters representing the key to be shuffled. 
                    The list should contain characters from BASE_ALPHABET.

    Returns:
        list: The modified key with two characters swapped. The original 
              key is altered in place and returned.
    """
    random_1 = randrange(0, len(BASE_ALPHABET))
    random_2 = randrange(0, len(BASE_ALPHABET) - 1)

    if random_2 >= random_1:
        random_2 += 1

    temp = key[random_1]

    key[random_1] = key[random_2]
    key[random_2] = temp

    return key



def text_correctness(original_text: str, decrypted_text: str) -> float:
    """
    Compares two texts and returns a "correctness" score based on character differences.

    This function evaluates how closely the decrypted text matches the 
    original text by counting the number of differing characters. The 
    result is expressed as a percentage, where a score of 1 indicates 
    perfect correctness (no differences) and a score of 0 indicates 
    complete divergence (all characters differ). This function is primarily 
    intended for testing purposes to assess the accuracy of the decryption 
    process.

    Parameters:
        original_text (str): The original text that serves as the reference for comparison.
        decrypted_text (str): The text produced by the decryption process that is being evaluated.

    Returns:
        float: A correctness score ranging from 0 to 1, where 1 indicates 
               that the texts are identical and 0 indicates that they are completely different.
    """
    output = 0
    
    for i in range(0, len(original_text)):
        if original_text[i] != decrypted_text[i]:
            output += 1

    output /= len(original_text)

    return 1 - output