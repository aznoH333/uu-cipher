

from cipher.cipher_util import BASE_ALPHABET, sanitize_text


class ProbabilityMatrix:
    
    def __init__(self):
        self.probabilities = {}
        self._total_occurence_count = 0


        # TODO : rename files
        # TODO : move constants to separate file
        # TODO : save / load from file

        # init probabilities
        for char in BASE_ALPHABET:
            for followingChar in BASE_ALPHABET:
                self.probabilities[char + followingChar] = 1



    def from_text(text, include_duplicate_spaces):
        editedText = sanitize_text(text, include_duplicate_spaces)

        this = ProbabilityMatrix()
        
        # create absolute matrix
        for i in range(0, len(editedText) - 1):
            this._note_occurence(editedText[i], editedText[i + 1])

        # convert to relative matrix
        for char in BASE_ALPHABET:
            for followingChar in BASE_ALPHABET:
                this.probabilities[char + followingChar] /= this._total_occurence_count + (len(BASE_ALPHABET) * len(BASE_ALPHABET))

        return this


    
    

    def save_to_file(self, target):
        content = str(self.probabilities.__dict__)

        with open(target, "w") as f:
            f.write(content)

    def _note_occurence(self, character, following_character):
        self._total_occurence_count += 1
        self.probabilities[character + following_character] += 1

    
    
    def calculate_text_score(self, text):
        out = 0
        for i in range(0, len(text) - 1):
            index = text[i] + text[i+1]
            out += self.probabilities[index]
            # + LOG( TM_ref[i][j] ) * TM_obs[i][j]

        
        return out
    
