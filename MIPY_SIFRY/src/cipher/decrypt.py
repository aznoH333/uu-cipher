from cipher.cipher_util import decrypt, generate_random_key, sanitize_text, shuffle_key
import random

from cipher.probability_matrix import plausability

RANDOM_ACCEPT_CHANCE = 0.01

def break_encryption(text, probability_matrix, attempts):
    text = sanitize_text(text)
    
    key = generate_random_key()

    best_key = key.copy()

    
    best_score = plausability(decrypt(key, text), probability_matrix)


    for iteration in range(0, attempts):
        
        # iterate key
        new_key = shuffle_key(key.copy())
        
        decrypted = decrypt(new_key, text)

        score = plausability(decrypted, probability_matrix)

        if score > best_score:
            best_key = key.copy()
            best_score = score
            key = new_key

        if random.uniform(0.0, 1.0) < RANDOM_ACCEPT_CHANCE:
            key = new_key


    return best_key


