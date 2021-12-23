from compilacion.analisisLexico import *


class Compiling:
    def __init__(self) -> None:
        self.__lexical = AnalisisLexico()

    @property
    def Lexical(self) -> AnalisisLexico:
        #KEYWORDS
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

        #SYMBOLS
        self.__lexical.registerSymbol("<", TokenValue.Less)
        self.__lexical.registerSymbol("<=", TokenValue.LessOrEquals)
        self.__lexical.registerSymbol(">", TokenValue.Greater)
        self.__lexical.registerSymbol(">=", TokenValue.GreaterOrEquals)
        self.__lexical.registerSymbol("==", TokenValue.Equals)
        self.__lexical.registerSymbol("!=", TokenValue.NotEquals)
        self.__lexical.registerSymbol("_", TokenValue.Underscore)
        self.__lexical.registerSymbol("=", TokenValue.Assign)
        self.__lexical.registerSymbol("!", TokenValue.PuntuactionMark)
        self.__lexical.registerSymbol("#", TokenValue.Hashtag)
        # self.__lexical.registerSymbol("-", TokenValue.Hypen)
        # self.__lexical.registerSymbol("<-", TokenValue.Assign)

        #OPERATORS
        self.__lexical.registerOperator("+", TokenValue.Add) 
        self.__lexical.registerOperator("-", TokenValue.Subtract)
        self.__lexical.registerOperator("*", TokenValue.Multiply)
        self.__lexical.registerOperator("/", TokenValue.Divide)
        self.__lexical.registerOperator("%", TokenValue.Modulus)
        
        #BRACKET
        self.__lexical.registerBracket("(", TokenValue.OpenBracket)
        self.__lexical.registerBracket(")", TokenValue.ClosedBracket)
        self.__lexical.registerBracket("{", TokenValue.OpenCurlyBraces)
        self.__lexical.registerBracket("}", TokenValue.ClosedCurlyBraces)
        self.__lexical.registerBracket("[", TokenValue.OpenSquareBracket)
        self.__lexical.registerBracket("]", TokenValue.ClosedSquareBracket)

        #SEPARATOR
        self.__lexical.registerSeparator(".", TokenValue.PointSeparator)
        self.__lexical.registerSeparator(":", TokenValue.DoblePointSeparator)
        self.__lexical.registerSeparator(",", TokenValue.ValueSeparator)
        self.__lexical.registerSeparator(";", TokenValue.StatementSeparator)

        self.__lexical.registerQuote('"', TokenValue.QuotationMarks)
        return self.__lexical