from compilacion.grammars.grammar import Grammar
from compilacion.parsing.afn.afn import Afn
from compilacion.parsing.afn.state import State
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
        afn = Afn(init_state)

        stack_state = [init_state] # pila de estados
        symbols_transitions = set()
        symbols_transitions_list = []


        while len(stack_state) > 0:
            state = stack_state.pop(0)
            if not state.all_trans_calculate:
                afn.add_state(state)
                next_item = state.item.next_item()
                if next_item is None:
                    state.is_final_state = True
                    continue
                
                next_symbol = state.item.next_symbol()

                if next_symbol is not None and not next_symbol in symbols_transitions:
                    symbols_transitions.add(next_symbol)
                    symbols_transitions_list.append(next_symbol)
           
                    next_item_state = State(next_item)
                    afn.add_transition(next_symbol, state, next_item_state)
                    stack_state.append(next_item_state)

                eps = self.grammar_items.epsilonItems(state.item)
                for e in eps:
                    eps_state = State(e)
                    afn.add_epsilon_transition(state, eps_state)
                    stack_state.append(eps_state)
                    
                # calculed_item_state.add(state)
                state.all_trans_calculate = True
        
        return 
