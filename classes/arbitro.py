from classes.agente import Agente
from act.act_arbitro.sacar_tarjeta import Sacar_tarjeta
from act.act_arbitro.cantar_falta import Cantar_falta
from act.default import Default
#from compilacion.analisis_semantico.Ast.instructions.variables.declaration import Declaration
from config import Config
config = Config()

class Arbitro(Agente): #(Agente, Declaration):
    def __init__(self, name, country, age, experience, list_prob, st = None):# no_canta_falta, declare_falta_leve, tarjeta_amarilla, tarjeta_roja) -> None:
        self.nombre = name
        self.experiencia = experience
        self.pais = country
        self.edad = age
        
        self.estrategia = st
        
        self.cantar_falta = list_prob[0]
        self.sacar_tarjeta = list_prob[1]
        self.sacar_tarjeta_amarilla = list_prob[2]
        self.sacar_tarjeta_roja = list_prob[3]

        self.acciones = self.acciones_dict()

     
    def acciones_dict(self) -> dict:
        return {
            'SACAR_TARJETA': (Sacar_tarjeta(self), self.sacar_tarjeta),
            'CANTAR_FALTA': (Cantar_falta(self), self.cantar_falta)
        }

    def escoger_accion_base(self, partido):
        if partido.ultima_accion.tipo == config.ACCIONES.JUGADOR.ACT_HACER_FALTA:
            return self.acciones['CANTAR_FALTA'][0]
        else:
            return Default(self)

    def escoger_accion_estrategia(self, partido):
        estrategia_accion = None
        if self.estrategia != None: 
            estrategia_accion = self.acciones[config.TRADUCTOR_ACT.ACT[self.estrategia.evaluar(partido, self)]]
        
        return  estrategia_accion if estrategia_accion != None and estrategia_accion.precondicion(partido) else self.escoger_accion_base(partido)
