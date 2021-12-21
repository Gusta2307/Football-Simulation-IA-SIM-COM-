from enum import Enum, auto

class Token:
    def __init__(self, text, tokenValue, tokenType, line, column) -> None:
        self.text = text
        self.tokenValue = tokenValue 
        self.tokenType = tokenType
        self.line = line
        self.column = column
    
    def __str__(self) -> str:
        return self.text + " " + str(self.tokenType.name) + f"[{self.tokenValue}]"

    def __eq__(self, token: object) -> bool:
        return self.tokenValue == token.tokenValue


class TokenType(Enum):
    Keyword = auto(),
    Identifier = auto(),
    Number = auto(),
    Symbol = auto(),
    Text = auto(),
    Separator = auto(),


class TokenValue(Enum):
    #Keywords
    Player = auto(),
    Team = auto(),
    Game = auto(),
    Manager = auto(),
    Referee = auto(),
    ForClausule = auto(),  # for
    InClausule = auto(),   # in
    IfClausule = auto(),   # if
    ElifClausule = auto(), # elif
    ElseClausule = auto(), # else
    Filter = auto(),
    ByClausule = auto(),  # by
    Function = auto(),
    Const = auto(),
    TEAM = auto(),

    #Operators
    Less = auto(),            # <
    LessOrEquals = auto(),    # <=
    Greater = auto(),         # >
    GreaterOrEquals = auto(), # >=
    Equals = auto(),          # ==
    NotEquals = auto(),       # !=
    Equal = auto(),           # =
    PuntuactionMark = auto(), # !

    # CREO Q ESTO TAMBIEN SERIA KEYWORD
    And = auto(),
    Or = auto(),
    Not = auto(),

    #Symbols
    Assign = auto(),               # <-
    Underscore = auto(),           # _
    Hypen = auto()                 # -
    DoblePointSeparator = auto(),  # :
    ValueSeparator = auto(),       # ,
    StatementSeparator = auto(),   # ;
    OpenBracket = auto(),          # (
    ClosedBracket = auto(),        # )
    OpenCurlyBraces = auto(),      # {
    ClosedCurlyBraces = auto(),    # }
    OpenSquareBracket = auto(),    # [
    ClosedSquareBracket = auto(),  # ]
    PointSeparator = auto(),       # .
    QuotationMarks = auto(),       # "