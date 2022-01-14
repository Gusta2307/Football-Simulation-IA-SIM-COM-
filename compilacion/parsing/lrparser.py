from compilacion.grammars.grammar import Grammar
from compilacion.parsing.afn.afn import Afn
from compilacion.parsing.afn.state import State
from compilacion.parsing.firsts_follows import calculate_sentence_firsts
from compilacion.parsing.grammar_items import GrammarItems, ItemLR


class LRParser:
    def __init__(self, G: Grammar) -> None:
        self.grammar_items = GrammarItems(G)
        self.afn = self.build_AFNLR() # construimos el automata LR(0)

    def parser(self):
        pass
    
    def build_AFNLR(self):
        init_items =  self.grammar_items.init_items()
        init_state = State(init_items)

        stack_state = [init_state] # cola de estados
        symbols_transitions = set()
        symbols_transitions_list = []
        calculed_item_state = {}

        while len(stack_state) > 0:
            state = stack_state.pop(0)
            if not calculed_item_state.__contains__(str(state)):
                print(state)
                item = state.item
                next_item = self.grammar_items.next_item(item)
                next_symbol = self.grammar_items.next_symbol(item)

                if next_symbol is not None and not next_symbol in symbols_transitions:
                    symbols_transitions.add(next_symbol)
                    symbols_transitions_list.append(next_symbol)

                if next_item is not None:
                    next_item_state = State(next_item)
                    state.add_transition(next_symbol, next_item_state)
                    stack_state.append(next_item_state)
                else:
                    state.is_final_state = True

                eps = self.grammar_items.epsilonItems(item)
                for e in eps:
                    eps_state = State(e)
                    state.add_epsilon_transition(eps_state)
                    stack_state.append(eps_state)
                    
                calculed_item_state[str(state)] = state
        
        
        afn = Afn()
        afn.build_afd(init_state)
        return afn
