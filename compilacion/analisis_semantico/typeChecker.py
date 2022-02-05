import visitor
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
    def __init__(self, context) -> None:
        self.symbolsType = {} # <keys=identifier, value=type>


    @visitor.on('node')
    def visit(self, node):
        pass

    @visitor.when(ProgramNode)
    def visit(self, node, errors):
        for st in node.statement:
            self.visit(st, errors)

    @visitor.when(BinaryOperator)
    def visit(self, node, errors): #se debe hacer uno por cada expresion
        self.visit(node.left, errors)
        self.visit(node.right, errors)

        if node.left.computed_type != node.right.computed_type:
            node.computed_type = 0
            errors.append(f"Left expression has type {node.left.computed_type} and right expression has type {node.right.computed_type}")
        else:
            node.computed_type = node.left.computed_type

    @visitor.when(UnaryOperator)
    def visit(self, node, errors):
        self.visit(node.expr, errors)
    
    @visitor.when(ArrayAtomNode)
    def visit(self, node, errors):
        curr_type = None
        for i in range(len(node.items)):
            item = node.items[i]
            self.visit(item, errors)
            if i == 0:
                curr_type = item.computed_type
            if curr_type != item.computed_type:
                curr_type = "object"
                break
        node.computed_type = curr_type
        

    @visitor.when(BoolNode)
    def visit(self, node, errors):
        node.computed_type = "bool"

    @visitor.when(FuncCall)
    def visit(self, node, errors):
        pass

    @visitor.when(IdNode)
    def visit(self, node, errors):
        node.computed_type = self.symbolsType[node.identifier]

    @visitor.when(IdPropertyNone)
    def visit(self, node, errors):
        pass

    @visitor.when(IndexNode)
    def visit(self, node, errors):
        pass

    @visitor.when(LenNode)
    def visit(self, node, errors):
        node.computed_type = "int"

    @visitor.when(IntNode)
    def visit(self, node, errors):
        node.computed_type = "int"

    @visitor.when(FloatNode)
    def visit(self, node, errors):
        node.computed_type = "float"

    @visitor.when(RangeNode)
    def visit(self, node, errors):
        node.computed_type = "range"

    @visitor.when(StrNode)
    def visit(self, node, errors):
        node.computed_type = "str"

    @visitor.when(ArrayDeclaration)
    def visit(self, node, errors):
        self.visit(node.items, errors)
        if node.type != node.items.computed_type:
            node.computed_type = 0
            errors.append(f"Declared type is {node.type} and elements of list have differents")
        else:
            node.computed_type = node.type

    @visitor.when(AssignNode)
    def visit(self, node, errors):
        self.visit(node.expr)
        if node.type != node.expr.computed_type:
            node.computed_type = 0
            errors.append(f"Declared type is {node.type} and expression has type {node.expr.computed_type}")
        else:
            node.computed_type = node.type
        self.symbolsType[node.identifier] = node.computed_type

    @visitor.when(Declaration)
    def visit(self, node, errors): # los errores de declaration se ven en ejecucion
        for attr in node.args:
            self.visit(attr, errors)
        node.computed_type = node.type

    @visitor.when(AttributeNode)
    def visit(self, node, errors):
        self.visit(node.value, errors)
        node.computed_type = node.value.computed_type

    @visitor.when(ReassignNode)
    def visit(self, node, errors):
        self.visit(node.expr)
        if node.expr.computed_type != self.symbolsType[node.identifier]:
            node.computed_type = 0
            errors.append(f"Declared type is {self.symbolsType[node.identifier]} and expression has type {node.expr.computed_type}")
        else:
            node.computed_type = node.expr.computed_type

    @visitor.when(ExecuteNode)
    def visit(self, node, errors):
        for item in node.list_items:
            self.visit(item, errors)
            if type(item) == ReturnNode:
                if node.return_type != item.expr.computed_type:
                    errors.append(f"Return type is {node.return_type} and expression to return has type {node.expr.computed_type}")
            
    @visitor.when(FilterNode)
    def visit(self, node, errors):
        pass

    @visitor.when(ForNode)
    def visit(self, node, errors):
        for inst in node.body:
            self.visit(inst, errors)

    @visitor.when(FunctionNode)
    def visit(self, node, errors):
        for arg in node.args:
            self.symbolsType[arg.identifier] = arg.type
        
        for inst in self.body:
            self.visit(inst, errors)
            if type(inst) == ReturnNode:
                if node.return_type != inst.expr.computed_type:
                    errors.append(f"Return type is {node.return_type} and expression to return has type {node.expr.computed_type}")
        

    @visitor.when(PrintNode)
    def visit(self, node, errors):
        self.visit(node.expr, errors)

    @visitor.when(ReturnNode)
    def visit(self, node, errors):
        self.visit(node.expr, errors)

    @visitor.when(StrategyNode)
    def visit(self, node, errors):
        pass

    @visitor.when(BreakNode)
    def visit(self, node, errors):
        pass

    @visitor.when(ContinueNode)
    def visit(self, node, errors):
        pass

    @visitor.when(Conditional)
    def visit(self, node, errors):
        self.visit(node.condition, errors)
        
        for item in node.ifBody:
            self.visit(item, errors)
        
        if node.elIf is not None:
            self.visit(node.elIf[0], errors)
            for item in node.elIf[1]:
                self.visit(item, errors)
        
        if node.elseBody is not None:
            for item in node.elseBody:
                self.visit(item, errors)