
from logging import root


class SyntaxTree:
    def __init__(self, value, production=None) -> None:
        self.value = value
        self.childs = []
        self.parent = None
        self.production = production

    def evaluate_attributes(self):
        if len(self.childs) > 0:
            result = self.production.attribute([child.evaluate_attributes() for child in self.childs])
        else:
            result = self.value.text
        return result

    def __str__(self) -> str:
        return str(self.value)

    def __repr__(self) -> str:
        return str(self)