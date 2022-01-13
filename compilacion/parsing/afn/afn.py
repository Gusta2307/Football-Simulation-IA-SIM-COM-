
from compilacion.parsing.afn.state import State


class Afn:
    def __init__(self, init_state: State) -> None: 
        self.states = {}      
        self.init_state = init_state
        self.add_state(init_state)
    
    def add_state(self, state):
        if not self.states.__contains__(state):
            self.states[state] = []
            self.states[state].append(state)

    def add_transition(self, symbol, state_from : State, state_to):
        state_from.add_transition(symbol, state_to)

    def add_epsilon_transition(self, state_from, state_to):
        state_from.add_epsilon_transition(state_to)

    def get_finals_states(self):
        finals_states = []
        for st in self.states.keys():
             if self.states[st].is_final_state:
                finals_states.append(st)
        return finals_states