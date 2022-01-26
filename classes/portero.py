import random
import numpy
from act.act_portero.atajar import Atajar
from act.act_portero.saque_porteria import Saque_porteria
from classes.jugador import Jugador
from act.default import Default
from config import Config
config = Config()

class Portero(Jugador):
    def __init__(self, nombre, pos, list_prob, list_act_prob, portero_prob):
        super().__init__(nombre, pos, list_prob, list_act_prob)
        
        self.atajar_balon = portero_prob[0]
        self.sin_rebote = portero_prob[1]
        self.rebote_banda = portero_prob[2]
        self.rebote_linea_final = portero_prob[3]
        self.rebote_jugador = portero_prob[4]
        self.saque_porteria = list_prob[5]

        self.acciones.pop('SAQUE_BANDA')
        self.acciones.pop('DESPEJAR_BALON')

        self.acciones['ATAJAR'] = (Atajar(self), self.atajar_balon)
        self.acciones['SAQUE_PORTERIA'] = (Saque_porteria(self), self.saque_porteria)



    def escoger_accion(self, partido):
        if partido.ultima_accion.tipo == config.ACT_TIRO_PORTERIA and partido.estado == config.EN_JUEGO:
            if self.acciones['ATAJAR'][0].precondicion(partido):
                return self.acciones['ATAJAR'][0]
                
        if self.acciones['SAQUE_PORTERIA'][0].precondicion(partido):
                return self.acciones['SAQUE_PORTERIA'][0]

        if partido.ultima_accion.tipo == config.ACT_ATAJAR and partido.ultima_accion.estado == config.SIN_REBOTE and self.acciones['PASE'][0].precondicion(partido):
            #El portero hace un pase a alguien de su equipo
            return self.acciones['PASE'][0]

        acciones_posibles = list(filter(lambda x: x[0].precondicion(partido), [self.acciones['PASE'], self.acciones['HACER_FALTA'], self.acciones['INTERCEPCION'], self.acciones['RECIBIR_BALON']]))

        temp_p = []
        for item in acciones_posibles:
            if item[0].tipo == config.ACT_RECIBIR_BALON and partido.ultima_accion.tipo == config.ACT_PASE:  # VERIFICAR SI PUEDO RECIBIR BALON
                return item[0]
            temp_p.append(item[1]/len(acciones_posibles))
        temp_p.append(1 - sum(temp_p))
        act = numpy.random.choice(numpy.arange(0, len(temp_p)), p=temp_p)
        
        return Default(self) if act == len(temp_p) - 1 else acciones_posibles[act][0]