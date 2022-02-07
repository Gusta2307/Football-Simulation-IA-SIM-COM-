from compilacion.analisis_lexico.regex.Ast.astNode import AstNode
from compilacion.parsing.afn.state import AnyItem, State


class UnionNode(AstNode):
    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right
    
    def evaluate(self):
        init_state = State(AnyItem())
        # final_state = State(AnyItem())

        l_inits, l_finals = self.left
        r_inits, r_finals = self.right

        for init in l_inits:
            init_state.add_epsilon_transition(init)

        for init in r_inits:
            init_state.add_epsilon_transition(init)

        return [init_state], l_finals + r_finals