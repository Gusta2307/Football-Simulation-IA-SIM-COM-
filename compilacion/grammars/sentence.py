
class Sentence:
    def __init__(self, *args) -> None:
        self.symbols = [x for x in args]  # secuencia de terminales y no-terminales

    def getIndex(self, item) -> int:
        pos = -1
        for i in range(len(self.symbols)):
            if str(self.symbols[i]) == str(item):
                pos = i
        return pos
    
    def __str__(self):
        string = ""
        for i in range(len(self.symbols)):
            string += str(self.symbols[i])
            if i != len(self.symbols) - 1:
                string += " "
        return string
    
    def __repr__(self) -> str:
        return str(self)
