from compilacion.analisis_semantico.Ast.expressions.atomExpression import AtomExpression
from compilacion.analisis_semantico.Ast.expressions.atomExpressions.funcCall import FuncCall
from compilacion.analisis_semantico.scope import Scope


class IdPropertyNone(AtomExpression):
    def __init__(self, identifier, _property) -> None:
        self.identifier = identifier
        self._property = _property
        self.property_value = None

    def checkSemantic(self, scope: Scope) -> bool:
        if scope.check_var(self.identifier):
            return True
        return False

    def evaluate(self, scope: Scope):
        var = scope.defineVar[self.identifier]
        try:
            if type(self._property) == FuncCall:
                self.property_value = getattr(var, self._property.identifier)
                return self.property_value()
            else:
                self.property_value = getattr(var, self._property)
                return self.property_value
            # print(var)
        except:
            print("IDPROPERTYYYYYYYYY")
            return None
