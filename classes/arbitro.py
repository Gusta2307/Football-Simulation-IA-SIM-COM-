from classes.agente import Agente
from act.act_arbitro.sacar_tarjeta import Sacar_tarjeta
from act.act_arbitro.cantar_falta import Cantar_falta
from act.default import Default
from compilacion.Ast.instructions.variables.declaration import Declaration
from config import Config
config = Config()

class arbitro(Agente, Declaration):
    def __init__(self, nombre, experiencia, list_prob):# no_canta_falta, declare_falta_leve, tarjeta_amarilla, tarjeta_roja) -> None:
        self.nombre = nombre
        self.experiencia = experiencia

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

    def escoger_accion(self, partido):
        if partido.ultima_accion.tipo == config.ACT_HACER_FALTA:
            return self.acciones['CANTAR_FALTA'][0]
        else:
            return Default(self)
