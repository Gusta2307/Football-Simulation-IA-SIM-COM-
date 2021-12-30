from compilacion.analisis_semantico.Ast.instructions.variableNode import VariableNode
from compilacion.analisis_semantico.Ast.instructions.functionNode import FunctionNode
from compilacion.analisis_semantico.objectContext import ObjectContext
from compilacion.analisis_semantico.Ast.programNode import ProgramNode


def visitor(f):
    def none(*args, **kw_args):
        pass
    return none


class TypeCollector:
    def __init__(self) -> None:
        self.context = ObjectContext()
    
    @visitor
    def visit(self, node: ProgramNode, logger):
        for st in node.statement:
            self.visit(st, logger)
    
    @visitor
    def visit(self, node: VariableNode, logger):
        self.context.create_type(node.var_type)

    @visitor
    def visit(self, node: FunctionNode, logger):
        self.context.create_type(node.return_type)
        for arg_type in node.arg_types:
            self.context.create_type(arg_type)
