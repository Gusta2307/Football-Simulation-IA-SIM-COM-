from IA.range import RangeBool, RangeChoice, RangeFloat, RangeInt
from classes.arbitro import Arbitro
from classes.equipo import Equipo
from classes.jugador import Jugador
from classes.partido import Partido
from classes.portero import Portero
from classes.reporte import Reporte
from classes.manager import Manager



types = {
    "int" : int,
    "str" : str,
    "bool" : bool,
    "float" : float,
    "object" : object,
    "range" : range,
    "player" : Jugador,
    "team" : Equipo,
    "referee" : Arbitro,
    "manager" : Manager,
    "game" : Partido,
    "goalkeeper" : Portero,
    "rangeint" : RangeInt,
    "rangefloat" : RangeFloat,
    "rangebool" : RangeBool,
    "rangechoice" : RangeChoice,
    "report" : Reporte
    }