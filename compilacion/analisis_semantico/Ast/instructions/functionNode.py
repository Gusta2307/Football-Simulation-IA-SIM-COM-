from typing import List
from compilacion.analisis_semantico.Ast.instruction import Instruction
from compilacion.analisis_semantico.Ast.instructions.returnNode import ReturnNode
from compilacion.analisis_semantico.scope import Scope
from compilacion.analisis_semantico.Ast.expressions.atomExpressions import funcCall
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
    
    def checkSemantic(self, scope: Scope) -> bool:
        print("ENTRE AL CHEQUEO")
        func_scope = Scope()
        
        for arg in self.args:
            func_scope.define_variables(arg.identifier)
        
        self.func_scope = func_scope


        if not scope.define_function(self.identifier, self.args):
            print("SCOPE EN FUNCTION:", scope)
            return False
        print("LLEGUE")

        self.func_scope.defineFun = copy.deepcopy(scope.defineFun) #NUEVO


        for inst in self.body:
            if  not inst.checkSemantic(self.func_scope):
                # print(inst)
                return False
                
        return True
        # if not self.func_scope.define_function(self.identifier, self.args):
        #     return False
        
        # return scope.define_function(self.identifier, self.args)

    def evaluateFunction(self, values):
        for i in range(len(values)):            
            val_type, value = values[i]
            if val_type == 'func':
                self.func_scope.defineFunc[(self.args[i], len(self.args))] = value
            else:
                self.func_scope.defineVar[self.args[i].identifier] = value
        for inst in self.body:
            if type(inst) == ReturnNode:
                value = inst.execute(self.func_scope)
                if type(value) == types[self.type]:
                    return value
                return None
            if type(inst) == funcCall and inst.identifier == self.identifier:
                print("RECURSIVIDAD")
              
            value = inst.execute(self.func_scope)
            if value is not None:
                return value
        if self.return_type != "void":
            print("ES VOID LA FUNCION")
            return None



    def execute(self, scope: Scope):
        if (scope.check_fun(self.identifier, len(self.args))):
            scope.defineFun[(self.identifier, len(self.args))] = self


    def visit(self, scope):
        funcScope = ScopeTypeChecker()
        funcScope.funcsType = copy.deepcopy(scope.funcsType)

        for arg in self.args:
            funcScope.save_varType(arg.identifier, arg.type)
        
        for inst in self.body:
            if not inst.visit(funcScope):
                return False
            if type(inst) == ReturnNode:
                if self.return_type != inst.expr.computed_type:
                    if inst.expr.computed_type != "exec":
                        print(f"Return type is {self.return_type} and expression to return has type {inst.expr.computed_type}")
                        return False
        return True
                        