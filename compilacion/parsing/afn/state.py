from compilacion.parsing.grammar_items import ItemLR


class State:
    def __init__(self, item : ItemLR, is_final_state=False) -> None:
        self.item = item
        self.transitions = {}  # dict<key=sym, value=state> 
        self.epsilon_transitions = []  # List[state]
        self.is_final_state = is_final_state
    
    @property
    def epsilonClausure(self) -> set:
        clausure = {self}

        l = 0
        while l != len(clausure):
            l = len(clausure)
            tmp = [s for s in clausure]
            for s in tmp:
                for epsilon_state in s.epsilon_transitions:
                    clausure.add(epsilon_state)
        return clausure

    def add_transition(self, symbol, state):
        if not self.transitions.__contains__(symbol):
            self.transitions[symbol] = []
        self.transitions[symbol].append(state)

    def add_epsilon_transition(self, state):
        if not state in self.epsilon_transitions:
            self.epsilon_transitions.append(state)
    
    def get_state(self, symbol):
        if self.transitions.__contains__(symbol):
            return self.transitions[symbol]
    
    def __str__(self) -> str:
        return str(self.item)

    def __repr__(self) -> str:
        return str(self.item)
