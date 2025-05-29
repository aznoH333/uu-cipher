class CipherUtil:
    
    
    DEFAULT_KEY = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "_"]
    
    def __init__ (self, key):
        self.setKey(key)
    
    def setKey(self, newKey):
        self.key = list(newKey.upper())


    def encrypt(self, text):
        out = ""
        for char in text.upper():
            out += self.key[self.DEFAULT_KEY.index(char)]
        
        return out

    def decrypt(self, text):
        out = ""
        for char in text.upper():
            out += self.DEFAULT_KEY[self.key.index(char)]
        
        return out
