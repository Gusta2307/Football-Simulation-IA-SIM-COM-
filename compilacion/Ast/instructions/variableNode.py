from compilacion.Ast.instruction import Instruction


class VariableNode(Instruction):
    def __init__(self, identifier: str) -> None:
        self.identifier = identifier