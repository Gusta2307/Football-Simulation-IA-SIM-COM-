from compilacion.analisis_semantico.scope import Scope

class StrategyNode:
      def __init__(self, identifier, list_items) -> None:
          self.identifier = identifier
          self.list_item = list_items
          self.strategyScope = None

      def checkSemantic(self, scope: Scope) -> bool:
          self.strategyScope = Scope()

          for item in self.list_item:
              if not item.checkSemantic(self.strategyScope):
                  return False
          
          return scope.define_variables(self.identifier)