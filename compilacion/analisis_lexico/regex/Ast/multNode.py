import itertools
from compilacion.analisis_lexico.regex.Ast.astNode import AstNode


class MultNode(AstNode):
    def __init__(self, leaf) -> None:
        self.leaf = leaf
    
    def evaluate(self):
        inits, finals = self.leaf
        for init, final in itertools.product(inits, finals):
            final.add_epsilon_transition(init)
        return inits, finals + inits