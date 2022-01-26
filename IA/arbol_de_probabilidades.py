import abc
from config import Config
from classes.jugador import Jugador

_config = Config()

class AP(abc.ABC):
    @abc.abstractmethod
    def validar() -> bool: 
        pass


class IA(AP): 
    def __init__(self, hijos) -> None:
        super().__init__()
        self.hijos = hijos
        self.IA = "Equipo"

    def validar(self, partido) -> bool:
        pass

    def asignar_acciones(self, partido, equipo) -> list:
        pass


class Estrategia(AP):
    def __init__(self, estrategia, hijos) -> None:
        super().__init__()
        self.hijos = hijos
        self.estrategia = estrategia

    def validar(self, partido, equipo) -> bool:
        if partido.pos_balon != None:
            return partido.pos_balon.equipo == equipo
        
        if partido.ultima_accion.agente is Jugador:
            acciones = [_config.ACT_PASE, _config.ACT_SAQUE_BANDA, _config.ACT_SAQUE_ESQUINA, _config.ACT_SAQUE_FALTA, _config.ACT_TIRO_PORTERIA,  _config.ACT_SAQUE_PORTERIA]
            if partido.ultima_accion.agente.equipo == equipo:
                return partido.ultima_accion.tipo in acciones and self.estrategia ==  _config.IA.Estrategia.ATAQUE
            else:
                return not partido.ultima_accion.tipo in acciones and self.estrategia ==  _config.IA.Estrategia.DEFENSA
        else:
            if partido.ultima_accion.tipo == _config.CANTA_FALTA and partido.ultima_accion.estado == _config.CANTA_FALTA:
                if partido.ultima_accion.falta_jugador.equipo == equipo:
                    return self.estrategia == _config.IA.Estrategia.DEFENSA
                else:
                    return self.estrategia == _config.IA.Estrategia.ATAQUE


class Estado_P(AP):
    def __init__(self, estado, hijos) -> None:
        super().__init__()
        self.hijos = hijos
        self.estado = estado
    
    def validar(self, partido, equipo) -> bool:
        return partido.estado == self.estado 


        
class Zona(AP):
    def __init__(self, zona, hijos) -> None:
        super().__init__()
        self.hijos = hijos
        self.zona = zona

    def validar(self, partido, jugador) -> bool:
        if jugador.ubc != self.zona: # ubc: ubicacion en el campo del jugador
            return False
        return True
        

class Prob(AP):
    def __init__(self, axp, validar) -> None:
        super().__init__()
        # self.hijos = hijos  # Este nodo tienes hijos? :/
        self.accion_prob = axp
        self.validar = validar
    
    def validar(self, partido, equipo) -> bool:
        pass

    def lista_acciones(self) -> list:
        return self.accion_prob


class Comportamiento(AP):
    def __init__(self, comportamiento, validar) -> None:
        super().__init__()
        self.validar = validar

    def validar(self, partido, equipo) -> bool:
        pass
