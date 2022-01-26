"""
Lenguaje de los tokens. Estan escritos en orden de prioridad
"""

regex = {}

regex['spaces'] = "[ \t\r\f\v\n]*"

regex['AND'] = 'AND'
regex['OR'] = 'OR'
regex['NOT'] = 'NOT'
regex['TEAM'] = 'TEAM'
regex['player'] = 'player'
regex['team'] = 'team'
regex['manager'] = 'manager'
regex['referee'] = 'referee'
regex['game'] = 'game'
regex['for'] = 'for'
regex['in'] = 'in'
regex['filter'] = 'filter'
regex['by'] = 'by'
regex['if'] = 'if'
regex['elif'] = 'elif'
regex['else'] = 'else'
regex['function'] = 'function'

regex[','] = '[,]'
regex[';'] = '[;]'
regex['.'] = '[.]'
regex[':'] = '[:]'

regex['('] = '[(]'
regex[')'] = '[)]'
regex['{'] = '[{]'
regex['}'] = '[}]'
regex['['] = '[[]'
regex[']'] = '[]]'

regex['='] = '[=]'

regex['+'] = '[+]'
regex['-'] = '[-]'
regex['*'] = '[*]'
regex['/'] = '[/]'
regex['%'] = '[%]'
regex['<'] = '[<]'
regex['>'] = '[>]'
regex['<='] = '[<=]'
regex['>='] = '[>=]'
regex['=='] = '[==]'
regex['!='] = '[!=]'

regex['_'] = '[_]'
regex['#'] = '[#]'
regex['/#'] = '[/#]'
regex['#/'] = '[#/]' 

regex['id'] = '([_]|[a-zA-Z])([_]|[a-zA-Z0-9])*'
regex['num'] = '[1-9][0-9]*(.[0-9]+)?'
regex['string'] = '"[!#-~]*"'