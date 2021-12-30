import random
import numpy
from act.default import Default
from act.act_jugador.pase import Pase
from act.act_jugador.tiro_porteria import Tiro_Porteria
from act.act_jugador.interceptar_balon import Interceptar_balon
from act.act_jugador.hacer_falta import Hacer_Falta
from act.act_jugador.recibir_balon import Recibir_balon
from act.act_jugador.saque_banda import Saque_banda
from act.act_jugador.saque_esquina import Saque_esquina
from act.act_jugador.saque_falta import Saque_falta
from act.act_jugador.despejar_balon import Despejar_balon
from classes.agente import Agente
from compilacion.analisis_semantico.Ast.instructions.variables.declaration import Declaration
from config import Config
config = Config()


class Jugador(Agente, Declaration):
    def __init__(self, nombre, pos, list_prob, list_act_prob):#  gol_p, atajar_p, pase_efectivo_p, pase_largo_p, pase_intercep_p, gol_partido, atajar_partido, no_falta, falta_leve, falta_amarilla, falta_roja, pos_array) -> None:
        self.nombre = nombre
        self.posicion = pos
        self.equipo = None
        

        #Las prob de que se realicen satisfactoriamente
        self.tiro_porteria = list_prob[0]
        self.pase = list_prob[1]
        self.interceptar_balon = list_prob[2]
        self.recibir_balon = list_prob[3]
        self.saque_banda = list_prob[4]
        self.saque_esquina = list_prob[5]
        self.despejar_balon = list_prob[6]
        
        #Las probabilidades con prefijo act son las prob de que se realice una accion 
        self.act_tiro_porteria = list_act_prob[0] 
        self.act_pase = list_act_prob[1]
        self.act_interceptar_balon = list_act_prob[2]
        self.act_recibir_balon = list_act_prob[3]
        self.act_saque_banda = list_act_prob[4]
        self.act_saque_esquina = list_act_prob[5]
        self.act_despejar_balon = list_act_prob[6]
        self.act_hacer_falta = list_act_prob[7]
      
        self.falta_leve = list_prob[8]
        self.falta_moderada = list_prob[9]
        self.falta_grave = list_prob[10]
        self.no_falta = 1 - (self.falta_leve + self.falta_moderada + self.falta_grave)

        self.cantidad_tarjetas = 0   
        
        self.acciones = self.acciones_dict()

     
    def acciones_dict(self) -> dict:
        return {
            'PASE': (Pase(self), self.act_pase),
            'TIRO': (Tiro_Porteria(self), self.act_tiro_porteria),
            'INTERCEPCION': (Interceptar_balon(self), self.act_interceptar_balon),
            'HACER_FALTA': (Hacer_Falta(self), self.act_hacer_falta),
            'RECIBIR_BALON' : (Recibir_balon(self), self.act_recibir_balon),
            'SAQUE_BANDA': (Saque_banda(self), self.act_saque_banda),
            'SAQUE_ESQUINA': (Saque_esquina(self), self.act_saque_esquina),
            'SAQUE_FALTA': (Saque_falta(self), 0.5),  #NO SE SI SE DEBERIA PONER UNA PROB DE SACAR FALTA
            
            
            'DESPEJAR_BALON': (Despejar_balon(self), self.act_despejar_balon)
        }

    def escoger_accion(self, partido):
        if partido.estado == config.INICIAR_PARTIDO or partido.estado == config.REANUDAR_PARTIDO:
            if self.acciones['PASE'][0].precondicion(partido) and partido.pos_balon == self:
                return self.acciones['PASE'][0]
            
        acciones_posibles = list(filter(lambda x: x[0].precondicion(partido), self.acciones.values()))

        temp_p = []
        for item in acciones_posibles:
            # print(item, acciones_posibles)
            if item[0].tipo == config.ACT_RECIBIR_BALON and partido.ultima_accion.tipo == config.ACT_PASE:  # VERIFICAR SI PUEDO RECIBIR BALON
                return item[0]
            temp_p.append(item[1]/len(acciones_posibles))

        temp_p.append(1 - sum(temp_p))
        act = numpy.random.choice(numpy.arange(0, len(temp_p)), p=temp_p)
        
        return Default(self) if act == len(temp_p) - 1 else acciones_posibles[act][0]
     

    def seleccionar_jugador_pase(self, partido):
        index = -1
        if self.posicion == 'DEL':
            index = numpy.random.choice(numpy.arange(0, 4), p=[0.5,   0.35,   0.1,  0.05])
        elif self.posicion == 'MC':
            index = numpy.random.choice(numpy.arange(0, 4), p=[0.4,   0.3,   0.2,  0.1])
        elif self.posicion == 'DEF':
            index = numpy.random.choice(numpy.arange(0, 4), p=[0.05,   0.4,   0.25,  0.3])
        elif self.posicion == 'GK':
            index = numpy.random.choice(numpy.arange(0, 3), p=[0.3,   0.3,   0.4])

        temp_list = []
        for item in self.equipo.jugadores_en_campo:
            if item.posicion == config.POSICIONES[index]:
                temp_list.append(item)
        jugador2 = temp_list[int(random.randint(0, len(temp_list)- 1))]

        if jugador2 == self:
            return self.seleccionar_jugador_pase(partido)
        
        return jugador2

    def __eq__(self, jugador) -> bool:
        return (self.nombre == jugador.nombre and self.posicion == jugador.posicion and self.equipo == jugador.equipo)
        
    def __str__(self) -> str:
        return self.nombre