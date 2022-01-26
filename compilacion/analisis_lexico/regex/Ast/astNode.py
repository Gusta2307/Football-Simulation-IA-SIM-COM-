import abc


class AstNode:
    @abc.abstractclassmethod
    def evaluate(self):
        pass