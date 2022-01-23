from functools import reduce
from os import stat
from compilacion.analisis_lexico.token import Token, TokenType
from compilacion.grammars.grammar import Grammar
from compilacion.grammars.sentence import Sentence
from compilacion.grammars.terminal import Terminal
from compilacion.parsing.afn.afn import Afn
from compilacion.parsing.afn.state import State
from compilacion.parsing.firsts_follows import calculate_sentence_firsts
from compilacion.parsing.grammar_items import GrammarItems


class LRParser:
    def __init__(self, G: Grammar) -> None:
        self.grammar_items = GrammarItems(G)
        self.afd = self.build_AFDLR() # construimos el automata LR(1)
   
    
    def build_AFDLR(self):
        init_items =  self.grammar_items.init_items()
        init_state = State(init_items)
        i = 0
        queue_state = [init_state] # cola de estados
        symbols_transitions = set()
        symbols_transitions_list = []
        calculed_item_state = {}

        while len(queue_state) > 0:
            state = queue_state.pop(0)
            # if i == 18:
                # print("LLLLLLEEEEEGUUUUEE")
            if not calculed_item_state.__contains__(str(state)):
                # print("Estado procesado: ", state)
                item = state.item
                next_item = self.grammar_items.next_item(item)
                next_symbol = self.grammar_items.next_symbol(item)

                if next_symbol is not None and not next_symbol in symbols_transitions:
                    symbols_transitions.add(next_symbol)
                    symbols_transitions_list.append(next_symbol)

                if next_item is not None:
                    next_item_state = State(next_item)
                    state.add_transition(next_symbol, next_item_state)
                    queue_state.append(next_item_state)
                else:
                    state.is_final_state = True

                eps = self.grammar_items.epsilonItems(item)
                for e in eps:
                    eps_state = State(e)
                    state.add_epsilon_transition(eps_state)
                    queue_state.append(eps_state)
                    
                calculed_item_state[str(state)] = state
                i += 1
        
        # tratar de mejorar
        for st in calculed_item_state:
            state = calculed_item_state[str(st)]
            for i in range(len(state.epsilon_transitions)):
                eps = state.epsilon_transitions[i]
                if calculed_item_state.__contains__(str(eps)):
                    state.epsilon_transitions[i] = calculed_item_state[str(eps)]

        afn = Afn()
        afn.build_afd(init_state)
        return afn

    def parser(self, tokens, logger, ast=False):
        afn = self.afd
        grammar = self.grammar_items.G
        grammarItems = self.grammar_items
            
        afn.reset()        
        
        i = 0
        tree_stack = []
        
        state_stack = [afn.current_state]
        tokens.append(Token('$', '$'))    

        while(i < len(tokens)):
            shift, reduce_prod= False, set()
            curr_token = tokens[i].tokenType 
            afn.current_state = state_stack[-1]

            for state in afn.current_state.states:
                item = state.item
                
                if len(item.sentence.symbols) == item.pos: # item de la forma X -> a., s
                    if item.lookahead_contains(curr_token):
                        reduce_prod.add((item.production.left, item.sentence))
                
                # item de la forma X -> a.cw, s
                next_symbol = grammarItems.next_symbol(item)
                if next_symbol is not None and type(next_symbol) == Terminal:
                    if curr_token == next_symbol.name:
                        shift = True
                           

            if len(reduce_prod) > 1:
                logger.append("Error: conflicto reduce-reduce")
                break
            
            if shift:
                if len(reduce_prod) == 0:
                    goto = afn.Goto(curr_token) # afn.q(t.type_token)
                    state_stack.append(goto) # state_stack.append(afn.active)
                    tree_stack.append(curr_token) # tree_stack.append(SyntaxTree(t))
                    i += 1
                else:
                    logger.append("Error: conflicto shift-reduce")
                    break
            else:
                if len(reduce_prod) == 1:
                    (p_left, p_right)  = reduce_prod.pop() # tomo la production

                    for _ in range(len(p_right.symbols)): # saco de la pila todos los elementos que estan en la parte derecha de la produccion
                        tree_stack.pop()
                        state_stack.pop()

                    tree_stack.append(p_left)
                    afn.current_state = state_stack[-1] # afn.active = state_stack[-1]
                    goto = afn.Goto(p_left) # afn.q(reduce_production.Left)
                    state_stack.append(goto) # state_stack.append(afn.active)
                else:
                    if curr_token == '$':
                        if len(tree_stack) == 1 and tree_stack[0].name == grammar.startNoTerminal.name:
                            break # termino de parsear la cadena
                        else:
                            logger.append("Error:...")
                    else:
                        logger.append("Error: unexpected token ", curr_token)