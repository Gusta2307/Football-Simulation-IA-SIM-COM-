from typing import List
from compilacion.analisis_semantico.Ast.instructions.variables.assignNode import AssignNode
from compilacion.analisis_semantico.Ast.instructions.variables.reassignNode import ReassignNode
from compilacion.analisis_semantico.Ast.instruction import Instruction
from compilacion.analisis_semantico.Ast.instructions.returnNode import ReturnNode
from compilacion.analisis_semantico.Ast.instructions.forNode import ForNode
from compilacion.analisis_semantico.Ast.instructions.conditional import Conditional
from compilacion.analisis_semantico.scope import Scope

from compilacion.analisis_semantico.predefined import types
import copy

from compilacion.analisis_semantico.scopeTypeChecker import ScopeTypeChecker


class FunctionNode(Instruction):
    def __init__(self, identifier: str, return_type: str, args=[], body: List[Instruction]=None) -> None:
        self.identifier = identifier
        self.return_type = return_type
        self.args = args
        self.body = body
        self.func_scope = None
        self.stack_scope = []
    
    def checkSemantic(self, scope: Scope) -> bool:
        func_scope = Scope()
        
        for arg in self.args:
            func_scope.define_variables(arg.identifier)
            func_scope.originType[arg.identifier] = arg.type
        
        self.func_scope = func_scope

        if not scope.define_function(self.identifier, self.args):
            return False

        self.func_scope.defineFun = scope.defineFun #NUEVO
        
        for inst in self.body:
            if  not inst.checkSemantic(self.func_scope):
                return False
        return True

    def evaluateFunction(self, values):
        from compilacion.analisis_semantico.Ast.expressions.atomExpressions.funcCall import FuncCall
        for i in range(len(values)):            
            val_type, value = values[i]
            if val_type == 'func':
                self.func_scope.defineFunc[(self.args[i], len(self.args))] = value
            else:
                self.func_scope.defineVar[self.args[i].identifier] = value
        for inst in self.body:
            if type(inst) == ReturnNode:
                value = inst.execute(self.func_scope)
                if self.stack_scope:
                    self.func_scope = self.stack_scope.pop()
                if type(value) == types[self.return_type] or (types[self.return_type] == float and type(value) == int):
                    return value
                
                return None
            if  type(inst) == AssignNode or type(inst) == ReassignNode:
                if type(inst.value) == FuncCall and inst.value.identifier == self.identifier:
                    self.stack_scope.append(copy.deepcopy(self.func_scope))
            
            elif type(inst) == FuncCall and inst.identifier == self.identifier:
                self.stack_scope.append(self.func_scope)
              
            value = inst.execute(self.func_scope)
            if value is not None:
                if self.stack_scope:
                    self.func_scope = self.stack_scope.pop()
                return value
        if self.return_type != "void":
            if self.stack_scope:
                    self.func_scope = self.stack_scope.pop()
            return None


    def execute(self, scope: Scope):
        if (scope.check_fun(self.identifier, len(self.args))):
            scope.defineFun[(self.identifier, len(self.args))] = self


    def visit(self, scope):
        funcScope = ScopeTypeChecker()
        
        for arg in self.args:
            funcScope.save_varType(arg.identifier, arg.type)
        
        if not scope.check_func(self.identifier):
            scope.funcsType[self.identifier] = self.return_type
        else:
            print(f"Function {self.identifier} is not defined")
            return False

        funcScope.funcsType = copy.deepcopy(scope.funcsType)

        for inst in self.body:
            if not inst.visit(funcScope):
                return False
            if type(inst) == ReturnNode:
                if self.return_type != inst.expr.computed_type:    
                    if inst.expr.computed_type != "exec" and (self.return_type == "float" and inst.expr.computed_type != "int"):
                        print(f"Return type is {self.return_type} and expression to return has type {inst.expr.computed_type}")
                        return False
                else:
                    return True

            elif type(inst) == ForNode or type(inst) == Conditional:
                if type(inst) == ForNode:
                    if not self._funcNode_visit_forNode(inst):
                        return False
                
                elif type(inst) == Conditional:
                    if not self._funcNode_visit_Conditional(inst):
                        return False


        if self.return_type != "void":
            return True
        else:
            print(f"Return type of function {self.identifier} should be void")
        return False

    def _funcNode_visit_forNode(self, inst):
        for inst_aux in inst.body:
            if type(inst_aux) == ForNode:
                if not self._funcNode_visit_forNode(inst_aux):
                    return False
            elif type(inst_aux) == Conditional:
                if not self._funcNode_visit_Conditional(inst_aux):
                    return False
            elif type(inst_aux) == ReturnNode:
                if self.return_type != inst_aux.expr.computed_type:    
                    if inst_aux.expr.computed_type != "exec" and (self.return_type == "float" and inst_aux.expr.computed_type != "int"):
                        print(f"Return type is {self.return_type} and expression to return has type {inst_aux.expr.computed_type}")
                        return False
                else:
                    return True
        return True


    def _funcNode_visit_Conditional(self, inst):
        for inst_aux in inst.ifBody:
            if type(inst_aux) == ForNode:
                if not self._funcNode_visit_forNode(inst_aux):
                    return False
            elif type(inst_aux) == Conditional:
                if not self._funcNode_visit_Conditional(inst_aux):
                    return False
            elif type(inst_aux) == ReturnNode:
                if self.return_type != inst_aux.expr.computed_type:    
                    if inst_aux.expr.computed_type != "exec" and (self.return_type == "float" and inst_aux.expr.computed_type != "int"):
                        print(f"Return type is {self.return_type} and expression to return has type {inst_aux.expr.computed_type}")
                        return False
                else:
                    return True

        if inst.elIf is not None:
            for inst_aux in inst.elIf[1]:
                if type(inst_aux) == ForNode:
                    if not self._funcNode_visit_forNode(inst_aux):
                        return False
                elif type(inst_aux) == Conditional:
                    if not self._funcNode_visit_Conditional(inst_aux):
                        return False
                elif type(inst_aux) == ReturnNode:
                    if self.return_type != inst_aux.expr.computed_type:    
                        if inst_aux.expr.computed_type != "exec" and (self.return_type == "float" and inst_aux.expr.computed_type != "int"):
                            print(f"Return type is {self.return_type} and expression to return has type {inst_aux.expr.computed_type}")
                            return False
                    else:
                        return True

        if inst.elseBody is not None:
            for inst_aux in inst.elseBody:
                if type(inst_aux) == ForNode:
                    if not self._funcNode_visit_forNode(inst_aux):
                        return False
                elif type(inst_aux) == Conditional:
                    if not self._funcNode_visit_Conditional(inst_aux):
                        return False
                elif type(inst_aux) == ReturnNode:
                    if self.return_type != inst_aux.expr.computed_type:    
                        if inst_aux.expr.computed_type != "exec" and (self.return_type == "float" and inst_aux.expr.computed_type != "int"):
                            print(f"Return type is {self.return_type} and expression to return has type {inst_aux.expr.computed_type}")
                            return False
                    else:
                        return True

        return True