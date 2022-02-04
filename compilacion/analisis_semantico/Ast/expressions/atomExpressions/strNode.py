from compilacion.analisis_semantico.Ast.expression import Expression
from compilacion.analisis_semantico.scope import Scope

class StrNode(Expression):
    def __init__(self, text) -> None:
        self.text = text
    
    def checkSemantic(self, scope: Scope) -> bool:
        return True

    def evaluate(self, scope: Scope):
        return self.text[1: len(self.text) - 1]
    
    def __str__(self) -> str:
        return str(self.text)