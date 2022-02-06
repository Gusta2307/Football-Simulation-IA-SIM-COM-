from compilacion.analisis_semantico.Ast.expression import Expression
from compilacion.analisis_semantico.Ast.instructions.variableNode import VariableNode
from compilacion.analisis_semantico.scope import Scope
from compilacion.analisis_semantico.predefined import types


class AssignNode(VariableNode):
    def __init__(self, identifier: str, var_type: str, value: Expression) -> None:
        super().__init__(identifier, var_type)
        self.value = value
        self.computed_type = None
    
    def checkSemantic(self, scope: Scope) -> bool:
        return self.value.checkSemantic(scope) and scope.define_variables(self.identifier)
    
    def execute(self, scope: Scope):
        if scope.check_var(self.identifier):
            val = self.value.evaluate(scope)
            if type(val) == types[self.type]:
                scope.defineVar[self.identifier] = val
    
    def visit(self, scope):
        if not self.value.visit(scope):
            return False
        if self.type != self.value.computed_type:
            if self.value.computed_type == "exec":
                self.computed_type = "exec"
                return True
            else:
                self.computed_type = 0
                print(f"Declared type is {self.type} and expression has type {self.value.computed_type}")
                return False
        else:
            if scope.save_varType(self.identifier, self.type):
                self.computed_type = self.type
                return True
            else:
                self.computed_type = 0
                print(f"Variable {self.identifier} is not declared")
                return False