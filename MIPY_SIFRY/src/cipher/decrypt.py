import random
from cipher.cipher_util import decrypt, generate_random_key, plausability, shuffle_key


IGNORE_CHANCE = 0.0001

def break_encryption(text, probability_matrix, attempts):
    
    key = generate_random_key()



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



        if score > current_score or random.uniform(0.0, 1.0) < (IGNORE_CHANCE * attempts_without_improvement):
            current_key = new_key
            current_score = score
            key = new_key
            attempts_without_improvement = 0
        else:
            attempts_without_improvement+=1

        if iteration % 100 == 0:
            print(f"decrypt progress {iteration}, score {best_score}, key {best_key}")
    
    return best_key


