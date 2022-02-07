from compilacion.analisis_lexico.regex.Ast.astNode import AstNode
from compilacion.parsing.afn.state import AnyItem, State


class RangeSymNode(AstNode):
    def __init__(self, left_symbol, right_symbol) -> None:
        self.left_symbol = left_symbol
        self.right_symbol = right_symbol
    
    def evaluate(self):
        init_state = State(AnyItem())
        final_state = State(AnyItem())
        for x in range(ord(self.left_symbol), ord(self.right_symbol) + 1):
            init_state.add_transition(chr(x), final_state)
        return [init_state], [final_state]


class RangeUnderSymNode(AstNode):
    def __init__(self, value) -> None:
        self.value = value

    def evaluate(self):
        init_state = State(AnyItem())
        final_state = State(AnyItem())
        for x in range(0, ord(self.value) + 1):
            init_state.add_transition(chr(x), final_state)
        return [init_state], [final_state]


class RangeSymUnderNode(AstNode):
    def __init__(self, value) -> None:
        self.value = value

    def evaluate(self):
        init_state = State(AnyItem())
        final_state = State(AnyItem())
        for x in range(ord(self.value), 256):
            init_state.add_transition(chr(x), final_state)
        return [init_state], [final_state]
    