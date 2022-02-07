from compilacion.parsing.afn.state import State
from compilacion.parsing.afn.complex_state import ComplexState


class Afn:
    def __init__(self) -> None: 
        self.states = {}      
        self.init_state = None
        self.states_dict = dict()
        self.dict_complex_states = dict()
        self.complex_states = set()
        self.broken = False

    
    def add_state(self, state):
        if not self.states.__contains__(state):
            self.states[state] = []
            self.states[state].append(state)


    def add_complexState(self, states, init_state=False): # añade un estado compuesto al automata
        if init_state:
            new_complex_st = ComplexState(states, self)
            self.complex_states.add(new_complex_st)
            self.dict_complex_states[hash(new_complex_st)] = new_complex_st
            return new_complex_st
        else:
            new_complex_st = ComplexState(states, self)
            st_hash = hash(new_complex_st)

            try:
                return self.dict_complex_states[st_hash]
            except:
                self.dict_complex_states[st_hash] = new_complex_st
                return new_complex_st

    def get_state(self, state):
        try:
            return self.states_dict[str(state)]
        except:
            self.states_dict[str(state)] = state
            return self.states_dict[str(state)]


    def add_transition(self, state_from, state_to, symbol):
        state_from = self.get_state(state_from)
        state_to = self.get_state(state_to)
        state_from.add_transition(symbol, state_to)        


    def add_epsilon_transition(self, state_from, state_to):
        state_from = self.get_state(state_from)
        state_to = self.get_state(state_to)
        state_from.add_epsilon_transition(state_to)


    def createInitComplexState(self, init_state): # crear el estado compuesto inicial
        self.init_state = self.add_complexState(init_state.epsilonClausure, True)
        self.current_state = self.init_state
        self.complex_states.add(self.current_state)
        return self.init_state


    def build_afd(self, init_state): # construir el AFD dado el AFN
        self.createInitComplexState(init_state)
        list_complex = list(self.complex_states) # calcular todas las transiciones
        # calculed_state = set()
        calculed_state = dict()

        while len(list_complex) > 0:
            st = list_complex.pop()
            trans_symbols = set()
            
            for state in st.states: # tomar todos los simbolos desde donde hay transiciones
                for symbol in state.transitions:
                    trans_symbols.add(symbol)
            
            for sym in trans_symbols: # por cada uno de estos simbolos se obliga a calcular sus trancisiones
                n = st.add_transition(sym)
                try:
                    calculed_state[hash(n)]
                except:
                    calculed_state[hash(n)] = n
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
                
    
    def Goto_Tokenize(self, symbol): # dado el estado actual y el simbolo que viene, cambiar al estado correspondiente
        if not self.broken:
            new_state = self.current_state.add_transition(symbol)
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
