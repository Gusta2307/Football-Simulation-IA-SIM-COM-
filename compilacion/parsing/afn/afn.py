from compilacion.parsing.afn.state import State
from compilacion.parsing.afn.complex_state import ComplexState


class Afn:
    def __init__(self) -> None: 
        self.states = {}      
        self.init_state = None
        self.complex_states = set()
        self.complex_states_dict = dict()
        self.broken = False

    
    def add_state(self, state):
        if not self.states.__contains__(state):
            self.states[state] = []
            self.states[state].append(state)

    def add_complexState(self, states): # añade un estado compuesto al automata
       tuple_states = tuple(states)
       if not tuple_states in self.complex_states:
           self.complex_states_dict[tuple_states] = ComplexState(states, self)
       return self.complex_states_dict[tuple_states]

    def createInitComplexState(self, init_state):
        self.init_state = init_state
        self.current_state = self.add_complexState(init_state.epsilonClausure)
        self.complex_states.add(self.current_state)
        # self.initial_complex_state = self.add_complexState(init_state.epsilonClausure)
        # self.active = self.initial_complex_state
        # self.complex_states.add(self.initial_complex_state)
        return self.current_state

    def build_afd(self, init_state):
        self.createInitComplexState(init_state)
        list_complex = list(self.complex_states) # calcular todas las transiciones
        
        while len(list_complex) > 0:
            st = list_complex.pop()

            trans_symbols = set()
            
            for state in st.states: # tomar todos los simbolos desde donde hay transiciones
                for symbol in state.transitions:
                    trans_symbols.add(symbol)
            
            for sym in trans_symbols: # por cada uno de estos simbolos se obliga a calcular sus trancisiones
                n = st.add_transition(sym)
                if not n in self.complex_states:
                    self.complex_states.add(n)
                    list_complex.append(n)
            