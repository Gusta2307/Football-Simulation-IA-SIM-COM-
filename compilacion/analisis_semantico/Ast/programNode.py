from compilacion.analisis_semantico.Ast.AstNode import AstNode
from compilacion.analisis_semantico.scope import Scope
# from compilacion.analisis_semantico.typeBuilder import TypeBuilder
# from compilacion.analisis_semantico.typeChecker import TypeChecker
# from compilacion.analisis_semantico.typeCollector import TypeCollector


class ProgramNode(AstNode):
    def __init__(self, statement) -> None:
        self.statement = statement
    
    def checkSemantic(self, scope: Scope) -> bool:
        # logger = None
        # collector = TypeCollector()
        # collector.visit(self, logger)

        # builder = TypeBuilder(collector.context)
        # builder.visit(self, logger)

        # checker = TypeChecker(builder.context)
        # checker.visit(self, logger)

        #si logger tiene errores, return False

        for inst in self.statement:
            if not inst.checkSemantic(scope):
                return False
        return True

    def execute(self, scope: Scope):
        if self.checkSemantic(scope):
            for inst in self.statement:
                inst.execute(scope)
