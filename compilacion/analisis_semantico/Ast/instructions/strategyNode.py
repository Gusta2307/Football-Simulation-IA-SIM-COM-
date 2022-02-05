from compilacion.analisis_semantico.Ast.instruction import Instruction
from compilacion.analisis_semantico.scope import Scope
from IA.estrategia import Estrategia
from utiles import create_dict
import copy

class StrategyNode(Instruction):
    def __init__(self, identifier, list_items) -> None:
        self.identifier = identifier
        self.list_item = list_items
        self.strategyScope = None

    def checkSemantic(self, scope: Scope) -> bool:
        self.strategyScope = Scope()
        self.strategyScope.defineFun = copy.deepcopy(scope.defineFun)

        for elem in self.list_item[0]:
            print("STATEGY ITEMS:", str(elem))
            if not elem.checkSemantic(scope):
                return False
            print("ELEM:", elem.identifier)    
            v = self.strategyScope.define_variables(elem.identifier)
            print("Resultado de añadir:", v)
        
        if not self.list_item[1].checkSemantic(self.strategyScope):
            print("CHECK DE EXECUTE")
            return False

        return scope.define_variables(self.identifier)

    def execute(self, scope: Scope): #list(lis(Attr1(BALL, ), Att), execute)
        variables = create_dict(self.list_item[0], scope)
        estrategia = Estrategia(variables, self.list_item[1])
        scope.defineVar[self.identifier] = estrategia
