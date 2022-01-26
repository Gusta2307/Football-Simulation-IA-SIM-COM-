from compilacion.parsing.afn.afn import Afn
from compilacion.analisis_lexico.token import *
from compilacion.parsing.afn.state import AnyItem, State
from compilacion.parsing.lrparser import LRParser


class Lexer:
    def __init__(self, regex, lr_parser : LRParser) -> None:
        self.regex = regex  # recibe las expresiones regulares
        self.lr_parser = lr_parser
        self.precedent = {} # prioridad de los tokens 
        self.afn = self.build_LexerAFN()


    def tokenize(self, line_input):
        tokens = []
        self.afn.reset()

        i, col, row = 0, 0, 0
        new_token_col, new_token_row, new_token_pos = 0, 0, 0
        last_token_col, last_token_row, last_token_pos = 0, 0, 0
        c, valid_token = None, None

        while i < len(line_input):
            if i == len(line_input):
                tokens.append(valid_token)
                valid_token = None
                if new_token_pos >= len(line_input):
                    break
                i, col, row = new_token_pos, new_token_col, new_token_row

            if c == '\n':
                row += 1
                col = 0

            c = line_input[i]

            self.afn.current_state = self.afn.Goto_Tokenize(c)
            if self.afn.broken:
                if not valid_token is None:
                    tokens.append(valid_token)
                    last_token_pos, last_token_col, last_token_row = i, col, row
                    i, col, row = new_token_pos, new_token_col, new_token_row
                else:
                    #BATACANG Error lexicografico
                    # tokens.append(ErrorToken(
                    #         line_input[new_token_pos:i+1],
                    #         new_token_col,
                    #         new_token_row,
                    #         new_token_pos)
                    #     )
                    #error
                    last_token_pos, last_token_col, last_token_row = i+1,col+1,row
                    new_token_pos, new_token_col, new_token_row = i+1,col+1,row
                    i+=1
                
                valid_token = None
                self.afn.reset()
                continue
            
            if not self.afn.broken and self.afn.current_state.is_final_state:
                #buscando el tipo de token de menor precedencia de entre todos los posibles tokens a resumir
                index = min([self.precedent[x.item.tokenType] for x in self.afn.current_state.states if x.is_final_state])
                # type_token = self.index_token[index_type_token]
                tokenType = None

                for t in self.precedent:
                    if self.precedent[t] == index:
                        tokenType = t

                valid_token = Token(
                        tokenType,
                        line_input[last_token_pos:i+1],
                        last_token_col,
                        last_token_row,
                        last_token_pos
                    )
                new_token_pos, new_token_col, new_token_row = i+1,col+1,row
            
            i+=1
            col+=1
        
        return tokens

        


    def build_LexerAFN(self):
        errors = []
        list_state = []
        state, priority = 0, 0

        for r in self.regex:
            if r == 'num'  or r == 'id':
                print("IDE")
            tree = self.buildAstByRegex(self.regex[r], errors)
            new_state = self.createAfnState(state, tree.ast, r)
            list_state.append(new_state)
            self.precedent[r] = priority
            state += 1
            priority += 1
            print(r)

        init_state = State(AnyItem())
        for state in list_state:
            init_state.add_epsilon_transition(state)
        
        afn = Afn()
        afn.createInitComplexState(init_state)
        return afn


    def buildAstByRegex(self, item_regex, errors):
        i = 0
        tokens = []

        while i < len(item_regex):
            if item_regex[i] == '(':
                tokens.append(Token('(', '('))
            elif item_regex[i] == ')':
                tokens.append(Token(')', ')'))
            elif item_regex[i] == '[':
                tokens.append(Token('[', '['))
            elif item_regex[i] == ']':
                tokens.append(Token(']', ']'))
            elif item_regex[i] == '.':
                tokens.append(Token('.', '.'))
            elif item_regex[i] == '_':
                tokens.append(Token('_', '_'))
            elif item_regex[i] == '+':
                tokens.append(Token('+', '+'))
            elif item_regex[i] == '-':
                tokens.append(Token('-', '-'))
            elif item_regex[i] == '*':
                tokens.append(Token('*', '*'))
            elif item_regex[i] == '|':
                tokens.append(Token('|','|' ))
            elif item_regex[i] == '?':
                tokens.append(Token('?','?' ))
            else:
                tokens.append(Token(item_regex[i], 'symbol'))
            i += 1

        # # if '([_]|[a-zA-Z])([_]|[a-zA-Z0-9])*' == item_regex:
        # if '[1-9][0-9]*(.[0-9]+)?' ==  item_regex or '[.]'==item_regex:
        #     print("DDDD")
        tree = self.lr_parser.parser(tokens, errors, True)
        return tree


    def createAfnState(self, state, ast, tokenType):
        inits, finals = ast
        new_state = State(state)

        inits, finals = ast

        for init in inits:
            new_state.add_epsilon_transition(init)
        
        for final in finals:
            final.item.tokenType = tokenType
            final.final = True

        return new_state
    