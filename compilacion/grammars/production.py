from compilacion.grammars.noTerminal import NoTerminal


class Production:
    def __init__(self, left : NoTerminal, *args) -> None:
        self.left = left
        self.right = [s for s in args] # secuencia de formas oracionales

    def __str__(self) -> str:
        string = ""
        for i in range(len(self.right)):
            string += str(self.right[i])
            if i != len(self.right) - 1:
                string += " | "

        return f"{str(self.left)} -> {string}"

    def __repr__(self) -> str:
        return str(self)