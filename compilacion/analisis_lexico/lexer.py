from compilacion.analisis_lexico.afn import Afn
from compilacion.analisis_lexico.token import *


class Lexer:
    def __init__(self, regex) -> None:
        self.regex = regex  # recibe las expresiones regulares
        self.afn = Afn()    # recibe un automata finito


    def tokenize(self, line_input):
        pass