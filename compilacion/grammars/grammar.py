"""
 Class Grammar: representa una gramatica de la forma G = <S, N, T, P>
"""

from compilacion.grammars.production import Production
from compilacion.grammars.terminal import Terminal
from compilacion.grammars.noTerminal import NoTerminal


class Grammar:
    def __init__(self) -> None:
        self.startNoTerminal = None
        self.noTerminals = []
        self.terminals = []
        self.productions = []
        self.EOF = Terminal('$')
    
    def define_noTerminal(self, name):
        noTerm = NoTerminal(name)
        self.noTerminals.append(noTerm)
        return noTerm


    def define_terminal(self, name):
        term = Terminal(name)
        self.terminals.append(term)
        return term


    def add_production(self, production : Production):
        production.left.productions.append(production)
        self.productions.append(production)


    def IsNoTerminal(self, name):
        return self.noTerminals.__contains__(name)


    def IsTerminal(self, name):
        return self.terminals.__contains__(name)
