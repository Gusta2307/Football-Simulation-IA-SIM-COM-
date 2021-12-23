from compilacion.analisis_lexico.token import *


class LexicalAnalizer:
    def __init__(self) -> None:
        self.keywords = {}
        self.symbols = {}
        self.separators = {}
        self.quotes = {}
        self.brackets = {}
        self.operators = {}
        self.errors = []  # guarda los errores durante la tokenizacion
    
    def registerKeyword(self, text, value):
        self.keywords[text] = value
    
    def registerSymbol(self, text, value):
        self.symbols[text] = value

    def registerSeparator(self, text, value):
        self.separators[text] = value  
    
    def registerQuote(self, text, value):
        self.quotes[text] = value
    
    def registerBracket(self, text, value):
        self.brackets[text] = value

    def registerOperator(self, text, value):
        self.operators[text] = value

    def tokenize(self, code):
        for i in range(len(code)):
            j = 0
            state = 0
            column = 1
            curr_token = ""

            while j <= len(code[i]):
                
                if j < len(code[i]):
                    c = code[i][j]

                if state == 0: # Inicial
                    if c.isspace(): 
                        j += 1
                        continue

                    curr_token += c
                    state = 0 if c.isspace() else 8 if self.isoperator(c) else 4 if self.isseparator(c) else 3 if self.issymbol(c) else 2 if c.isdigit() else 5 if self.isquote(c) else 6 if self.isbracket(c) else 1  # si no es ni un symbol o un digit, es un char cualquiera
                    j += 1
                    
                elif state == 1: # keyword/id
                    if c.isspace() or self.isoperator(c) or (self.issymbol(c) and c != '_') or self.isseparator(c) or self.isquote(c) or self.isbracket(c) or (j == len(code[i])):
                        if self.iskeywords(curr_token):
                            yield Token(curr_token, self.keywords[curr_token], TokenType.Keyword, i + 1, column)
                        elif self.check_identifier(curr_token, i, column):
                            yield Token(curr_token, curr_token, TokenType.Identifier, i + 1, column)

                        state = 0
                        curr_token = ""
                        column += 1

                    else:
                        curr_token += c
                        j += 1

                elif state == 2: # number ojo: no se tiene en cuenta los float ni negativos
                    if c.isspace() or self.isoperator(c) or self.issymbol(c) or self.isseparator(c) or self.isquote(c) or self.isbracket(c) or (j == len(code[i])):
                        if self.check_number(curr_token, i, column):
                            yield Token(curr_token, curr_token, TokenType.Number, i + 1, column)
                        state = 0
                        curr_token = ""
                        column += 1
                    else:
                        curr_token += c
                        j += 1

                elif state == 3: # symbols: <, >, <=, >=, ==, !=, <-, _, #
                    if curr_token == '#': 
                        break

                    if curr_token in ['>', '<', '=', '!'] and self.issymbol(c):
                        curr_token += c
                        j += 1

                    if self.issymbol(curr_token):
                        yield Token(curr_token, self.symbols[curr_token], TokenType.Symbol, i + 1, column)
                    else:
                        self.errors.append(f"{curr_token} token desconocido linea {i} posicion {column}")
                    
                    state = 0
                    curr_token = ""
                    column += 1

                elif state == 4 or state == 8: #state 4 : separator, state 8: operator
                    if self.isseparator(curr_token) or self.isoperator(curr_token):
                        yield Token(curr_token, 
                                    self.separators[curr_token] if state == 4 else self.operators[curr_token], 
                                    TokenType.Separator if state == 4 else TokenType.Operator, 
                                    i + 1, 
                                    column)
                    else:
                        self.errors.append(f"{curr_token} token desconocido linea {i} posicion {column}")

                    state = 0
                    curr_token = ""
                    column += 1

                elif state == 5 or state == 6: # quotes: ", brackets: (, ), {, }, [, ]
                    if self.isquote(curr_token) or self.isbracket(curr_token):
                        yield Token(curr_token,
                                    self.quotes[curr_token] if state == 5 else self.brackets[curr_token],
                                    TokenType.Quote if state == 5 else TokenType.Bracket,
                                    i + 1,
                                    column)         
                    else:
                        self.errors.append("Token desconocido")
                    
                    state = 7 if state == 5 else 0
                    curr_token = ""
                    column += 1

                elif state == 7: # Text: son los strings
                    if self.isquote(c):
                        yield Token(curr_token, curr_token, TokenType.Text, i, column)
                        yield Token(c, self.quotes[c], TokenType.Quote, i, column)
                        
                        state = 0
                        curr_token = ""
                        column += 1
                        j += 1
                    else:
                        curr_token += c
                        j += 1
                
                if c.isspace() and state != 7: j += 1

    def iskeywords(self, c):
        return self.keywords.__contains__(c)

    def issymbol(self, c):
        return self.symbols.__contains__(c)

    def isseparator(self, c):
        return self.separators.__contains__(c)

    def isquote(self, c):
        return self.quotes.__contains__(c)

    def isbracket(self, c):
        return self.brackets.__contains__(c)
    
    def isoperator(self, c):
        return self.operators.__contains__(c)

    def check_identifier(self, text, i, column):
        for i in range(len(text)):
            if not self.isCharValid(text[i], True if i==0 else False):
                self.errors.append(f"El identificador {text} de la linea {i} en la posicion {column} es invalido")
                return False
        return True
    
    def check_number(self, text, i, column):
        for c in text:
            if not c.isdigit():
                self.errors.append(f"El numero o identificador {text} de la linea {i} en la posicion {column} es invalido")
                return False
        return True

    def isCharValid(self, c, start): #Arreglar, se puede comenzar con _ (underscore)
        valid = c.isalpha() if start else c.isalnum() #(c.isalpha() or c.isdigit())
        return c == '_' or valid
    