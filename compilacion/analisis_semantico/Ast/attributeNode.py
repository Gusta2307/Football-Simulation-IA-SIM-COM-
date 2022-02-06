from compilacion.analisis_semantico.Ast.AstNode import AstNode
from compilacion.analisis_semantico.Ast.expressions.atomExpression import AtomExpression
from compilacion.analisis_semantico.scope import Scope


class AttributeNode(AstNode):
    def __init__(self, name: str, value: AtomExpression) -> None:
        self.name = name
        self.computed_type = None
        self.value = value

    def checkSemantic(self, scope: Scope) -> bool:
        return self.value.checkSemantic(scope)

    def visit(self, scope):
        if not self.value.visit(scope):
            return False
            
        self.computed_type = self.value.computed_type
        return True

    def __str__(self) -> str:
        return str(self.name) + " = " + str(self.value)
