"""
Lenguaje de los tokens
"""

from compilacion.analisis_lexico.token import TokenType


regex = {}

regex['spaces'] = "[ \t\r\f\v\n]*"
regex[TokenType.Identifier] = '([_]|[a-zA-Z])([_]|[a-zA-Z0-9])*'
regex[TokenType.Number] = '[1-9][0-9]*(.[0-9]+)?'
regex[TokenType.Text] = '"[[:print:]-["]]*"' # Buscar bien la def del regex de un string
regex[TokenType.OpenBracket] = '[(]'
regex[TokenType.ClosedBracket] = '[)]'
regex[TokenType.OpenCurlyBraces] = '[{]'
regex[TokenType.ClosedCurlyBraces] = '[}]'
regex[TokenType.OpenSquareBracket] = '[[]'
regex[TokenType.ClosedSquareBracket] = '[]]'

regex[TokenType.Assign] = '[=]'
regex[TokenType.ValueSeparator] = '[,]'
regex[TokenType.PointSeparator] = '[.]'
regex[TokenType.StatementSeparator] = '[;]'
regex[TokenType.DoblePointSeparator] = '[:]'

regex[TokenType.Multiply] = '[_]'
regex[TokenType.Divide] = '[#]'

regex[TokenType.Add] = '[+]'
regex[TokenType.Subtract] = '[-]'
regex[TokenType.Multiply] = '[*]'
regex[TokenType.Divide] = '[/]'
regex[TokenType.Add] = '[%]'
regex[TokenType.Less] = '[<]'
regex[TokenType.Greater] = '[>]'
regex[TokenType.LessOrEquals] = '[<=]'
regex[TokenType.GreaterOrEquals] = '[>=]'
regex[TokenType.Equals] = '[==]'
regex[TokenType.NotEquals] = '[!=]'

regex[TokenType.And] = 'AND'
regex[TokenType.Or] = 'OR'
regex[TokenType.Not] = 'NOT'
regex[TokenType.TEAM] = 'TEAM'
regex[TokenType.Player] = 'player'
regex[TokenType.Team] = 'team'
regex[TokenType.Manager] = 'manager'
regex[TokenType.Referee] = 'referee'
regex[TokenType.Game] = 'game'
regex[TokenType.ForClausule] = 'for'
regex[TokenType.InClausule] = 'in'
regex[TokenType.Filter] = 'filter'
regex[TokenType.ByClausule] = 'by'
regex[TokenType.IfClausule] = 'if'
regex[TokenType.ElifClausule] = 'elif'
regex[TokenType.ElseClausule] = 'else'
regex[TokenType.Function] = 'function'