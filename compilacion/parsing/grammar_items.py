from compilacion.grammars.epsilon import Epsilon
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
        self.lookaheads = lookaheads
        self.head = self.get_head() # lo que esta antes del "."
        self.tail = self.get_tail() # lo que esta despues del "."

    def get_head(self):
        head = Sentence(*self.sentence.symbols[0:self.pos])
        return head
    
    def get_tail(self):
        tail = Sentence(*self.sentence.symbols[self.pos:])
        return tail

    def lookahead_contains(self, elem):
        for look in self.lookaheads:
            if str(look) == elem:
                return True
        return False

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
        item = ItemLR(prod, sent, 0, [self.G.EOF])
        return item
    
    def next_item(self, item): # dado un item, devolver el item resultado de mover el "."
        if item.pos + 1 <= len(item.sentence.symbols):
            new_item = ItemLR(item.production, item.sentence, item.pos + 1, item.lookaheads)
            return new_item
        return None

    def next_symbol(self, item): # dado un item, devolver el symbol que se añadio al mover el "."
        if item.pos < len(item.sentence.symbols):
            return item.sentence.symbols[item.pos]
        else:
            return None

    def epsilonItems(self, item: ItemLR):
        pos = item.pos
        eps_set = []
        
        if len(item.sentence.symbols) > pos:
                next_symbol = item.sentence.symbols[pos]
                if type(next_symbol) == NoTerminal:
                    for p in next_symbol.productions:
                        for sent in p.right:
                            item_sent = Sentence(*item.sentence.symbols[pos + 1:])
                            first = {str(item_sent) : []}
                            calculate_sentence_firsts(item_sent, first, self.G.epsilon)
                            look = item.lookaheads if len(item_sent.symbols) == 0 else first[str(item_sent)]
                            new_item = ItemLR(p, sent, 0, look)
                            if not new_item in eps_set:
                                eps_set.append(new_item)
        return eps_set