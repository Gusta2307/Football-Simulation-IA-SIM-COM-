from compilacion.analisis_lexico.regex.Ast.astNode import AstNode
from compilacion.parsing.afn.afn import Afn
from compilacion.parsing.afn.state import AnyItem, State


class SymbolNode(AstNode):
    def __init__(self, symbol) -> None:
        self.symbol = symbol
    
    def evaluate(self):
        init_state = State(AnyItem())
        final_state = State(AnyItem())
        init_state.add_transition(self.symbol, final_state)
        return [init_state], [final_state]