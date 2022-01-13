from compilacion.grammars.grammar import Grammar
from compilacion.parsing.lrparser import LRParser


class LALRParser(LRParser):
    def __init__(self, G: Grammar) -> None:
        super().__init__(G)
        self.reduce_afn()
    
    def reduce_afn(self):
        pass