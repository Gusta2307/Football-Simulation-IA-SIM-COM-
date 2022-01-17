
from typing import AbstractSet

from compilacion.parsing.afn.state import State

class ComplexState:
    def __init__(self, states, afn) -> None:
        self.states = states.union(self.epsilonClausure(states))
        self.transitions = {}
        self.is_final_state = False
        self.afn = afn
        
        for state in self.states:
            if state.is_final_state:
                self.is_final_state = True
                break
    
    def epsilonClausure(self, states) -> set:
        clausure = set()
        for state in states:
            cl = state.epsilonClausure
            clausure = clausure.union(cl)
        return clausure
    
    def add_transition(self, symbol):
        if self.transitions.__contains__(symbol):
            return self.transitions[symbol]
        
        states = set()

        for state in self.states: # por cada estado que hay en el estado compuesto
            if state.transitions.__contains__(symbol):
                for trans_state in state.transitions[symbol]:
                    states = states.union(trans_state.epsilonClausure)
        
        if len(states) > 0:
            complex_state = self.afn.add_complexState(states) # creo el nuevo estado compuesto
            self.transitions[symbol] = complex_state
            return complex_state
        
        return None
    
    def get_transition(self, symbol):
        for sym in self.transitions:
            if sym.name == str(symbol):
                return self.transitions[sym]
        return None

    def __str__(self):
        return str(self.states)
    
    def __repr__(self):
        return str(self)