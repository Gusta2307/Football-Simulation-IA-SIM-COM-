import os
# import string
from compilacion.analisis_semantico import *
from classes.equipo import Equipo
from classes.arbitro import Arbitro
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
from compilacion.analisis_semantico.typeChecker import TypeChecker
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
    # for t in tokens:
    #     print(t.tokenType, t.text, t.line, t.column)

    # Analizador Sintactico
    if len(tokenizer_errors) > 0:
        print_errors(tokenizer_errors)
        return
        
    parser = LRParser(G)
    tree = parser.parser(tokens, tokenizer_errors)
    astTree = tree.evaluate_attributes()
    
    # Analisis Semantico
    scope = Scope()
    semantics_errors = []
    scopeType = ScopeTypeChecker()
    type_checker = TypeChecker()
    check_ok = astTree.checkSemantic(scope)

    if check_ok:
        type_checker.visit(astTree, semantics_errors, scopeType)
        if len(semantics_errors) > 0:
            check_ok = False
            print_errors(semantics_errors)
    else:
        print_errors(semantics_errors) # errores del chequeo semantico

    print("chequeo",check_ok)

    # Ejecucion
    if check_ok:
        astTree.execute(scope)

    return

    manager = [Manager('Xavi', 'Espana', 0.7, 43), Manager('Zidane', 'Francia', 0.8, 46)]

    arbitros = [arbitro('Oscar', None, (0.7, 0.0001, 0.3, 0.005))]

    t1_name = ['messi', 'fati', 'depay', 'de jong', 'neymar', 'ansu fati', 'gavi', 'pedri', 'dembele', 'dani alves', 'eric garcia', 'ter stegen']
    t1_pos = [config.POSICIONES[0], config.POSICIONES[0], config.POSICIONES[0], config.POSICIONES[1], config.POSICIONES[2], config.POSICIONES[0], config.POSICIONES[1], config.POSICIONES[1], config.POSICIONES[2], config.POSICIONES[2], config.POSICIONES[2], config.POSICIONES[3]]
    t1_prob = [(0.75, 0.1, 0.8, 0.1, 0.1, 0.1, 0.6, 0.69, 0.2, 0.1, 0.01), (0.6, 0.1, 0.7, 0.1, 0.2, 0.1, 0.7, 0.69, 0.2, 0.1, 0.01), (0.7, 0.1, 0.75, 0.2, 0.05, 0.1, 0.7, 0.69, 0.2, 0.1, 0.01), (0.58, 0.1, 0.7, 0.2, 0.1, 0.1, 0.7,  0.69, 0.2, 0.1, 0.01), (0.73, 0.1, 0.81, 0.1, 0.09, 0.1, 0.7, 0.69, 0.2, 0.1, 0.01), (0.6, 0.1, 0.7, 0.1, 0.2, 0.1, 0.7, 0.69, 0.2, 0.1, 0.01), (0.6, 0.1, 0.7, 0.1, 0.2, 0.1, 0.7, 0.69, 0.2, 0.1, 0.01), (0.6, 0.1, 0.7, 0.1, 0.2, 0.1, 0.7, 0.69, 0.2, 0.1, 0.01), (0.6, 0.1, 0.7, 0.1, 0.2, 0.1, 0.7, 0.69, 0.2, 0.1, 0.01), (0.6, 0.1, 0.7, 0.1, 0.2, 0.1, 0.7, 0.69, 0.2, 0.1, 0.01), (0.6, 0.1, 0.7, 0.1, 0.2, 0.1, 0.7, 0.69, 0.2, 0.1, 0.01), (0.1, 0.6, 0.8, 0.1, 0.1, 0.01, 0.6, 0.69, 0.2, 0.1, 0.01, 0.5, 0.4, 0.3, 0.3)]
    t1_act_prob = [[0.999, 0.1, 0.7, 0.8, 0.75, 0.6, 0.8, 0.0001]]*12

    t2_name = ['ronaldo', 'mbappe', 'ramos', 'benzema', 'alaba', 'hazard', 'marcelo', 'dani carvajal', 'toni kroos',  'lukano dric', 'isco', 'courtoi']
    t2_pos = [config.POSICIONES[0], config.POSICIONES[0], config.POSICIONES[2], config.POSICIONES[1], config.POSICIONES[2], config.POSICIONES[0], config.POSICIONES[2], config.POSICIONES[2], config.POSICIONES[1], config.POSICIONES[1], config.POSICIONES[1], config.POSICIONES[3]]
    t2_prob = [(0.8, 0.1, 0.85, 0.1, 0.05, 0.1, 0.6, 0.69, 0.2, 0.1, 0.01), (0.62, 0.1, 0.7, 0.2, 0.1, 0.1, 0.7, 0.69, 0.2, 0.1, 0.01), (0.6, 0.1, 0.65, 0.2, 0.15, 0.1, 0.7, 0.69, 0.2, 0.1, 0.01), (0.6, 0.1, 0.76, 0.11, 0.13, 0.1, 0.7, 0.69, 0.2, 0.1, 0.01), (0.57, 0.1, 0.9, 0.5, 0.5, 0.1, 0.7, 0.69, 0.2, 0.1, 0.01),(0.6, 0.1, 0.7, 0.1, 0.2, 0.1, 0.7, 0.69, 0.2, 0.1, 0.01), (0.6, 0.1, 0.7, 0.1, 0.2, 0.1, 0.7, 0.69, 0.2, 0.1, 0.01), (0.6, 0.1, 0.7, 0.1, 0.2, 0.1, 0.7, 0.69, 0.2, 0.1, 0.01), (0.6, 0.1, 0.7, 0.1, 0.2, 0.1, 0.7, 0.69, 0.2, 0.1, 0.01), (0.6, 0.1, 0.7, 0.1, 0.2, 0.1, 0.7, 0.69, 0.2, 0.1, 0.01), (0.6, 0.1, 0.7, 0.1, 0.2, 0.1, 0.7, 0.69, 0.2, 0.1, 0.01), (0.1, 0.6, 0.8, 0.1, 0.1, 0.01, 0.6, 0.69, 0.2, 0.1, 0.01, 0.5, 0.4, 0.3, 0.3)]
    t2_act_prob = [[0.99, 0.1, 0.7, 0.8, 0.75, 0.6, 0.8, 0.0001]]*12

    t1 = []
    t2 = []
    length = len(t1_name)

    for i in range(length - 1):
        t1.append(Jugador(t1_name[i], t1_pos[i], t1_prob[i], t1_act_prob[i]))
        t2.append(Jugador(t2_name[i], t2_pos[i], t2_prob[i], t2_act_prob[i]))
    
    t1_portero_prob = [0.8, 0.4, 0.1, 0.2, 0.3]
    t2_portero_prob = [0.7, 0.4, 0.1, 0.3, 0.2]
    t1.append(Portero(t1_name[length - 1], t1_pos[length - 1], t1_prob[length - 1], t1_act_prob[length - 1], t1_portero_prob))
    t2.append(Portero(t2_name[length - 1], t2_pos[length - 1], t2_prob[length - 1], t2_act_prob[length - 1], t2_portero_prob))


    eq1 = Equipo("Barca", manager[0], t1)
    eq2 = Equipo("Madrid", manager[1], t2)


    p1 = Partido(eq1,eq2, arbitros)
    p1.simular()
    # n = 20
    # while n:
    #     n -= 1

def print_errors(errors):
    for e in errors:
        print(e)

if '__main__' == __name__:
    main()
