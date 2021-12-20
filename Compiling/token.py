from enum import Enum, auto


class Token:
    def __init__(self, text, tokenValue, tokenType, line, column) -> None:
        self.text = text
        self.tokenValue = tokenValue 
        self.tokenType = tokenType
        self.line = line
        self.column = column
    
    def __str__(self) -> str:
        return self.text + " " + str(self.tokenType) + f"[{self.tokenValue}]"

    def __eq__(self, token: object) -> bool:
        return self.tokenValue == self.tokenValue


class TokenType(Enum):
    Keyword = 1,
    Identifier = 2,
    Number = 3,
    Symbol = 4


class TokenValue(Enum):

    #Keywords
    Player = 0,
    Team = 1,
    Game = 2,
    Manager = 3,
    Referee = 4,
    ForClausule = 5,  # for
    InClausule = 6,   # in
    IfClausule = 7,   # if
    ElseClausule = 8, # else
    Filter = 9,
    ByClausule = 10,  # by
    Function = 11,
    Const = 12,
    TEAM = 13,

    #Operators
    Less = 14,            # <
    LessOrEquals = 15,    # <=
    Greater = 16,         # >
    GreaterOrEquals = 17, # >=
    Equals = 18,          # ==
    NotEquals = 19,       # !=
    And = 20,
    Or = 21,
    Not = 22,

    #Symbols
    Assign = 23,               # <-
    Underscore = 24,           # _
    DoblePointSeparator = 25,  # :
    ValueSeparator = 26,       # ,
    StatementSeparator = 27,   # ;
    OpenBracket = 28,          # (
    ClosedBracket = 29,        # )
    OpenCurlyBraces = 30,      # {
    ClosedCurlyBraces = 31,    # }
    OpenSquareBracket = 32,    # [
    ClosedSquareBracket = 33,  # ]
    PointSeparator = 34,       # .