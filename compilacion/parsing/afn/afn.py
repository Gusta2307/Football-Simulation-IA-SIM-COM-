from compilacion.parsing.afn.state import State
from compilacion.parsing.afn.complex_state import ComplexState


class Afn:
    def __init__(self) -> None: 
        self.states = {}      
        self.init_state = None
        self.complex_states = []
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

    def createInitComplexState(self, init_state): # crear el estado compuesto inicial
        self.init_state = self.add_complexState(init_state.epsilonClausure)
        self.current_state = self.init_state
        self.complex_states.append(self.current_state)
        return self.init_state

    def build_afd(self, init_state): # construir el AFD dado el AFN
        self.createInitComplexState(init_state)
        list_complex = list(self.complex_states) # calcular todas las transiciones
        calculed_state = {}

        while len(list_complex) > 0:
            st = list_complex.pop()

            trans_symbols = set()
            
            for state in st.states: # tomar todos los simbolos desde donde hay transiciones
                for symbol in state.transitions:
                    trans_symbols.add(symbol)
            
            for sym in trans_symbols: # por cada uno de estos simbolos se obliga a calcular sus trancisiones
                n = st.add_transition(sym)
                if not calculed_state.__contains__(str(n)):
                    self.complex_states.append(n)
                    calculed_state[str(n)] = n
                    list_complex.append(n)
    
    def Goto(self, symbol): # dado el estado actual y el simbolo que viene, cambiar al estado correspondiente
        if not self.broken:
            new_state = self.current_state.get_transition(symbol)
            if new_state is not None:
                self.current_state = new_state
            else:
                self.broken = True
                new_state = self.current_state
            return new_state
        return None
                
    def reset(self):
        self.broken = False
        self.current_state = self.init_state
