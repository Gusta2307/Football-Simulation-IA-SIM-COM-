from compilacion.grammars.grammar import Grammar
from compilacion.grammars.noTerminal import NoTerminal
from compilacion.grammars.sentence import Sentence
from compilacion.parsing.firsts_follows import calculate_firsts, calculate_follows, calculate_sentence_firsts

"""
Representacion de Item LR(1)
"""

class ItemLR:
    def __init__(self, production, sentence: Sentence, pos, lookaheads) -> None:
        self.pos = pos # posicion del "."
        self.production = production
        self.sentence = sentence
        self.lookaheads = tuple(look for look in lookaheads)
        self.head = self.get_head() # lo que esta antes del "."
        self.tail = self.get_tail() # lo que esta despues del "."

    def get_head(self):
        head = Sentence(*self.sentence.symbols[0:self.pos])
        return head
    
    def get_tail(self):
        tail = Sentence(*self.sentence.symbols[self.pos:])
        return tail

    def next_item(self): # dado un item, devolver el item resultado de mover el "."
        if self.pos + 1 <= len(self.sentence.symbols):
            new_item = ItemLR(self.production, self.sentence, self.pos + 1, self.lookaheads)
            return new_item
        return None

    def next_symbol(self): # dado un item, devolver el symbol que se añadio al mover el "."
        if len(self.head.symbols) > 0:
            symbol = self.head.symbols[len(self.head.symbols) - 1]
            return symbol
        return None

    def __str__(self) -> str:
        return f"{str(self.production.left)} -> {str(self.head)}.{str(self.tail)} {self.lookaheads}"

    def __repr__(self) -> str:
        return str(self)


class GrammarItems:
    def __init__(self, G: Grammar) -> None:
        self.G = G
        self.follows = calculate_follows(G)

    def init_items(self):
        prod = self.G.productions[0] 
        sent = prod.right[0]
        item = ItemLR(prod, sent, 0, (self.G.EOF,))
        return item
            
    def epsilonItems(self, item: ItemLR):
        pos = item.pos
        eps_set = set()

        if len(item.sentence.symbols) > pos:
                next_symbol = item.sentence.symbols[pos]
                if type(next_symbol) == NoTerminal:
                    for p in next_symbol.productions:
                        for r in p.right:
                            if len(item.lookaheads) > 1:
                                print("dd")
                            for look in item.lookaheads:
                                firsts = {}
                                l = item.sentence.symbols[pos + 1:]
                                a = Sentence(*l)
                                if a.symbols != []:
                                    a.symbols.append(look)
                                    firsts[str(a)] = []
                                    calculate_sentence_firsts(a, firsts, self.G.epsilon)
                                f = firsts[str(a)] if a.symbols != [] else [self.G.EOF]
                                new_item = ItemLR(p, r, 0, f)
                                eps_set.add(new_item)
        return eps_set