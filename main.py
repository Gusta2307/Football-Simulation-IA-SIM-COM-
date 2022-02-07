import os
from compilacion.analisis_semantico import *
from classes.equipo import Equipo
from classes.jugador import Jugador
from classes.manager import Manager
from classes.partido import Partido
from classes.portero import Portero
from compilacion.analisis_semantico.scope import Scope
from compilacion.parsing.lrparser import LRParser
from compilacion.analisis_lexico.lexer import Lexer
from compilacion.analisis_lexico.regex.regex import regex
from compilacion.analisis_lexico.regex.regex_grammar import regex_grammar
from compilacion.parsing.syntax_grammar import G
from compilacion.analisis_semantico.scopeTypeChecker import ScopeTypeChecker
from config import Config


config = Config()


def read_script(name):
    cwd = os.getcwd()
    direction = os.path.join(cwd, "compilacion", "test",  name)
    file = open(direction, "r")
    line = file.read()
    file.close()
    return line


def main():
    print("Input file:")
    file_name = input()
    code = read_script(file_name)

    lexer_parser = LRParser(regex_grammar)
    lexer = Lexer(regex, lexer_parser)

    # Analizador Lexico
    tokenizer_errors = []
    tokens_temp = lexer.tokenize(code, tokenizer_errors)
    tokens = [token for token in tokens_temp if token.tokenType != 'space']
   
    # Analizador Sintactico
    if len(tokenizer_errors) > 0:
        print_errors(tokenizer_errors)
        return

    parse_errors = []
    parser = LRParser(G)
    tree = parser.parser(tokens, parse_errors)
    if tree is None:
        return

    astTree = tree.evaluate_attributes()

    # Analisis Semantico
    scope = Scope()
    semantics_errors = []
    scopeType = ScopeTypeChecker()
    check_ok = astTree.checkSemantic(scope)

    if check_ok:
        check_ok = astTree.visit(scopeType)

    # Ejecucion
    if check_ok:
        astTree.execute(scope)


def print_errors(errors):
    for e in errors:
        print(e)


if '__main__' == __name__:
    main()
