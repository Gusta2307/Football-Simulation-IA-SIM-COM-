
from logging import root


class SyntaxTree:
    def __init__(self, value, production=None) -> None:
        self.value = value
        self.childs = []
        self.parent = None
        self.production = production

    def __str__(self) -> str:
        return str(self.value)

    def __repr__(self) -> str:
        return str(self)