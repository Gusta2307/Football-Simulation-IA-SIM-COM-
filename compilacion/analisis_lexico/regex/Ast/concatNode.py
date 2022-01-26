import itertools
from compilacion.analisis_lexico.regex.Ast.astNode import AstNode


class ConcatNode(AstNode):
    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right
    
    def evaluate(self):
        l_inits, l_finals = self.left
        r_inits, r_finals = self.right

        for final, init in itertools.product(l_finals, r_inits):
            final.add_epsilon_transition(init)
        
        return l_inits, r_finals