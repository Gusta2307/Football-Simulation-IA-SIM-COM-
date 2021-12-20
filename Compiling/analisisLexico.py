
class AnalisisLexico:
    def __init__(self) -> None:
        self.keywords = {}
        self.symbols = {}
    
    def registerKeyword(self, text, value):
        self.keywords[text] = value
    
    def registerSymbol(self, text, value):
        self.keywords[text] = value

    def tokenize(code):
        pass