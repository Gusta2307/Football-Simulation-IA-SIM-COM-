from enum import Enum, auto

class Token:
    def __init__(self, text, tokenType, line=0, column=0) -> None:
        self.text = text
        self.tokenType = tokenType
        self.line = line
        self.column = column
    
    def __str__(self):
        return str((self.tokenType,
                    self.text,
                    "line: "+str(self.line),
                    "column: "+str(self.column)))
    
    def __repr__(self):
        return str(self)