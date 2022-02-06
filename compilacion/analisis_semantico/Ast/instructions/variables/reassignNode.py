

from compilacion.analisis_semantico.Ast.instruction import Instruction
from compilacion.analisis_semantico.Ast.instructions.variableNode import VariableNode
from compilacion.analisis_semantico.scope import Scope
from compilacion.analisis_semantico.predefined import types

class ReassignNode(VariableNode):
    def __init__(self, identifier, new_value) -> None:
        self.identifier = identifier
        self.computed_type = None
        self.new_value = new_value

    def checkSemantic(self, scope: Scope) -> bool:
      if scope.check_var(self.identifier):
          return self.new_value.checkSemantic(scope)      
      return False

    def execute(self, scope: Scope): # lo del tipo
      if scope.check_var(self.identifier):
        val = self.new_value.evaluate(scope)
        if type(val) == types[self.type]:
          scope.defineVar[self.identifier] = val

    def visit(self, scope):
        if scope.check_symbol(self.identifier):
            curr_type = scope.varsType[self.identifier]
            if not self.new_value.visit(scope):
              return False

            if self.new_value.computed_type != curr_type:
                if self.new_value.computed_type == "exec":
                    self.computed_type = "exec"
                    return True
                else:
                    self.computed_type = 0
                    print(f"Declared type is {self.variablesType[self.new_value.identifier]} and expression has type {self.new_value.computed_type}")
                    return False
            else:
                self.computed_type = self.new_value.computed_type
                scope.varsType[self.identifier] = self.computed_type
                return True
        else:
            self.computed_type = 0
            print(f"Variable {self.identifier} not declared")
            return False