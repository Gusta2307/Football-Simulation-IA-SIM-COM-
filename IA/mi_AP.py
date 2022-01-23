from arbol_de_probabilidades import *
from validar import *
from config import Config
from comportamiento import *

_config = Config()

####       PARTIDO EN JUEGO        ####
##      PORTERO        ##
# con tiro a porteria
defensa_enjuego_ZD_P_1 = Prob(
    [
        ['ATAJAR', 0.6],
        ['HACER_FALTA', 0.1],
        ['MANTENER_POS', 0.4]
    ],
    validar=validar_defensa_enjuego_ZD_P_1
)

# sin tiro a porteria
defensa_enjuego_ZD_P_2 = Prob(
    [
        ['INTERCEPCION', 0.1],
        ['HACER_FALTA', 0.05],
        ['MANTENER_POS', 0.85]
    ],
    validar = validar_defensa_enjuego_ZD_P_2
)

#######################################
##     JUGADOR      ##
# ZONA DEFENSA
defensa_enjuego_ZD3 = Prob(
    [
        ['INTERCEPCION', 0.3],
        ['HACER_FALTA', 0.25],
        ['MANTENER_POS', 0.3],
        ['AVANZAR_POS', 0.3]
    ],
    validar = validar_defensa_enjuego_ZD3
)

#ZONA CENTRAL
defensa_enjuego_ZC = Prob(
    [
        ['INTERCEPCION', 0.25],
        ['HACER_FALTA', 0.15],
        ['MANTENER_POS', 0.2],
        ['AVANZAR_POS', 0.15],
        ['RETRASAR_POS', 0.15]
    ],
    validar = validar_defensa_enjuego_ZA_ZC
)

#ZONA ATAQUE
defensa_enjuego_ZA = Prob(
    [
        ['INTERCEPCION', 0.15],
        ['HACER_FALTA', 0.2],
        ['MANTENER_POS', 0.2],
        ['RETRAZAR_POS', 0.35]
    ],
    validar = validar_defensa_enjuego_ZA_ZC
)


###         PARTIDO DETENIDO        ###


#Balon sale por la banda
defensa_detenido_BB = Comportamiento(
    validar = validar_defensa_detenido_BB, 
    comportamiento  = comportamiento_defensa_detenido_BB
)

#Balon por linea final 
defensa_detenido_BLF = Comportamiento(
    validar = validar_defensa_detenido_BLF,
    comportamiento = comportamiento_defensa_detenido_BLF
)

#Se canto falta y zona de ataque
defensa_detenido_CF_ZA = Comportamiento(
    validar = validar_defensa_detenido_CF_ZA,
    comportamiento = comportamiento_defensa_detenido_CF_ZA
)

#Se canto falta y zona central
defensa_detenido_CF_ZC = Comportamiento(
    validar = validar_defensa_detenido_CF_ZC,
    comportamiento = comportamiento_defensa_detenido_CF_ZC
)

#Se canta falta y zona de defensa
defensa_detenido_CF_ZD = Comportamiento(
    validar = validar_defensa_detenido_CF_ZD,
    comportamiento = comportamiento_defensa_detenido_CF_ZD
)

#balon por linea final 
defensa_detenido_BLF = Comportamiento(
    validar=validar_defensa_detenido_BLF,
    comportamiento = comportamiento_defensa_detenido_BLF
)


#####################################################################################
####       PARTIDO EN JUEGO        ####
###       ATAQUE        ###
##      ZONA DENFENSA    ##
#Portero con balon 
ataque_enjuego_ZD_P_1 = Prob(
    [
        ['PASE', 0.7],
        ['HACER_FALTA', 0.05],
        ['MANTENER_POS', 0.2],
        ['AVANZAR_POS', 0.05]
    ],
    validar = validar_ataque_enjuego_ZD_P_1
)

#Portero sin balon 
ataque_enjuego_ZD_P_2 = Prob(
    [
        ['MANTENER_POS', 0.8],
        ['RECIBIR_BALON', 0.2]
    ],
    validar = validar_ataque_enjuego_ZD_P_2
)

#Jugador con balon
ataque_enjuego_ZD_1 = Prob(
    [
        ['PASE', 0.5],
        ['HACER_FALTA', 0.1],
        ['MANTENER_POS', 0.15],
        ['AVANZAR_POS', 0.25]
    ],
    validar = validar_ataque_enjuego_ZD_1
)

#Jugador sin balon 
ataque_enjuego_ZD_2 = Prob(
    [
        ['RECIBIR_BALON', 0.4],
        ['HACER_FALTA', 0.15],
        ['MANTENER_POS', 0.25],
        ['AVANZAR_POS', 0.2]
    ],
    validar = validar_ataque_enjuego_ZD_2
)

##      ZONA CENTRAL      ##

 #jugador con balon
ataque_enjuego_ZC_1 = Prob(
    [
        ['PASE', 0.4],
        ['HACER_FALTA', 0.05],
        ['MANTENER_POS', 0.2],
        ['AVANZAR_POS', 0.25],
        ['RETRASAR_POS', 0.15]
    ],
    validar = validar_ataque_enjuego_ZA_ZC_1
)

#jugador sin balon
ataque_enjuego_ZC_2 = Prob(
    [
        ['RECIBIR_BALON', 0.4],
        ['HACER_FALTA', 0.05],
        ['MANTENER_POS', 0.2],
        ['AVANZAR_POS', 0.2],
        ['RETRASAR_POS', 0.15]
    ],
    validar = validar_ataque_enjuego_ZA_ZC_2
)

##      ZONA ATAQUE      ##

#jugador con balon 
ataque_enjuego_ZA_1 = Prob(
    [
        ['TIRO', 0.3],
        ['HACER_FALTA', 0.05],
        ['MANTENER_POS', 0.15],
        ['PASE', 0.35],
        ['RETRASAR_POS', 0.15]
    ],
    validar = validar_ataque_enjuego_ZA_ZC_1
)

#jugador sin balon
ataque_enjuego_ZA_2 = Prob(
    [
        ['RECIBIR_BALON', 0.4],
        ['HACER_FALTA', 0.05],
        ['MANTENER_POS', 0.25],
        ['AVANZAR_POS', 0.2]
    ],
    validar = validar_ataque_enjuego_ZA_ZC_2
)

###         PARTIDO DETENIDO        ###

# Balon sale por la banda
ataque_detenido_BB = Comportamiento(
    validar = validar_ataque_detenido_BB,
    comportamiento = comportamiento_ataque_detenido_BB
)

# Se canto falta 
ataque_detenido_CF_ZA = Comportamiento(
    validar = validar_ataque_detenido_CF_ZA,
    comportamiento = comportamiento_ataque_detenido_CF_ZA
)

 # Se canto falta
ataque_detenido_CF_ZC = Comportamiento(
    validar = validar_ataque_detenido_CF_ZC,
    comportamiento = comportamiento_ataque_detenido_CF_ZC
)

# Se canto falta
ataque_detenido_CF_ZD = Comportamiento(
    validar = validar_ataque_detenido_CF_ZD,
    comportamiento = comportamiento_ataque_detenido_CF_ZD
)

# Balon linea final y el equipo en ataque pierde el balon
ataque_detenido_BLF_1 = Comportamiento(
    validar = validar_ataque_detenido_BLF_1,
    comportamiento = comportamiento_ataque_detenido_BLF_1
)

#balon linea final y el equipo en defensa fue el ultima en tocar el balon
ataque_detenido_BLF_2 = Comportamiento(
    validar = validar_ataque_detenido_BLF_2,
    comportamiento = comportamiento_ataque_detenido_BLF_2
)


###################         ZONA        ############################

defensa_enjuego_defensa = Zona(
    zona = _config.IA.Zona.DEFENSA,
    hijos = [defensa_enjuego_ZD_P_1, defensa_enjuego_ZD_P_2, defensa_enjuego_ZD3]
)

defensa_enjuego_centro = Zona(
    zona = _config.IA.Zona.CENTRO,
    hijos = [defensa_enjuego_ZC]
)

defensa_enjuego_ataque = Zona(
    zona = _config.IA.Zona.ATAQUE,
    hijos = [defensa_enjuego_ZA]
)

ataque_enjuego_defensa = Zona(
    zona = _config.IA.Zona.DEFENSA,
    hijos = [
        ataque_enjuego_ZD_P_1,
        ataque_enjuego_ZD_P_2,
        ataque_enjuego_ZD_1, 
        ataque_enjuego_ZD_2
    ]
)

ataque_enjuego_centro = Zona(
    zona = _config.IA.Zona.CENTRO,
    hijos = [ataque_enjuego_ZC_1,ataque_enjuego_ZC_2]
)

ataque_enjuego_ataque = Zona(
    zona = _config.IA.Zona.ATAQUE,
    hijos = [ataque_enjuego_ZA_1,ataque_enjuego_ZA_2]
)

###################         ESTADOS DEL PARTIDO        ############################

defensa_enjuego = Estado_P(
    estado = _config.EN_JUEGO,
    hijos = [
        defensa_enjuego_defensa,
        defensa_enjuego_centro,
        defensa_enjuego_ataque
    ]
)

defensa_detenido = Estado_P(
    estado = _config.DETENIDO,
    hijos = [
        defensa_detenido_BB,
        defensa_detenido_BLF,
        defensa_detenido_CF_ZA,
        defensa_detenido_CF_ZC,
        defensa_detenido_CF_ZD,
        defensa_detenido_BLF,
        defensa_detenido_BB
    ]
)

ataque_enjuego = Estado_P(
    estado = _config.EN_JUEGO,
    hijos = [
        ataque_enjuego_defensa,
        ataque_enjuego_centro,
        ataque_enjuego_ataque
    ]
)

ataque_detenido = Estado_P(
    estado = _config.DETENIDO,
    hijos = [
        ataque_detenido_BB,
        ataque_detenido_CF_ZA,
        ataque_detenido_CF_ZC,
        ataque_detenido_CF_ZD,
        ataque_detenido_BLF_1,
        ataque_detenido_BLF_2
    ]
)

###################         ESTRATEGIA        ############################

defensa = Estrategia(
    estrategia = _config.IA.Estrategia.DEFENSA,
    hijos = [defensa_enjuego,defensa_detenido]
)

ataque = Estrategia(
    estrategia = _config.IA.Estrategia.ATAQUE,
    hijos = [ataque_enjuego,ataque_detenido]
)

ia = IA(
    hijos = [defensa, ataque]
)