from classes.portero import Portero
from config import Config

_config = Config()

##      VALIDAR ESTRATEGIA ATAQUE       ##
######################################################################
##         PARTIDO EN JUEGO             ##

def validar_ataque_enjuego_ZA_ZC_1(partido, jugador): #jugador con balon
    return partido.pos_balon != None and partido.pos_balon == jugador


def validar_ataque_enjuego_ZA_ZC_2(partido, jugador): #jugador sin balon 
    return partido.pos_balon != jugador

 
def validar_ataque_enjuego_ZD_P_1(partido, jugador):
    return partido.pos_balon != None and partido.pos_balon == jugador and jugador is Portero #Portero con balon


def validar_ataque_enjuego_ZD_P_2(partido, jugador):
    return partido.pos_balon != None and partido.pos_balon != jugador and jugador is Portero #Portero sin balon 

        
def validar_ataque_enjuego_ZD_1(partido, jugador): 
    return partido.pos_balon != None and partido.pos_balon == jugador and not jugador is Portero #Jugador con balon


def validar_ataque_enjuego_ZD_2(partido, jugador):
    return partido.pos_balon != None and partido.pos_balon != jugador and not jugador is Portero #Jugador sin balon 


######################################################################
##         PARTIDO DETENIDO             ##

def validar_ataque_detenido_BB(partido, jugador): # Balon sale por la banda
    return partido.ultima_accion.tipo in [_config.BANDA, _config.REBOTE_BANDA, _config.DESPEJE_BANDA]

def validar_ataque_detenido_CF_ZA(partido, jugador): # Se canto falta
    return partido.ultima_accion.tipo == _config.ACT_CANTAR_FALTA and partido.ultima_accion.falta_jugador.ubc == _config.IA.Zona.ATAQUE

def validar_ataque_detenido_CF_ZC(partido, jugador): # Se canto falta
    return partido.ultima_accion.tipo == _config.ACT_CANTAR_FALTA and partido.ultima_accion.falta_jugador.ubc == _config.IA.Zona.CENTRO

def validar_ataque_detenido_CF_ZD(partido, jugador): # Se canto falta
    return partido.ultima_accion.tipo == _config.ACT_CANTAR_FALTA and partido.ultima_accion.falta_jugador.ubc == _config.IA.Zona.DEFENSA

def validar_ataque_detenido_BLF_1(partido, jugador): # Balon linea final y el equipo en ataque pierde el balon
    return partido.ultima_accion.tipo == _config.LINEA_FINAL #[_config.LINEA_FINAL, _config.REBOTE_LINEA_FINAL, _config.DESPEJE_LINEA_FINAL]:
        
def validar_ataque_detenido_BLF_2(partido, jugador): #balon linea final y el equipo en defensa fue el ultima en tocar el balon
    return partido.ultima_accion.tipo in [_config.REBOTE_LINEA_FINAL, _config.DESPEJE_LINEA_FINAL]
    
#############################################################################################################################
##         PARTIDO EN JUEGO              ##
##      VALIDAR ESTRATEGIA DEFENSA       ##

def validar_defensa_enjuego_ZA_ZC(partido, jugador):
    return True

def validar_defensa_enjuego_ZD_P_1(partido, jugador): #Jugador es un portero y se hace tiro a porteria
    return jugador is Portero and partido.ultima_accion.tipo == _config.ACT_TIRO_PORTERIA

def validar_defensa_enjuego_ZD_P_2(partido, jugador):#Jugador es un portero y no se hace tiro a porteria
    return jugador is Portero and partido.ultima_accion.tipo != _config.ACT_TIRO_PORTERIA

def validar_defensa_enjuego_ZD3(partido, jugador): #Jugador que no sea portero
    return not jugador is Portero 


######################################################################
##         PARTIDO DETENIDO             ##

def validar_defensa_detenido_CF_ZA(partido, jugador): #Se canto falta y zona de ataque
    return partido.ultima_accion.tipo == _config.ACT_CANTAR_FALTA and partido.ultima_accion.falta_jugador.ubc == _config.IA.Zona.ATAQUE

def validar_defensa_detenido_CF_ZC(partido, jugador): #Se canto falta y zona central
    return partido.ultima_accion.tipo == _config.ACT_CANTAR_FALTA and partido.ultima_accion.falta_jugador.ubc == _config.IA.Zona.CENTRAL

def validar_defensa_detenido_CF_ZD(partido, jugador): #Se canta falta y zona de defensa
    return partido.ultima_accion.tipo == _config.ACT_CANTAR_FALTA and partido.ultima_accion.falta_jugador.ubc == _config.IA.Zona.DEFENSA

def validar_defensa_detenido_BLF(partido, jugador): #balon por linea final 
    return partido.ultima_accion.tipo in [_config.LINEA_FINAL, _config.REBOTE_LINEA_FINAL, _config.DESPEJE_LINEA_FINAL]

def validar_defensa_detenido_BB(partido, jugador): #Balon sale por la banda
    return partido.ultima_accion.tipo in [_config.BANDA, _config.REBOTE_BANDA, _config.DESPEJE_BANDA]