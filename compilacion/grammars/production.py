from compilacion.grammars.noTerminal import NoTerminal


class Production:
    def __init__(self, left : NoTerminal, sentence, attribute=None) -> None:
        self.left = left
        self.right = [sentence] # secuencia de formas oracionales
        self.attribute = attribute  # es una expresion lambda

    def __str__(self) -> str:
        string = ""
        for i in range(len(self.right)):
            string += str(self.right[i])
            if i != len(self.right) - 1:
                string += " | "

        return f"{str(self.left)} -> {string}"

    def __repr__(self) -> str:
        return str(self)