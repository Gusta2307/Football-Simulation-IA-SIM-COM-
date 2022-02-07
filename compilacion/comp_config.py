from IA.estrategia import Estrategia
from classes.equipo import Equipo
from classes.manager import Manager
from classes.jugador import Jugador

# import classes

class Config_C:
    class Player:
        args = {
            "name": str,
            "pos": str,
            "country": str,
            "age": int,
            "list_prob": list,
            "st": Estrategia
        }

    class Manager_:
        args = {
            "name": str,
            "country": str,
            "age": int,
            "experience": int,
            "st": Estrategia
        }

    class Goalkeeper:
        args = {
            "name": str,
            "country": str,
            "age": int,
            "pos": str,
            "list_prob": list,
            "goalkeeper_prob": list,
            "st": Estrategia
        }

    class Referee:
        args = {
            "name": str,
            "country": str,
            "age": int,
            "experience": int,
            "list_prob": list,
            "st": Estrategia
        }
    
    class Game:
        args = {
            'eq1': Equipo,
            'eq2': Equipo,
            'referees': list
        }

    class Team:
        args = {
            "name": str,
            "country": str,
            "manager": Manager,
            "players": list
        }

    class RangeInt:
        args = {
            "li": int,
            "ls": int,
        }

    class RangeFloat:
        args = {
            "li": float,
            "ls": float,
        }

    class RangeChoice:
        args = {
            "valores": list
        }

    