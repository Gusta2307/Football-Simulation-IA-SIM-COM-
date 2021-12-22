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
    Quote = auto(),
    Bracket = auto(),

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
    And = auto(),
    Or = auto(),
    Not = auto(),

    #Symbols
    Less = auto(),            # <
    LessOrEquals = auto(),    # <=
    Greater = auto(),         # >
    GreaterOrEquals = auto(), # >=
    Equals = auto(),          # ==
    NotEquals = auto(),       # !=
    Equal = auto(),           # =
    PuntuactionMark = auto(), # !
    Hashtag = auto(),
    Assign = auto(),               # <-
    Underscore = auto(),           # _
    Hypen = auto()                 # -
    
    #Separators
    DoblePointSeparator = auto(),  # :
    ValueSeparator = auto(),       # ,
    StatementSeparator = auto(),   # ;
    PointSeparator = auto(),       # .

    #Brackets
    OpenBracket = auto(),          # (
    ClosedBracket = auto(),        # )
    OpenCurlyBraces = auto(),      # {
    ClosedCurlyBraces = auto(),    # }
    OpenSquareBracket = auto(),    # [
    ClosedSquareBracket = auto(),  # ]
    
    #Quotes
    QuotationMarks = auto(),       # "