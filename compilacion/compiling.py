from compilacion.analisisLexico import *


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
        self.__lexical.registerKeyword("AND", TokenValue.And)
        self.__lexical.registerKeyword("OR", TokenValue.Or)
        self.__lexical.registerKeyword("NOT", TokenValue.Not)
        self.__lexical.registerKeyword("and", TokenValue.And)
        self.__lexical.registerKeyword("or", TokenValue.Or)
        self.__lexical.registerKeyword("not", TokenValue.Not)

        self.__lexical.registerSymbol("<", TokenValue.Less)
        self.__lexical.registerSymbol("<=", TokenValue.LessOrEquals)
        self.__lexical.registerSymbol(">", TokenValue.Greater)
        self.__lexical.registerSymbol(">=", TokenValue.GreaterOrEquals)
        self.__lexical.registerSymbol("==", TokenValue.Equals)
        self.__lexical.registerSymbol("!=", TokenValue.NotEquals)
        self.__lexical.registerSymbol("<-", TokenValue.Assign)
        self.__lexical.registerSymbol("_", TokenValue.Underscore)
        self.__lexical.registerSymbol("(", TokenValue.OpenBracket)
        self.__lexical.registerSymbol(")", TokenValue.ClosedBracket)
        self.__lexical.registerSymbol("{", TokenValue.OpenCurlyBraces)
        self.__lexical.registerSymbol("}", TokenValue.ClosedCurlyBraces)
        self.__lexical.registerSymbol("[", TokenValue.OpenSquareBracket)
        self.__lexical.registerSymbol("[", TokenValue.ClosedSquareBracket)
        self.__lexical.registerSymbol('"', TokenValue.QuotationMarks)
        self.__lexical.registerSymbol("=", TokenValue.Equal)
        self.__lexical.registerSymbol("!", TokenValue.PuntuactionMark)
        self.__lexical.registerSymbol("-", TokenValue.Hypen)

        self.__lexical.registerSeparator(".", TokenValue.PointSeparator)
        self.__lexical.registerSeparator(":", TokenValue.DoblePointSeparator)
        self.__lexical.registerSeparator(",", TokenValue.ValueSeparator)
        self.__lexical.registerSeparator(";", TokenValue.StatementSeparator)
        return self.__lexical