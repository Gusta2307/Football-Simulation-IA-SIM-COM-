from compilacion.analisis_lexico.regex.Ast.astNode import AstNode


class QuestNode(AstNode):
    def __init__(self, value) -> None:
        self.value = value
    
    def evaluate(self):
        inits, finals = self.value
        return inits, finals + inits