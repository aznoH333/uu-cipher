

import math
from cipher.cipher_util import BASE_ALPHABET, sanitize_text


class ProbabilityMatrix:
    
    def __init__(self):
        self.probabilities = {}
        self._total_occurence_count = 0
        
        # init probabilities
        for char in BASE_ALPHABET:
            for followingChar in BASE_ALPHABET:
                self.probabilities[char + followingChar] = 0



    def from_text(text):
        editedText = sanitize_text(text)

        this = ProbabilityMatrix()
        
        # create absolute matrix
        for i in range(0, len(editedText) - 1):
            this._note_occurence(editedText[i], editedText[i + 1])
        

        for key in this.probabilities.keys():
            if this.probabilities[key] == 0:
                this.probabilities[key] = 1
                this._total_occurence_count += 1


        # convert to relative matrix
        #for char in BASE_ALPHABET:
        #    for followingChar in BASE_ALPHABET:
        #        this.probabilities[char + followingChar] /= this._total_occurence_count

        return this


    
    

    def save_to_file(self, target):
        content = str(self.probabilities.__dict__)

        with open(target, "w") as f:
            f.write(content)

    def _note_occurence(self, character, following_character):
        self._total_occurence_count += 1
        self.probabilities[character + following_character] += 1

    
    

    

def plausability(text, probability_matrix):
    original_matrix = ProbabilityMatrix.from_text(text)

    output = 0

    for i in BASE_ALPHABET:
        for j in BASE_ALPHABET:
            key = i + j
            output += math.log(probability_matrix.probabilities[key]) * original_matrix.probabilities[key]
    
    return output