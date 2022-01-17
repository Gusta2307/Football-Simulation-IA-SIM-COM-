from enum import Enum, auto

class Token:
    def __init__(self, text, tokenType, line=0, column=0) -> None:
        self.text = text
        self.tokenType = tokenType
        self.line = line
        self.column = column
    
    def __str__(self) -> str:
        return self.text + " " + str(self.tokenType.name)


class TokenType(Enum):
    Keyword = auto(),
    Identifier = auto(),
    Number = auto(),
    Symbol = auto(),
    Text = auto(),
    Separator = auto(),
    Quote = auto(),
    Bracket = auto(),
    Operator = auto(),
    Assign = auto(),
    EOF = auto(),