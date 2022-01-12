
from compilacion.grammars.grammar import Grammar
from compilacion.parsing.firsts_follows import calculate_noTerminal_firsts, calculate_follows


class LRParser:
    def __init__(self, G: Grammar) -> None:
        self.firsts = calculate_noTerminal_firsts(G.productions)
        self.follows = calculate_follows(G, self.firsts)
        self.afn = self.build_afn_LRParser() # construimos el automata LR(0)

    
    def build_afn_LRParser(self):
        pass