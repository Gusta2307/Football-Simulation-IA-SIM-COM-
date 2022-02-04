from compilacion.analisis_semantico.Ast.instruction import Instruction
from compilacion.analisis_semantico.scope import Scope
from IA.estrategia import Estrategia
from utiles import create_dict

class StrategyNode(Instruction):
    def __init__(self, identifier, list_items) -> None:
        self.identifier = identifier
        self.list_item = list_items
        self.strategyScope = None

    def checkSemantic(self, scope: Scope) -> bool:
        for elem in self.list_item[0]:
            if not elem.checkSemantic(scope):
                return False
        
        if not self.list_item[1]:
            return False
        
        return scope.define_variables(self.identifier)

    def execute(self, scope: Scope): #list(lis(Attr1(BALL, ), Att), execute)
        variables = create_dict(self.list_item[0], scope)
        estrategia = Estrategia(variables, self.list_item[1])
        scope.defineVar[self.identifier] = estrategia
