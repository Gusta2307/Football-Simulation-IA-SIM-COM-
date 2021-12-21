from compilacion.token import *


class AnalisisLexico:
    def __init__(self) -> None:
        self.keywords = {}
        self.symbols = {}
        self.separators = {}
        self.errors = []  # guarda los errores durante la tokenizacion
    
    def registerKeyword(self, text, value):
        self.keywords[text] = value
    
    def registerSymbol(self, text, value):
        self.symbols[text] = value

    def registerSeparator(self, text, value):
        self.separators[text] = value    

    def tokenize(self, code):
        # listTokens = []
        
        for i in range(len(code)):
            j = 0
            state = 0
            column = 1
            curr_token = ""

            while j <= len(code[i]) - 1:
                c = code[i][j]  # tomo el caracter actual

                # if c == '\n': j += 1

                if state == 0:
                    if c.isspace() or (j < len(code[i]) - 1): j += 1
                    curr_token += c
                    state = 11 if self.isseparator(c) else 3 if self.issymbol(c) else 2 if c.isdigit() else 1  # si no es ni un symbol o un digit, es un char cualquiera
                    
                elif state == 1:
                    if c.isspace() or self.issymbol(c) or self.isseparator(c): #si es un espacio en blanco o viene un symbol, el token llega hasta donde esta
                        if self.iskeywords(curr_token):
                            yield Token(curr_token, self.keywords[curr_token], TokenType.Keyword, i + 1, column)
                        elif not self.issymbol(curr_token):  # es un identificador
                            if self.check_identifier(curr_token, i, column):
                                yield Token(curr_token, curr_token, TokenType.Identifier, i + 1, column)

                        state = 0
                        curr_token = ""
                        column += 1
                        if c.isspace() or j == len(code[i]) - 1: j += 1

                    else:
                        curr_token += c
                        j += 1

                elif state == 2:
                    if c.isspace() or self.issymbol(c) or self.isseparator(c):
                        if self.check_number(curr_token, i, column):
                            yield Token(curr_token, curr_token, TokenType.Number, i + 1, column)
                        state = 0
                        curr_token = ""
                        column += 1
                        if c.isspace() or j == len(code[i]) - 1: j += 1
                    else:
                        curr_token += c
                        j += 1
                       # if c.isalpha(): #este tipo de string no es valido ej: 1hola = "kiko"

                elif state == 3:
                    if curr_token == '#': 
                        break

                    if self.issymbol(curr_token) and (curr_token == '>' or curr_token == '<' or curr_token == '=' or curr_token == '!'):
                        state = 4 if curr_token == '>' else 5 if curr_token == '<' else 6 #if curr_token == '=' else 7
                        continue

                    # elif c.isspace() or c.isdigit() or self.isseparator(c) or (c.isalpha() and not self.issymbol(c)):
                    if self.issymbol(curr_token):
                        yield Token(curr_token, self.symbols[curr_token], TokenType.Symbol, i + 1, column)

                    else:
                        self.errors.append(f"{curr_token} token desconocido ia {i} posicion {column}")
                    
                    state = 10 if curr_token == '"' else 0
                    curr_token = ""
                    column += 1
                    if c.isspace() or j == len(code[i]) - 1: j += 1

                elif state == 4:
                    if self.issymbol(c) and c == '=':
                        curr_token += c
                        j += 1
                        state = 6
                    else:
                        if self.issymbol(curr_token):
                            yield Token(curr_token, self.symbols[curr_token], TokenType.Symbol, i + 1, column)

                            state = 0
                            curr_token = ""
                            column += 1
                            if c.isspace() or j == len(code[i]) - 1: j += 1
                        else:
                            self.errors.append("Error")

                elif state == 5:
                    if c == '=' or c == '-':
                        state = 8 if c == '=' else 9
                        curr_token += c
                        j += 1

                    else:
                        if not self.issymbol(c):
                            if self.issymbol(curr_token):
                                yield Token(curr_token, self.symbols[curr_token], TokenType.Symbol, i + 1, column)
                            else:
                                self.errors.append("Error")
                        else:
                            self.errors.append("Error")
                        
                        state = 0
                        curr_token = ""
                        column += 1
                        if c.isspace() or j == len(code[i]) - 1: j += 1

                elif state == 6: #vino un = depsues de un =
                    if c == '=':
                        curr_token += c
                        j += 1
                    elif curr_token == "=" and c == '"':
                        state = 10
                        continue
                    else:
                        self.errors.append("Error")

                    state = 0
                    curr_token = ""
                    column += 1
                    if c.isspace() or j == len(code[i]) - 1: j += 1

                elif state == 8:
                    if not self.issymbol(c):
                        if self.issymbol(curr_token):
                            yield Token(curr_token, self.symbols[curr_token], TokenType.Symbol, i + 1, column)
                        else:
                            self.errors.append("Error")
                    else:
                        self.errors.append("Error")

                    state = 0
                    curr_token = ""
                    column += 1
                    if c.isspace() or j == len(code[i]) - 1: j += 1

                elif state == 9:
                    if not self.issymbol(c) or c == '"':
                        if self.issymbol(curr_token):
                            yield Token(curr_token, self.symbols[curr_token], TokenType.Symbol, i + 1, column)
                        else:
                            self.errors.append("Error")
                    else:
                        self.errors.append("Error")

                    state = 10 if c == '"' else 0
                    curr_token = ""
                    column += 1
                    if c.isspace() or j == len(code[i]) - 1: j += 1
                
                elif state == 10:
                    if c == '"':
                        if self.issymbol(curr_token):
                            yield Token(curr_token, self.symbols[curr_token], TokenType.Symbol, i + 1, column)
                        else:
                            yield Token(curr_token, curr_token, TokenType.Text, i, column)

                        state = 0
                        curr_token = ""
                        column += 1

                    else:
                        if not self.issymbol(c) and not self.isseparator(c):
                            curr_token += c
                            j += 1                        
                        else:
                            state = 0
                            j += 1
                
                elif state == 11:
                    if self.isseparator(curr_token):
                        yield Token(curr_token, self.separators[curr_token], TokenType.Separator, i + 1, column)
                    
                    state = 0
                    curr_token = ""
                    column += 1
                    if c.isspace() or j == len(code[i]) - 1: j += 1


    def iskeywords(self, c):
        return self.keywords.__contains__(c)

    def issymbol(self, c):
        return self.symbols.__contains__(c)

    def isseparator(self, c):
        return self.separators.__contains__(c)

    def check_identifier(self, text, i, column):
        for i in range(len(text)):
            if not self.isCharValid(text[i], True if i==0 else False):
                self.errors.append(f"El identificador {text} de la ia {i} en la posicion {column} es invalido")
                return False
        return True
    
    def check_number(self, text, i, column):
        for c in text:
            if not c.isdigit():
                self.errors.append(f"El numero o identificador {text} de la ia {i} en la posicion {column} es invalido")
                return False
        return True

    def isCharValid(self, c, start):
        valid = c.isalpha() if start else (c.isalpha() or c.isdigit())
        return c == '_' or valid