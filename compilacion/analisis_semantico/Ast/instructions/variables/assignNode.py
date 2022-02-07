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
        if self.value.checkSemantic(scope) and scope.define_variables(self.identifier):
            scope.originType[self.identifier] = self.type
            return True
        return False
    
    def execute(self, scope: Scope):
        if scope.check_var(self.identifier):
            val = self.value.evaluate(scope)
            if type(val) == types[self.type] or types[self.type] == object or (types[self.type] == float and type(val) == int):
                scope.defineVar[self.identifier] = val
    
    def visit(self, scope):
        if not self.value.visit(scope):
            return False
        if self.type != self.value.computed_type:
            if self.type == "object":
                if scope.save_varType(self.identifier, "object"):
                    self.computed_type = "object"
                    return True
            elif self.type == "float" and self.value.computed_type == "int":
                if scope.save_varType(self.identifier, "float"):
                    self.computed_type = "float"
                    return True
            elif self.value.computed_type == "exec":
                if scope.save_varType(self.identifier, "exec"):
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