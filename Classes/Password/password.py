import random
import string

class Password:
    def __init__(self):
        self.symbols = ["!", "%", "_", "+", "-", ":", "?", "="]
    
    def letter(self, upper=None):
        if upper:
            return random.choice(string.ascii_uppercase)
        return random.choice(string.ascii_lowercase)
    
    def symbol(self):
        return random.choice(self.symbols)
    
    def number(self):
        return random.randint(0, 9)
    
    def password(self, length):
        if length < 10:
            raise(Exception)
        
        ret = ""

        # Starts with letter and must contain one upper and one lower
        ret += self.letter() if (random.randint(1, 2) == 1) else self.letter(True)
        ret += self.letter() if ret[0].isupper() else self.letter(True)

        for _ in range(length-5):
            match random.randint(1, 4):
                case 1:
                    ret += self.symbol()
                case 2:
                    ret += str(self.number())
                case 3:
                    ret += self.letter()
                case 4:
                    ret += self.letter(True)
    
        # Must contain 2 numbers and at least one symbol
        match random.randint(1, 3):
            case 1:
                ret += str(str(self.number())) + str(self.number()) + self.symbol()
            case 2:
                ret += str(self.number()) + self.symbol() + str(self.number())
            case 3:
                ret += self.symbol() + str(self.number()) + str(self.number())
        
        return ret
