from os import stat
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
        pass


    def build_LexerAFN(self):
        errors = []
        list_state = []
        state, priority = 0, 0

        for r in self.regex:
            # if r == 'num' or r == '.':
            #     print("IDE")
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
    