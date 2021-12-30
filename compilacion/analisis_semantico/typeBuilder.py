from compilacion.analisis_semantico.Ast.attributeNode import AttributeNode
from compilacion.analisis_semantico.Ast.instructions.functionNode import FunctionNode
from compilacion.analisis_semantico.Ast.instructions.variableNode import VariableNode
from compilacion.analisis_semantico.Ast.instructions.variables.declaration import Declaration
from compilacion.analisis_semantico.Ast.programNode import ProgramNode
from compilacion.analisis_semantico.objectContext import ObjectContext
from compilacion.analisis_semantico.type import MyType


def visitor(f):
    def none(*args, **kw_args):
        pass
    return none


class TypeBuilder:
    def __init__(self, context: ObjectContext) -> None:
        self.context  = context
        self.currentType : MyType = None
    
    @visitor
    def visit(self, node: ProgramNode):
        for st in node.statement:
            self.visit(st)

    @visitor
    def visit(self, node: VariableNode):
        self.currentType = self.context.get_type(node.type)
        self.context.define_symbol(node.identifier, self.currentType)

        if type(node) == Declaration:
            for attr in node.attribute:
                self.visit(attr)
    
    @visitor
    def visit(self, node: AttributeNode):
        attr_type = self.context.get_type(node.type)
        self.currentType.define_attribute(node.name, attr_type)

    @visitor
    def visit(self, node: FunctionNode):
        return_type = self.context.get_type(node.return_type)
        arg_types = [self.context.get_type(t) for t in node.arg_types]
        self.currentType.define_method(node.identifier, return_type, node.args, arg_types)
        self.context.define_symbol(node.identifier, return_type)
