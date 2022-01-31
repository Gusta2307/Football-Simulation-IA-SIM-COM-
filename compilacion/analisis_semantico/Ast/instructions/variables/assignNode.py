from compilacion.analisis_semantico.Ast.expression import Expression
from compilacion.analisis_semantico.Ast.instructions.variableNode import VariableNode
from compilacion.analisis_semantico.scope import Scope


class AssignNode(VariableNode):
    def __init__(self, identifier: str, var_type: str, value: Expression) -> None:
        super().__init__(identifier, var_type)
        self.value = value
    
    def checkSemantic(self, scope: Scope) -> bool:
        return self.value.checkSemantic(scope) and scope.define_variables(self.identifier)
    
    def execute(self, scope: Scope):
        if scope.check_var(self.identifier):
            scope.defineVar[self.identifier] = self.value.evaluate(scope)