from distutils.command.config import config
from compilacion.analisis_semantico.Ast.expressions.atomExpression import AtomExpression
from compilacion.analisis_semantico.Ast.expressions.atomExpressions.funcCall import FuncCall
from compilacion.analisis_semantico.Ast.expressions.atomExpressions.idNode import IdNode
from compilacion.analisis_semantico.Ast.expressions.atomExpressions.indexNode import IndexNode
from compilacion.analisis_semantico.scope import Scope

from config import Config
_config = Config()

class IdPropertyNone(AtomExpression):
    def __init__(self, identifier, _property) -> None:
        self.identifier = identifier
        self._property = _property
        self.property_value = None

    def checkSemantic(self, scope: Scope) -> bool:
        if type(self.identifier) == IdNode:
            if not scope.check_var(self.identifier):
                return False
        return True
        
        # if scope.check_var(self.identifier):
        #     return True
        # return False

    def evaluate(self, scope: Scope):
        var = scope.defineVar[self.identifier]
        if type(self._property) == FuncCall:
            self.property_value = getattr(var, _config.TRADUCTOR_ID.ID[self._property.identifier])
            return self.property_value()
        else:
            self.property_value = getattr(var, _config.TRADUCTOR_ID.ID[self._property])
            return self.property_value

    def visit(self, scope):
        self.computed_type = "exec"
        return True
