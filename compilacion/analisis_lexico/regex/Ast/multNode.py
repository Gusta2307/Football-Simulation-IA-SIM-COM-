import itertools
from compilacion.analisis_lexico.regex.Ast.astNode import AstNode


class MultNode(AstNode):
    def __init__(self, value) -> None:
        self.value = value
    
    def evaluate(self):
        inits, finals = self.value
        for init, final in itertools.product(inits, finals):
            final.add_epsilon_transition(init)
        return inits, finals + inits