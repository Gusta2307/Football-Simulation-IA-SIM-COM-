from compilacion.parsing.afn.state import State

class ComplexState:
    def __init__(self, states, afn) -> None:
        self.states = states
        self.states = states.union(self.epsilonClausure)
        self.transitions = {}
        self.is_final_state = False
        self.afn = afn
        
        for state in self.states:
            if state.is_final_state:
                self.is_final_state = True
                break
    
    @staticmethod
    def epsilon_clausure_by_state(complex_state):
        epsilon_clausure = set()
        for state in complex_state.states:
            epsilon_clausure = epsilon_clausure.union(state.epsilonClausure)
        return epsilon_clausure
    
    @property
    def epsilonClausure(self):
        return self.epsilon_clausure_by_state(self)

    def add_transition(self, symbol):
        if self.transitions.__contains__(symbol):
            return self.transitions[symbol]
        
        states = set()

        for state in self.states: # por cada estado que hay en el estado compuesto
            if state.exist_transition(symbol):
                for trans_state in state.transitions[symbol]:
                    states = states.union(trans_state.epsilonClausure)
        
        if len(states) > 0:
            complex_state = self.afn.add_complexState(states) # creo el nuevo estado compuesto
            self.transitions[symbol] = complex_state
            return complex_state
        
        return None


    def get_transition(self, symbol):
        for sym in self.transitions:
            if str(sym) == str(symbol):   # sym.name
                return self.transitions[sym]
        return None


    def __str__(self):
        return str(self.states)

    
    def __repr__(self):
        return str(self)

    def __hash__(self):
        h = ""
        for x in self.states:
            h += str(hash(x))
        return hash(h)
    
    def __eq__(self, other):
        return self.states == other.states