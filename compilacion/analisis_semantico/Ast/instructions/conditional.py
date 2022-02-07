from typing import List, Tuple
from compilacion.analisis_semantico.Ast.instruction import Instruction
from compilacion.analisis_semantico.Ast.instructions.returnNode import ReturnNode
from compilacion.analisis_semantico.Ast.instructions.variables.assignNode import AssignNode
from compilacion.analisis_semantico.scope import Scope
from compilacion.analisis_semantico.Ast.expression import Expression
from utiles import actualizar_scope
import copy


class Conditional(Instruction):
    def __init__(self, condition: Expression, ifBody: List[Instruction], elIf: List[Tuple[Expression, List[Instruction]]] = None, elseBody: List[Instruction] = None) -> None:
        self.condition = condition
        self.ifBody = ifBody
        self.elIf = elIf
        self.elseBody = elseBody
        self.ifScope = None
        self.elifScope = None
        self.elseScope = None

    def checkSemantic(self, scope: Scope) -> bool:
        if not self.condition.checkSemantic(scope):
            return False
        
        self.ifScope = copy.deepcopy(scope)

        for inst in self.ifBody:
            if type(inst) == AssignNode:
                pass
            if not inst.checkSemantic(self.ifScope):
                return False
        
        if self.elIf is not None:
            self.elifScope = copy.deepcopy(scope)
            if not self.elIf[0].checkSemantic(self.elifScope):
                return False
            for inst in self.elIf[1]:
                if not inst.checkSemantic(self.elifScope):
                    return False

        if self.elseBody is not None:
            self.elseScope = copy.deepcopy(scope)
            for inst in self.elseBody:
                if not inst.checkSemantic(self.elseScope):
                    return False 
        return True

    def execute(self, scope: Scope):
        eval_cond = self.condition.evaluate(scope)
        if eval_cond:
            actualizar_scope(scope, self.ifScope)
            value = self.execute_instructions(self.ifScope, self.ifBody)
            actualizar_scope(self.ifScope, scope)
            if value is not None:
                return value
            return None
        elif self.elIf is not None:
            if self.elIf[0].evaluate(scope):
                actualizar_scope(scope, self.elifScope)
                value = self.execute_instructions(self.elifScope, self.elIf[1])
                actualizar_scope(self.elifScope, scope)
                if value is not None:
                    return value
                return None
        if self.elseBody is not None:
            actualizar_scope(scope, self.elseScope)
            value = self.execute_instructions(self.elseScope, self.elseBody)
            actualizar_scope(self.elseScope, scope)
            if value is not None:
                return value
            return None

    def execute_instructions(self, scope, instructions):
        for inst in instructions:
            if type(inst) == ReturnNode:
                value = inst.execute(scope)
                return value
            value = inst.execute(scope)
            if value is not None:
                return value

                
    def visit(self, scope):
        ifScope = copy.deepcopy(scope)
        elifScope = copy.deepcopy(scope)
        elseScope = copy.deepcopy(scope)

        self.condition.visit(scope)
        
        for item in self.ifBody:
            if not item.visit(ifScope):
                return False
        
        if self.elIf is not None:
            self.elIf[0].visit(scope)
            for item in self.elIf[1]:
                if not item.visit(elifScope):
                    return False
        
        if self.elseBody is not None:
            for item in self.elseBody:
                if not item.visit(elseScope):
                    return False
                    
        return True
        
        