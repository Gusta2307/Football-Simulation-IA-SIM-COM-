from typing import List
from compilacion.analisis_semantico.Ast.instruction import Instruction
from compilacion.analisis_semantico.Ast.instructions.breakNode import BreakNode
from compilacion.analisis_semantico.Ast.instructions.continueNode import ContinueNode
from compilacion.analisis_semantico.Ast.instructions.returnNode import ReturnNode
from compilacion.analisis_semantico.scope import Scope
from utiles import actualizar_scope
import copy



class ForNode(Instruction):
    def __init__(self, item: str, iterable: str, body: List[Instruction]) -> None:
        self.item = item
        self.iter = iterable
        self.body = body
        self.forScope = None

    def checkSemantic(self, scope: Scope) -> bool:
        self.forScope = copy.deepcopy(scope)

        if not self.forScope.check_var(self.iter.identifier):
            return False

        if self.forScope.define_variables(self.item):
            for ins in self.body:
                if not ins.checkSemantic(self.forScope):
                    return False
            return True
        return False

    def execute(self, scope: Scope):
        if_break = 0
        actualizar_scope(scope, self.forScope)
        iterable = scope.defineVar[self.iter.identifier]
        for elem in iterable.items:
            self.forScope.defineVar[self.item] = elem.evaluate(self.forScope)
            for item_body in self.body:
                if type(item_body) == ContinueNode:
                    break
                elif type(item_body) == BreakNode:
                    if_break = 1
                    actualizar_scope(self.forScope, scope)
                    break
                elif type(item_body) == ReturnNode:
                    actualizar_scope(self.forScope, scope)
                    return item_body.execute(self.forScope)
                else:
                    value = item_body.execute(self.forScope)
                    if value is not None:
                        actualizar_scope(self.forScope, scope)
                        return value
            if if_break:
                actualizar_scope(self.forScope, scope)
                break
        actualizar_scope(self.forScope, scope)
    
    def visit(self, scope):
        forScope = copy.deepcopy(scope)
        if not forScope.check_var(self.item):
            forScope.varsType[self.item] = forScope.varsType[self.iter.identifier]
        else:
            return False
        for inst in self.body:
            if not inst.visit(forScope):
                return False
        return True