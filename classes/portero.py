import random
import numpy
from act.act_portero.atajar import Atajar
from act.act_portero.saque_porteria import Saque_porteria
from classes.jugador import Jugador
from act.default import Default
from config import Config
config = Config()

class Portero(Jugador):
    def __init__(self, nombre, pos, list_prob, portero_prob, estrategia):
        super().__init__(nombre, pos, list_prob, estrategia)
        
        self.atajar_balon = portero_prob[0]
        self.sin_rebote = portero_prob[1]
        self.rebote_banda = portero_prob[2]
        self.rebote_linea_final = portero_prob[3]
        self.rebote_jugador = portero_prob[4]
        self.saque_porteria = list_prob[5]

        self.acciones.pop('SAQUE_BANDA')
        self.acciones.pop('DESPEJAR_BALON')

        self.acciones['ATAJAR'] = Atajar(self)
        self.acciones['SAQUE_PORTERIA'] = Saque_porteria(self)
        self.estrategia = estrategia


    def escoger_accion_estrategia(self, partido):
        estrategia_accion = None
        if self.estrategia != None: 
            estrategia_accion = self.acciones[self.estrategia.execute(partido, self, self.estrategia.variables)]
        
        return  estrategia_accion if estrategia_accion != None and estrategia_accion.precondicion(partido) else self.escoger_accion_agente(partido)
      


    def escoger_accion_agente(self, partido):
        if partido.ultima_accion.tipo == config.ACCIONES.JUGADOR.ACT_TIRO_PORTERIA and partido.estado == config.PARTIDO.ESTADO.EN_JUEGO:
            if self.acciones['ATAJAR'].precondicion(partido):
                return self.acciones['ATAJAR']
                
        if self.acciones['SAQUE_PORTERIA'].precondicion(partido):
                return self.acciones['SAQUE_PORTERIA']

        if partido.ultima_accion.tipo == config.ACCIONES.JUGADOR.ACT_ATAJAR and partido.ultima_accion.estado == config.ACCIONES.ESTADO.ATAJAR.SIN_REBOTE and self.acciones['PASE'].precondicion(partido):
            #El portero hace un pase a alguien de su equipo
            return self.acciones['PASE']

        acciones_posibles = list(filter(lambda x: x.precondicion(partido), [self.acciones['PASE'], self.acciones['HACER_FALTA'], self.acciones['INTERCEPCION'], self.acciones['RECIBIR_BALON']]))

        temp_p = []
        for item in acciones_posibles:
            if item.tipo == config.ACCIONES.JUGADOR.ACT_RECIBIR_BALON and partido.ultima_accion.tipo == config.ACCIONES.JUGADOR.ACT_PASE:  # VERIFICAR SI PUEDO RECIBIR BALON
                return item
            temp_p.append(0.3/len(acciones_posibles))
        temp_p.append(1 - sum(temp_p))
        act = numpy.random.choice(numpy.arange(0, len(temp_p)), p=temp_p)
        
        return Default(self) if act == len(temp_p) - 1 else acciones_posibles[act]