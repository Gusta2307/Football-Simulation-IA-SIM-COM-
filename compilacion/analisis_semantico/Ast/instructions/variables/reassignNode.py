

from compilacion.analisis_semantico.Ast.instruction import Instruction
from compilacion.analisis_semantico.scope import Scope


class ReassignNode(Instruction):
      def __init__(self, identifier, new_value) -> None:
          self.identifier = identifier
          self.type = None
          self.new_value = new_value

      def checkSemantic(self, scope: Scope) -> bool:
        if scope.check_var(self.identifier):
            return self.new_value.checkSemantic(scope)      
        return False

      def execute(self, scope: Scope):
          if scope.check_var(self.identifier):
                scope.defineVar[self.identifier] = self.new_value.evaluate(scope)