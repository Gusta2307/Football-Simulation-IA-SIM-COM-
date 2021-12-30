from compilacion.analisis_semantico.Ast.AstNode import AstNode
from compilacion.analisis_semantico.Ast.expressions.atomExpression import AtomExpression
from compilacion.analisis_semantico.scope import Scope


class AttributeNode(AstNode):
    def __init__(self, name: str, attr_type: str, value: AtomExpression) -> None:
        self.name = name
        self.type = attr_type
        self.value = value

    def checkSemantic(self, scope: Scope) -> bool:
        return self.value.checkSemantic(scope)