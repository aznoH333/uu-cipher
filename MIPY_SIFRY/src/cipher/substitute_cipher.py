import random

from cipher.bygram_matrix import plausability
from cipher.cipher_util import BASE_ALPHABET, generate_random_key, shuffle_key


MUTATE_CHANCE = 0.0001

def encrypt(key: list, text: str) -> str:
    """
    Encrypts the given text using a substitution cipher.

    This function takes a plaintext input and encrypts it by substituting each 
    character with its corresponding character from the provided key, which is 
    a randomized iteration of the BASE_ALPHABET. The input text is first 
    converted to uppercase to ensure consistency. The resulting encrypted text 
    is returned as a string.

    Parameters:
        key (list): A list representing the substitution key, where each character 
                    corresponds to a character in BASE_ALPHABET.
        text (str): The plaintext input that needs to be encrypted.

    Returns:
        str: The encrypted text, where each character has been substituted according 
             to the provided key.
    """
    out = ""
    for char in text.upper():
        out += key[BASE_ALPHABET.index(char)]
        
    return out

def decrypt(key: list, text: str) -> str:
    """
    Decrypts the given text using a substitution cipher.

    This function takes an encrypted text and decrypts it by substituting each 
    character back to its original form using the provided key, which is a 
    randomized iteration of the BASE_ALPHABET. The input text is first converted 
    to uppercase to ensure consistency. The resulting decrypted text is returned 
    as a string.

    Parameters:
        key (list): A list representing the substitution key, where each character 
                    corresponds to a character in BASE_ALPHABET.
        text (str): The encrypted input that needs to be decrypted.

    Returns:
        str: The decrypted text, where each character has been restored to its 
             original form according to the provided key.
    """
    out = ""
    for char in text.upper():
        out += BASE_ALPHABET[key.index(char)]
        
    return out


def break_encryption(text: str, probability_matrix: dict, attempts: int) -> list:
    """
    Attempts to find the decryption key for a given encrypted text using the Metropolis-Hastings algorithm.

    This function employs a probabilistic approach to decrypt an encrypted text by 
    iteratively searching for the best-performing key. It utilizes a probability bygram matrix 
    to evaluate the performance of each key based on the plausibility of the decrypted text. 
    The algorithm generates new keys by shuffling the current key and accepts or rejects 
    these keys based on their performance scores.

    Parameters:
        text (str): The encrypted text for which the decryption key is to be found.
        probability_matrix (dict): A matrix representing the probabilities of bygrams, 
                                   used to assess the plausibility of decrypted text.
        attempts (int): The number of attempts to find a better key. More attempts 
                        increase the likelihood of finding an optimal key.

    Returns:
        list: The best-performing key found during the attempts, which is a randomized 
              iteration of BASE_ALPHABET that maximizes the plausibility of the decrypted text.
    """
    key = generate_random_key()

    """
    DEVELOPER NOTE: 
    I have made some minor adjustments to the suggested algorithim.
    1. The best overall key is stored and returned at the end instead of the current key.
    This is mentionied in the assignemt just not implemented in the pseudo code. It made sense to me so i implemented it.

    2. The chance to accept a worse key scales with the number of passed iterations without improvement.
    I made this change to make the algorithim more likely to explore new combinations.

    Do these changes improve the result? 
    
    idk ¯\_(ツ)_/¯. probably? maybe? 
    it seems that they do.
    
    I have tried to run this many times. Usually with 20000 attempts it gets to 100%, but I have had a few instances where it got to only 90%
    """

    current_key = key.copy()
    current_score = plausability(decrypt(current_key, text), probability_matrix)

    best_key = key.copy()
    best_score = plausability(decrypt(best_key, text), probability_matrix)
    
    attempts_without_improvement = 0

    
    for iteration in range(0, attempts):
        
        new_key = shuffle_key(key.copy())

        score = plausability(decrypt(new_key, text), probability_matrix)

        if score > best_score:
            best_key = new_key.copy()
            best_score = score



        if score > current_score or random.uniform(0.0, 1.0) < (MUTATE_CHANCE * attempts_without_improvement):
            
            current_key = new_key
            current_score = score
            key = new_key
            attempts_without_improvement = 0

        else:
            attempts_without_improvement+=1

        if iteration % 1000 == 0:
            print(f"decrypt progress {iteration}, score {best_score}, key {best_key}")
    
    return best_key


