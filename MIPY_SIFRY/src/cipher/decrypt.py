from cipher.cipher_util import decrypt, generate_random_key, sanitize_text, shuffle_key
import random

IGNORE_CHANCE = 0.01

def break_encryption(text, probability_matrix, attempts):
    text = sanitize_text(text, True)
    
    key = generate_random_key()

    best_key = key.copy()

    
    best_score = probability_matrix.calculate_text_score(decrypt(key, text))


    for iteration in range(0, attempts):
        
        # iterate key
        new_key = shuffle_key(key.copy())
        
        decrypted = decrypt(new_key, text)

        score = probability_matrix.calculate_text_score(decrypted)

        if score > best_score:
            best_key = key.copy()
            best_score = score

            if random.uniform(0.0, 1.0) > IGNORE_CHANCE:
                key = new_key

    return best_key


