from functools import reduce
from itertools import product
from os import stat
import string
from compilacion.analisis_lexico.token import Token
from compilacion.grammars.grammar import Grammar
from compilacion.grammars.sentence import Sentence
from compilacion.grammars.production import Production
from compilacion.grammars.terminal import Terminal
from compilacion.parsing.afn.afn import Afn
from compilacion.parsing.afn.state import State
from compilacion.parsing.syntaxTree import SyntaxTree
from compilacion.parsing.firsts_follows import calculate_sentence_firsts
from compilacion.parsing.grammar_items import GrammarItems


class LRParser:
    def __init__(self, G: Grammar) -> None:
        self.grammar_items = GrammarItems(G)
        self.afd = self.build_AFDLR() # construimos el automata LR(1)
   
    
    def build_AFDLR(self):
        i = 0
        afn = Afn()
        init_items =  self.grammar_items.init_items()
        init_state = State(init_items)
        queue_state = [init_state] # cola de estados
        symbols_transitions = set()
        calculed_item_state = set()

        while len(queue_state) > 0:
            state = queue_state.pop(0)
            if not state in calculed_item_state:
                item = state.item
                next_item = self.grammar_items.next_item(item)
                next_symbol = self.grammar_items.next_symbol(item)
                if next_symbol is not None and not next_symbol in symbols_transitions:
                    symbols_transitions.add(next_symbol)

                if next_item is not None:
                    next_item_state = State(next_item)
                    
                    afn.add_transition(state, next_item_state, next_symbol)
                    queue_state.append(next_item_state)
                else:
                    state.is_final_state = True

                
                eps = self.grammar_items.epsilonItems(item)

                for e in eps:
                    eps_state = State(e)
                    afn.add_epsilon_transition(state, eps_state)
                    queue_state.append(eps_state)

                calculed_item_state.add(state)
                i += 1

        afn = Afn()
        afn.build_afd(init_state)
        return afn


    def parser(self, tokens, errors, ast=False):
        afn = self.afd
        grammar = self.grammar_items.G
        grammarItems = self.grammar_items
            
        i = 0
        afn.reset()        
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
                        reduce_prod.add(item.production)
                
                next_symbol = grammarItems.next_symbol(item)
                if next_symbol is not None and type(next_symbol) == Terminal:
                    if curr_token == next_symbol.name:
                        shift = True
                           
            if len(reduce_prod) > 1:
                errors.append("Error: conflict reduce-reduce")
                break
            
            if shift:
                if len(reduce_prod) == 0:
                    goto = afn.Goto(curr_token) # afn.q(t.type_token)
                    state_stack.append(goto) # state_stack.append(afn.active)
                    tree_stack.append(SyntaxTree(tokens[i])) # tree_stack.append(SyntaxTree(t))
                    i += 1
                else:
                    errors.append("Error: conflict shift-reduce")
                    break
            else:
                if len(reduce_prod) == 1:
                    r_production  = reduce_prod.pop() # tomo la production
                    root = SyntaxTree(r_production.left, r_production)

                    for _ in range(len(r_production.right[0].symbols)): # saco de la pila todos los elementos que estan en la parte derecha de la produccion
                        new_child = tree_stack.pop()
                        new_child.parent = root
                        root.childs.append(new_child)
                        state_stack.pop()

                    root.childs.reverse()

                    if(ast):
                        attributes = []
                        for item in root.childs:
                            try:
                                attributes.append(item.ast)
                            except:
                                attributes.append(item)
                        root.ast = r_production.attribute(attributes).evaluate()

                    tree_stack.append(root)
                    afn.current_state = state_stack[-1] # afn.active = state_stack[-1]
                    goto = afn.Goto(r_production.left) # afn.q(reduce_production.Left)
                    state_stack.append(goto) # state_stack.append(afn.active)
                    
                else:
                    if curr_token == '$':
                        if len(tree_stack) == 1 and tree_stack[0].value.name == grammar.startNoTerminal.name:
                            return tree_stack[0]
                        else:
                            errors.append("Error: ")
                            break
                    else:
                        errors.append(f"Error: unexpected token")
                        break
        return None