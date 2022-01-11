from classes.jugador import Jugador
from classes.equipo import Equipo
from classes.arbitro import arbitro
from classes.manager import Manager


types = {
    "int" : int,
    "str" : str,
    "bool" : bool,
    "float" : float,
    "player" : Jugador,
    "team" : Equipo,
    "referee" : arbitro,
    "manager" : Manager
}
