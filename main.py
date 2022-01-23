import os
from IA.estrategia import Estrategia
from IA.range import *
from IA.optimizador import Optimizador
from compilacion.analisis_semantico import *
from classes.equipo import Equipo
from classes.arbitro import arbitro
from classes.jugador import Jugador
from classes.manager import Manager
from classes.partido import Partido
from classes.portero import Portero
from compilacion.grammars.grammar import Grammar
from compilacion.grammars.production import Production
from compilacion.grammars.sentence import Sentence
from compilacion.parsing.grammar_items import ItemLR
from compilacion.parsing.lrparser import LRParser
from config import Config
from compilacion.parsing.firsts_follows import calculate_firsts, calculate_follows
from ejemplos import productions, S, E, terminales, no_terminales
from compilacion.parsing.defined_grammar import G
import copy


config = Config()


def read_script(name):
    cwd = os.getcwd()
    direction = os.path.join(cwd, "compilacion", "test",  name)
    file = open(direction, "r")
    line = file.read()
    file.close()
    return line

def main():
    # g = Grammar()
    # g.productions = productions
    # g.terminals = terminales
    # g.noTerminals = no_terminales
    # g.startNoTerminal = S
    # # g.startNoTerminal = E
    # firsts = calculate_firsts(g)
    # follows = calculate_follows(g)
    
    #lr_parser = LRParser(G)
    #print("")
    # for f in firsts.keys():
    #     print(f"first({f}) = {firsts[f]}")
    # print(" ")

    # for f in follows.keys():
    #     print(f"follow({f}) = {follows[f]}")
    # print(" ")


    # file_name = 'file0.txt'#input()
    # code = read_script(file_name).splitlines()
    # compiler = Compiling()
    # for token in compiler.Lexical.tokenize(code):
    #     print(token)

    manager = [Manager('Xavi', 'Espana', 0.7, 43), Manager('Zidane', 'Francia', 0.8, 46)]

    arbitros = [arbitro('Oscar', None, (0.7, 0.0001, 0.3, 0.005))]

    t1_name = ['messi', 'fati', 'depay', 'de jong', 'neymar', 'ansu fati', 'gavi', 'pedri', 'dembele', 'dani alves', 'eric garcia', 'ter stegen']
    t1_pos = [config.POSICIONES[0], config.POSICIONES[0], config.POSICIONES[0], config.POSICIONES[1], config.POSICIONES[2], config.POSICIONES[0], config.POSICIONES[1], config.POSICIONES[1], config.POSICIONES[2], config.POSICIONES[2], config.POSICIONES[2], config.POSICIONES[3]]
    t1_prob = [(0.75, 0.1, 0.8, 0.1, 0.1, 0.1, 0.6, 0.69, 0.2, 0.1, 0.01, 0.8), (0.6, 0.1, 0.7, 0.1, 0.2, 0.1, 0.7, 0.69, 0.2, 0.1, 0.01, 0.2), (0.7, 0.1, 0.75, 0.2, 0.05, 0.1, 0.7, 0.69, 0.2, 0.1, 0.01, 0.2), (0.58, 0.1, 0.7, 0.2, 0.1, 0.1, 0.7,  0.69, 0.2, 0.1, 0.01, 0.4), (0.73, 0.1, 0.81, 0.1, 0.09, 0.1, 0.7, 0.69, 0.2, 0.1, 0.01, 0.6), (0.6, 0.1, 0.7, 0.1, 0.2, 0.1, 0.7, 0.69, 0.2, 0.1, 0.01, 0.7), (0.6, 0.1, 0.7, 0.1, 0.2, 0.1, 0.7, 0.69, 0.2, 0.1, 0.01, 0.4), (0.6, 0.1, 0.7, 0.1, 0.2, 0.1, 0.7, 0.69, 0.2, 0.1, 0.01, 0.3), (0.6, 0.1, 0.7, 0.1, 0.2, 0.1, 0.7, 0.69, 0.2, 0.1, 0.01, 0.2), (0.6, 0.1, 0.7, 0.1, 0.2, 0.1, 0.7, 0.69, 0.2, 0.1, 0.01, 0.5), (0.6, 0.1, 0.7, 0.1, 0.2, 0.1, 0.7, 0.69, 0.2, 0.1, 0.01, 0.5), (0.1, 0.6, 0.8, 0.1, 0.1, 0.01, 0.6, 0.69, 0.2, 0.1, 0.01, 0.5, 0.4, 0.3, 0.3, 0.3J)]
    #t1_act_prob = [[0.999, 0.1, 0.7, 0.8, 0.75, 0.6, 0.8, 0.0001]]*12

    def f(a):
        return a
    
    def g():
        return RangeFloat(9, 4)
    variables_t1 = {'PASE': 3, 'TIRO': RangeInt(3, 5),'INTERCEPCION': RangeBool(f), 'HACER_FALTA': True, 'RECIBIR_BALON' : g(), 'SAQUE_BANDA': RangeChoice(["pepe", 4, 6])}
    
    def execute_t1(partido, jugador, variables):
        if partido.pos_balon != None and partido.pos_balon == jugador and  variables['PASE'] > 2 and variables["TIRO"] == 1:
            return "PASE"
        elif variables['INTERCEPCION']:
            return "HACER_FALTA"
        else:
            return "TIRO"


    t1_act = Estrategia(variables_t1, execute_t1)

    t2_name = ['ronaldo', 'mbappe', 'ramos', 'benzema', 'alaba', 'hazard', 'marcelo', 'dani carvajal', 'toni kroos',  'lukano dric', 'isco', 'courtoi']
    t2_pos = [config.POSICIONES[0], config.POSICIONES[0], config.POSICIONES[2], config.POSICIONES[1], config.POSICIONES[2], config.POSICIONES[0], config.POSICIONES[2], config.POSICIONES[2], config.POSICIONES[1], config.POSICIONES[1], config.POSICIONES[1], config.POSICIONES[3]]
    t2_prob = [(0.8, 0.1, 0.85, 0.1, 0.05, 0.1, 0.6, 0.69, 0.2, 0.1, 0.01, 0.3), (0.62, 0.1, 0.7, 0.2, 0.1, 0.1, 0.7, 0.69, 0.2, 0.1, 0.01, 0.3), (0.6, 0.1, 0.65, 0.2, 0.15, 0.1, 0.7, 0.69, 0.2, 0.1, 0.01, 0.3), (0.6, 0.1, 0.76, 0.11, 0.13, 0.1, 0.7, 0.69, 0.2, 0.1, 0.01, 0.3), (0.57, 0.1, 0.9, 0.5, 0.5, 0.1, 0.7, 0.69, 0.2, 0.1, 0.01, 0.3),(0.6, 0.1, 0.7, 0.1, 0.2, 0.1, 0.7, 0.69, 0.2, 0.1, 0.01, 0.3), (0.6, 0.1, 0.7, 0.1, 0.2, 0.1, 0.7, 0.69, 0.2, 0.1, 0.01, 0.3), (0.6, 0.1, 0.7, 0.1, 0.2, 0.1, 0.7, 0.69, 0.2, 0.1, 0.01, 0.3), (0.6, 0.1, 0.7, 0.1, 0.2, 0.1, 0.7, 0.69, 0.2, 0.1, 0.01, 0.3), (0.6, 0.1, 0.7, 0.1, 0.2, 0.1, 0.7, 0.69, 0.2, 0.1, 0.01, 0.3), (0.6, 0.1, 0.7, 0.1, 0.2, 0.1, 0.7, 0.69, 0.2, 0.1, 0.01, 0.3), (0.1, 0.6, 0.8, 0.1, 0.1, 0.01, 0.6, 0.69, 0.2, 0.1, 0.01, 0.5, 0.4, 0.3, 0.3, 0.3)]
    #t2_act_prob = [[0.99, 0.1, 0.7, 0.8, 0.75, 0.6, 0.8, 0.0001]]*12

    t1 = []
    t2 = []
    length = len(t1_name)

    for i in range(length - 1):
        t1.append(Jugador(t1_name[i], t1_pos[i], t1_prob[i], copy.deepcopy(t1_act)))
        t2.append(Jugador(t2_name[i], t2_pos[i], t2_prob[i], copy.deepcopy(t1_act)))
    
    t1_portero_prob = [0.8, 0.4, 0.1, 0.2, 0.3, 0.6]
    t2_portero_prob = [0.7, 0.4, 0.1, 0.3, 0.2, 0.7]
    t1.append(Portero(t1_name[length - 1], t1_pos[length - 1], t1_prob[-1], t1_portero_prob, t1_act))
    t2.append(Portero(t2_name[length - 1], t2_pos[length - 1], t2_prob[-1], t2_portero_prob, t1_act))


    eq1 = Equipo("Barca", manager[0], t1)
    eq2 = Equipo("Madrid", manager[1], t2)

    print("Aqui")
    p1 = Partido(eq1,eq2, arbitros)
    print("termine")
    #p1.simular()
    #p1.simular()
    # n = 20
    # while n:
    #     n -= 1


if '__main__' == __name__:
    main()
