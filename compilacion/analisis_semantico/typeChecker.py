import copy
from compilacion.analisis_semantico import visitor 
from compilacion.analisis_semantico.scopeTypeChecker import ScopeTypeChecker
from compilacion.analisis_semantico.Ast.instructions.functionNode import FunctionNode
from compilacion.analisis_semantico.Ast.instructions.variables.arrayDeclaration import ArrayDeclaration
from compilacion.analisis_semantico.Ast.instructions.variables.assignNode import AssignNode
from compilacion.analisis_semantico.Ast.instructions.variables.declaration import Declaration
from compilacion.analisis_semantico.Ast.attributeNode import AttributeNode
from compilacion.analisis_semantico.Ast.instructions.variables.reassignNode import ReassignNode
from compilacion.analisis_semantico.Ast.instructions.executeNode import ExecuteNode
from compilacion.analisis_semantico.Ast.instructions.filterNode import FilterNode
from compilacion.analisis_semantico.Ast.instructions.forNode import ForNode
from compilacion.analisis_semantico.Ast.instructions.printNode import PrintNode
from compilacion.analisis_semantico.Ast.instructions.returnNode import ReturnNode
from compilacion.analisis_semantico.Ast.instructions.strategyNode import StrategyNode
from compilacion.analisis_semantico.Ast.instructions.conditional import Conditional
from compilacion.analisis_semantico.Ast.instructions.breakNode import BreakNode
from compilacion.analisis_semantico.Ast.instructions.continueNode import ContinueNode
from compilacion.analisis_semantico.Ast.instructions.variables.declaration import Declaration
from compilacion.analisis_semantico.Ast.expressions.atomExpressions.arrayAtom import ArrayAtomNode
from compilacion.analisis_semantico.Ast.expressions.atomExpressions.boolNode import BoolNode
from compilacion.analisis_semantico.Ast.expressions.atomExpressions.funcCall import FuncCall
from compilacion.analisis_semantico.Ast.expressions.atomExpressions.idNode import IdNode
from compilacion.analisis_semantico.Ast.expressions.atomExpressions.IdProperty import IdPropertyNone
from compilacion.analisis_semantico.Ast.expressions.atomExpressions.indexNode import IndexNode
from compilacion.analisis_semantico.Ast.expressions.atomExpressions.lenNode import LenNode
from compilacion.analisis_semantico.Ast.expressions.atomExpressions.numberNode import IntNode, FloatNode
from compilacion.analisis_semantico.Ast.expressions.atomExpressions.rangeNode import RangeNode
from compilacion.analisis_semantico.Ast.expressions.atomExpressions.strNode import StrNode
from compilacion.analisis_semantico.Ast.expressions.operators.unaryOperator import UnaryOperator
from compilacion.analisis_semantico.Ast.expressions.operators.binaryOperator import BinaryOperator
from compilacion.analisis_semantico.Ast.programNode import ProgramNode
from compilacion.analisis_semantico.objectContext import ObjectContext


class TypeChecker:
    
    @visitor.on('node')
    def visit(self, node, a):
        pass

    @visitor.when(ProgramNode)
    

    @visitor.when(BinaryOperator)
    def visit(self, node, errors, scope): # se debe hacer uno por cada expresion
        self.visit(node.left, errors, scope)
        self.visit(node.right, errors, scope)
        
        if node.left.computed_type != node.right.computed_type:
            if (node.left.computed_type == "int" or node.left.computed_type == "float") and (node.right.computed_type == "float" or node.right.computed_type == "int"):
                node.computed_type = "float"
            elif node.left.computed_type == "exec" or node.right.computed_type == "exec":
                node.computed_type = "exec"
            else:
                node.computed_type = 0
                errors.append(f"Left expression has type {node.left.computed_type} and right expression has type {node.right.computed_type}")
        else:
            node.computed_type = node.left.computed_type

    @visitor.when(UnaryOperator)
    def visit(self, node, errors, scope):
        self.visit(node.expr, errors, scope)
        node.computed_type = node.expr.computed_type
    
    @visitor.when(ArrayAtomNode) #DONE
    def visit(self, node, errors, scope):
        curr_type = None
        for i in range(len(node.items)):
            item = node.items[i]
            self.visit(item, errors, scope)
            if i == 0:
                curr_type = item.computed_type
            if curr_type != item.computed_type:
                curr_type = "object"
                break
        node.computed_type = curr_type

    @visitor.when(BoolNode) #DONE
    def visit(self, node, errors, scope):
        node.computed_type = "bool"

    @visitor.when(FuncCall)
    def visit(self, node, errors, scope):
        if scope.check_func(node.identifier):
            node.computed_type = scope.funcsType[node.identifier]
        else:
            errors.append(f"Function {node.identifier} is not declared")
            node.computed_type = 0

    @visitor.when(IdNode) #DONE
    def visit(self, node, errors, scope):
        if scope.check_symbol(node.identifier):
            node.computed_type = scope.varsType[node.identifier]
        else:
            node.computed_type = 0
            errors.append(f"This {node.identifier} is not declared")

    @visitor.when(IdPropertyNone) #DONE
    def visit(self, node, errors, scope):
        node.computed_type = "exec"

    @visitor.when(IndexNode) # en ejecucion
    def visit(self, node, errors, scope):
        if scope.check_var(node.identifier):
            node.computed_type = scope.varsType[node.identifier]
        else:
            node.computed_type = 0
            errors.append(f"List {node.identifier} is not defined")

    @visitor.when(LenNode) #DONE
    def visit(self, node, errors, scope):
        node.computed_type = "int"

    @visitor.when(IntNode) #DONE
    def visit(self, node, errors, scope):
        node.computed_type = "int"

    @visitor.when(FloatNode) #DONE
    def visit(self, node, errors, scope):
        node.computed_type = "float"

    @visitor.when(RangeNode) #DONE  
    def visit(self, node, errors, scope):
        node.computed_type = "range"

    @visitor.when(StrNode) #DONE
    def visit(self, node, errors, scope):
        node.computed_type = "str"

    @visitor.when(ArrayDeclaration)
    def visit(self, node, errors, scope):
        self.visit(node.items, errors, scope)
        if node.type != node.items.computed_type:
            node.computed_type = 0
            errors.append(f"Declared type is {node.type} and elements of list have differents")
        else:
            node.computed_type = node.type

    @visitor.when(AssignNode)
    def visit(self, node, errors, scope):
        self.visit(node.value, errors, scope)
        if node.type != node.value.computed_type:
            if node.value.computed_type == "exec":
                node.computed_type = "exec"
            else:
                node.computed_type = 0
                errors.append(f"Declared type is {node.type} and expression has type {node.value.computed_type}")
        else:
            if scope.save_varType(node.identifier, node.type):
                node.computed_type = node.type
            else:
                node.computed_type = 0
                errors.append(f"Variable {node.identifier} is not declared")

    @visitor.when(Declaration)
    def visit(self, node, errors, scope): # los errores de declaration se ven en ejecucion
        for attr in node.args:
            self.visit(attr, errors, scope)
        node.computed_type = node.type
        scope.save_varType(node.identifier, node.type)

    @visitor.when(AttributeNode)
    

    @visitor.when(ReassignNode) # DONE
    def visit(self, node, errors, scope):
        if scope.check_symbol(node.identifier):
            curr_type = scope.varsType[node.identifier]
            self.visit(node.expr, errors, scope)

            if node.expr.computed_type != curr_type:
                if node.expr.computed_type == "exec":
                    node.computed_type = "exec"
                else:
                    node.computed_type = 0
                    errors.append(f"Declared type is {self.variablesType[node.identifier]} and expression has type {node.expr.computed_type}")
            else:
                node.computed_type = node.expr.computed_type
                scope.varsType[node.identifier] = node.computed_type
        else:
            node.computed_type = 0
            errors.append(f"Variable {node.identifier} not declared")

    @visitor.when(ExecuteNode)
    def visit(self, node, errors, scope):
        exeScope = ScopeTypeChecker()
        exeScope.funcsType = copy.deepcopy(scope.funcsType)

        for item in node.list_items:
            self.visit(item, errors, exeScope)
            if type(item) == ReturnNode:
                if node.return_type != item.expr.computed_type:
                    errors.append(f"Return type is {node.return_type} and expression to return has type {node.expr.computed_type}")

    @visitor.when(ForNode)
    def visit(self, node, errors, scope):
        forScope = copy.deepcopy(scope)
        for inst in node.body:
            self.visit(inst, errors, forScope)

    @visitor.when(FunctionNode)
    def visit(self, node, errors, scope):
        funcScope = ScopeTypeChecker()
        funcScope.funcsType = copy.deepcopy(scope.funcsType)

        for arg in node.args:
            funcScope.save_varType(arg.identifier, arg.type)
        
        for inst in self.body:
            self.visit(inst, errors, funcScope)
            if type(inst) == ReturnNode:
                if node.return_type != inst.expr.computed_type:
                    if inst.expr.computed_type != "exec":
                        errors.append(f"Return type is {node.return_type} and expression to return has type {node.expr.computed_type}")
        
    @visitor.when(PrintNode)
    def visit(self, node, errors, scope):
        self.visit(node.expr, errors, scope)

    @visitor.when(ReturnNode)
    def visit(self, node, errors, scope):
        if node.expr is None:
            node.computed_type = "void"
        else:
            self.visit(node.expr, errors, scope)

    @visitor.when(StrategyNode)
    def visit(self, node, errors, scope):
        strategyScope = ScopeTypeChecker()
        strategyScope.funcsType = copy.deepcopy(scope.funcsType)

        for elem in node.list_item[0]:
            self.visit(elem, errors, strategyScope)
        
        self.visit(node.list_item[1], errors, scope)
        
    @visitor.when(BreakNode)
    

    @visitor.when(ContinueNode)
    def visit(self, node, errors, scope):
        pass

    @visitor.when(Conditional)
    def visit(self, node, errors, scope):
        ifScope = copy.deepcopy(scope)
        elifScope = copy.deepcopy(scope)
        elseScope = copy.deepcopy(scope)

        self.visit(node.condition, errors, scope)
        
        for item in node.ifBody:
            self.visit(item, errors, ifScope)
        
        if node.elIf is not None:
            self.visit(node.elIf[0], errors, scope)
            for item in node.elIf[1]:
                self.visit(item, errors, elifScope)
        
        if node.elseBody is not None:
            for item in node.elseBody:
                self.visit(item, errors, elseScope)