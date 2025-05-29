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
        pass

    def fromText(text):
        editedText = ProbabilityMatrix._filterText(text)
        print(editedText)
        """
        this = ProbabilityMatrix()
        
        for i in range(0, len(editedText) - 1):
            this._noteOccurence(editedText[i], editedText[i + 1])

        return this"""
            
    
    def _noteOccurence(self, character, followingCharacter):
        if self.probabilities[character] == None:
            self.probabilities[character] = []
        
        self.probabilities[character].append(character)

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
            if char == "_" and pushedSpaceLast:
                continue

            #check if is part of the alphabet
            if char in CipherUtil.DEFAULT_KEY:
                out += char
                pushedSpaceLast = out == "_"
                continue

            


        return out
