import random
from cipher.cipher_util import decrypt, generate_random_key, plausability, shuffle_key


IGNORE_CHANCE = 0.01

def break_encryption(text, probability_matrix, attempts):
    
    key = generate_random_key()



    best_key = key.copy()
    best_score = plausability(decrypt(best_key, text), probability_matrix)


    
    for iteration in range(0, attempts):
        
        new_key = shuffle_key(key.copy())

        score = plausability(decrypt(new_key, text), probability_matrix)

        if score > best_score:
            best_key = new_key
            best_score = score
            key = new_key
        elif random.uniform(0, 1) < IGNORE_CHANCE:
            key = new_key

        if iteration % 100 == 0:
            print(f"decrypt progress {iteration}, score {best_score}")
    
    return best_key


