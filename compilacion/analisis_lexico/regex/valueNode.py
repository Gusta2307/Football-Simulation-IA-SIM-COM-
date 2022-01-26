from compilacion.analisis_lexico.regex.Ast.astNode import AstNode


class ValueNode(AstNode):
    def __init__(self, value) -> None:
        self.value = value
    
    def evaluate(self):
        return self.value

