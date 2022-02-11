from compilacion.analisis_semantico.Ast.instruction import Instruction
from compilacion.analisis_semantico.scope import Scope
from IA.estrategia import Estrategia
from compilacion.analisis_semantico.scopeTypeChecker import ScopeTypeChecker
from utiles import create_dict_decl
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
            if not elem.checkSemantic(scope):
                return False
            v = self.strategyScope.define_variables(elem.identifier)
        
        if not self.list_item[1].checkSemantic(self.strategyScope):
            return False

        return scope.define_variables(self.identifier)

    def execute(self, scope: Scope): 
        variables = create_dict_decl(self.list_item[0], scope)
        estrategia = Estrategia(variables, self.list_item[1])
        scope.defineVar[self.identifier] = estrategia
    
    def visit(self, scope):
        strategyScope = ScopeTypeChecker()
        strategyScope.funcsType = copy.deepcopy(scope.funcsType)

        for elem in self.list_item[0]:
            if not elem.visit(strategyScope):
                return False
        
        if not self.list_item[1].visit(strategyScope):
            return False

        if not scope.check_var(self.identifier):
            scope.varsType[self.identifier] = 'strategy'
            return True
        return False
