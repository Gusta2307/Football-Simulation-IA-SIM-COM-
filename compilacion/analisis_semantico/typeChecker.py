from compilacion.analisis_semantico.Ast.expressions.operators.binaryOperator import BinaryOperator
from compilacion.analisis_semantico.Ast.programNode import ProgramNode
from compilacion.analisis_semantico.objectContext import ObjectContext
from compilacion.analisis_semantico.anyType import AnyType


def visitor(f):
    def none(*args, **kw_args):
        pass
    return none
    

class TypeChecker:
    def __init__(self, context) -> None:
        self.context: ObjectContext = context

    @visitor
    def visit(self, node: ProgramNode, logger):
        for st in node.statement:
            self.visit(st, logger)

    @visitor
    def visit(self, node: BinaryOperator, logger): #se debe hacer uno por cada expresion
        self.visit(node.left, logger)
        self.visit(node.right, logger)

        if node.left.computed_type != node.right.computed_type:
            # logger.error("Type...")
            node.computed_type = AnyType()
        else:
            node.computed_type = node.left.computed_type
