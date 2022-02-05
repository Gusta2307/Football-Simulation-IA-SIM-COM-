from compilacion.analisis_semantico.Ast.AstNode import AstNode
from compilacion.analisis_semantico.Ast.expressions.atomExpression import AtomExpression
from compilacion.analisis_semantico.scope import Scope


class AttributeNode(AstNode):
    def __init__(self, name: str, value: AtomExpression) -> None:
        self.name = name
        self.computed_type = None
        self.value = value

    def checkSemantic(self, scope: Scope) -> bool:
        # print("Tipo:", type(self.value))
        # result = self.value.checkSemantic(scope)
        # print(result)
        # return result
        return self.value.checkSemantic(scope)

    def __str__(self) -> str:
        return str(self.name) + " = " + str(self.value)