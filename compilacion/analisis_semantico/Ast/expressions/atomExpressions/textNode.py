from compilacion.analisis_semantico.Ast.expressions.atomExpression import AtomExpression
from compilacion.analisis_semantico.scope import Scope


class TextNode(AtomExpression):
    def __init__(self, text: str) -> None:
        self.text = text

    def checkSemantic(self, scope: Scope) -> bool:
        return True
    
    def evaluate(self, scope: Scope):
        return self.text