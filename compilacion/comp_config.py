from IA.estrategia import Estrategia
from classes.manager import Manager

# import classes

class Config_C:
    class Player:
        args = {
            "name": str,
            "pos": str,
            "country": str,
            "age": int,
            "list_prob": list,
            "strategy": Estrategia
        }

    class Manager_:
        args = {
            "name": str,
            "country": str,
            "age": int,
            "experience": int,
            "strategy": Estrategia
        }

    class Goalkeeper:
        args = {
            "name": str,
            "country": str,
            "age": int,
            "pos": str,
            "list_prob": list,
            "goalkeeper_prob": list,
            "strategy": Estrategia
        }

    class Referee:
        args = {
            "name": str,
            "country": str,
            "age": int,
            "experience": int,
            "list_prob": list,
            "strategy": Estrategia
        }
    
    class Team:
        args = {
            "name": str,
            "country": str,
            "manager": Manager,
            "jugadores": list
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

    