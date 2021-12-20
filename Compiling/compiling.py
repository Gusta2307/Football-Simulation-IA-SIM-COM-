from Compiling.token import TokenValue
from Compiling.analisisLexico import AnalisisLexico


class Compiling:
    def __init__(self) -> None:
        self.__lexical = AnalisisLexico()

    @property
    def Lexical(self) -> AnalisisLexico:
        self.__lexical.registerKeyword("player", TokenValue.Player)
        self.__lexical.registerKeyword("team", TokenValue.Team)
        self.__lexical.registerKeyword("game", TokenValue.Game)
        self.__lexical.registerKeyword("manager", TokenValue.Manager)
        self.__lexical.registerKeyword("referee", TokenValue.Referee)
        self.__lexical.registerKeyword("for", TokenValue.ForClausule)
        self.__lexical.registerKeyword("in", TokenValue.InClausule)
        self.__lexical.registerKeyword("if", TokenValue.IfClausule)
        self.__lexical.registerKeyword("else", TokenValue.ElseClausule)
        self.__lexical.registerKeyword("filter", TokenValue.Filter)
        self.__lexical.registerKeyword("by", TokenValue.ByClausule)
        self.__lexical.registerKeyword("function", TokenValue.Function)
        self.__lexical.registerKeyword("const", TokenValue.Const)
        self.__lexical.registerKeyword("TEAM", TokenValue.TEAM)

        self.__lexical.registerSymbol("<", TokenValue.Less)
        self.__lexical.registerSymbol("<=", TokenValue.LessOrEquals)
        self.__lexical.registerSymbol(">", TokenValue.Greater)
        self.__lexical.registerSymbol(">=", TokenValue.GreaterOrEquals)
        self.__lexical.registerSymbol("==", TokenValue.Equals)
        self.__lexical.registerSymbol("!=", TokenValue.NotEquals)
        self.__lexical.registerSymbol("AND", TokenValue.And)
        self.__lexical.registerSymbol("OR", TokenValue.Or)
        self.__lexical.registerSymbol("NOT", TokenValue.Not)
        self.__lexical.registerSymbol("<-", TokenValue.Assign)
        self.__lexical.registerSymbol("_", TokenValue.Underscore)
        self.__lexical.registerSymbol(".", TokenValue.PointSeparator)
        self.__lexical.registerSymbol(":", TokenValue.DoblePointSeparator)
        self.__lexical.registerSymbol(",", TokenValue.ValueSeparator)
        self.__lexical.registerSymbol(";", TokenValue.StatementSeparator)
        self.__lexical.registerSymbol("(", TokenValue.OpenBracket)
        self.__lexical.registerSymbol(")", TokenValue.ClosedBracket)
        self.__lexical.registerSymbol("{", TokenValue.OpenCurlyBraces)
        self.__lexical.registerSymbol("}", TokenValue.ClosedCurlyBraces)
        self.__lexical.registerSymbol("[", TokenValue.OpenSquareBracket)
        self.__lexical.registerSymbol("[", TokenValue.ClosedSquareBracket)
        return self.__lexical