

from compilacion.analisis_semantico.Ast.instruction import Instruction
from compilacion.analisis_semantico.Ast.instructions.variableNode import VariableNode
from compilacion.analisis_semantico.scope import Scope
from compilacion.analisis_semantico.predefined import types

class ReassignNode(VariableNode):
    def __init__(self, identifier, value) -> None:
        self.identifier = identifier
        self.computed_type = None
        self.value = value

    def checkSemantic(self, scope: Scope) -> bool:
      if scope.check_var(self.identifier):
          return self.value.checkSemantic(scope)      
      return False

    def execute(self, scope: Scope): 
      if scope.check_var(self.identifier):
        val = self.value.evaluate(scope)
        asig_type = types[scope.originType[self.identifier]]
        if type(val) == asig_type or asig_type == object or (asig_type == float and type(val) == int):
          scope.defineVar[self.identifier] = val

    def visit(self, scope):
        if scope.check_var(self.identifier):
            curr_type = scope.varsType[self.identifier]
            if not self.value.visit(scope):
              return False

            if self.value.computed_type != curr_type:
                if curr_type == "object":
                      self.computed_type = "object"
                      return True
                elif self.value.computed_type == "exec":
                      self.computed_type = "exec"
                      return True
                elif curr_type == "float" and self.value.computed_type == "int":
                      self.computed_type = "float"
                      return True
                else:
                    self.computed_type = 0
                    print(f"Declared type is {self.variablesType[self.value.identifier]} and expression has type {self.value.computed_type}")
                    return False
            else:
                self.computed_type = self.value.computed_type
                scope.varsType[self.identifier] = self.computed_type
                return True
        else:
            self.computed_type = 0
            print(f"Variable {self.identifier} not declared")
        return False