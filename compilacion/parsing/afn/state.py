from compilacion.parsing.grammar_items import ItemLR


class State:
    def __init__(self, item : ItemLR, is_final_state=False) -> None:
        self.item = item
        self.transitions = {}  # dict<key=sym, value=state> 
        self.epsilon_transitions = []  # List[state]
        self.is_final_state = is_final_state
        self.all_trans_calculate = False
    
    def add_transition(self, symbol, state):
        if not self.transitions.__contains__(symbol):
            self.transitions[symbol] = []
        self.transitions[symbol].append(state)

    def add_epsilon_transition(self, state):
        self.epsilon_transitions.append(state)
    
    def get_state(self, symbol):
        if self.transitions.__contains__(symbol):
            return self.transitions[symbol]
    
    def __str__(self) -> str:
        return str(self.item)

    def __repr__(self) -> str:
        return str(self.item)
