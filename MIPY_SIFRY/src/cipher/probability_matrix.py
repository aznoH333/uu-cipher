from cipher.cipher_util import CipherUtil


class ProbabilityMatrix:
    _CHARACTER_DECODE = {
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
    def __init__(self):
        self.probabilities = {}
        self._total_occurence_count = 0


        # TODO : rename files
        # TODO : move constants to separate file
        # TODO : save / load from file

        # init probabilities
        for char in CipherUtil.DEFAULT_KEY:
            for followingChar in CipherUtil.DEFAULT_KEY:
                self.probabilities[char + followingChar] = 1



    def fromText(text):
        editedText = ProbabilityMatrix._filterText(text)

        this = ProbabilityMatrix()
        
        # create absolute matrix
        for i in range(0, len(editedText) - 1):
            this._noteOccurence(editedText[i], editedText[i + 1])

        # convert to relative matrix
        for char in CipherUtil.DEFAULT_KEY:
            for followingChar in CipherUtil.DEFAULT_KEY:
                this.probabilities[char + followingChar] /= this._total_occurence_count

        return this
            
    
    def _noteOccurence(self, character, following_character):
        self._total_occurence_count += 1
        self.probabilities[character + following_character] += 1

    def saveToFile(self, target):
        content = str(self.probabilities.__dict__)

        with open(target, "w") as f:
            f.write(content)


    def _filterText(text):
        decoded = str(text.upper().replace("\n", ""))
        out = ""
        pushedSpaceLast = False
        for i in range(0, len(decoded)):
            char = decoded[i]
            
            #remap unicode
            if char in ProbabilityMatrix._CHARACTER_DECODE:
                char = ProbabilityMatrix._CHARACTER_DECODE[char]
            
            
            #dont include duplicate spaces
            if char == '_' and pushedSpaceLast:
                continue

            #check if is part of the alphabet
            if char in CipherUtil.DEFAULT_KEY:
                out += char
                pushedSpaceLast = (char == '_')
                continue

            


        return out
