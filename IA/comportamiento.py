import random
from classes.jugador import Jugador
from classes.portero import Portero
from config import Config

_config = Config()


####            DEFENSA         ####
#Los jugadores avanzan o retrasan su posición según la zona donde se produce el saque de banda 
def comportamiento_defensa_detenido_BB(partido, equipo): 
    zona_actual = partido.ultima_accion.agente.ubc
    jugador_acciones = []
    for j in equipo.jugadores_en_campo:
        if j is Portero:
            jugador_acciones.append(
                            [
                                j,
                                [
                                    ['MANTENER_POS', 1]
                                ]
                            ]
            )
            continue
           
        if zona_actual == _config.IA.Zona.DEFENSA:
            if j.ubc == _config.IA.Zona.ATAQUE:
                if j.posicion == _config.POSICIONES[0]: #Delantero
                    jugador_acciones.append(
                        [
                            j,
                            [
                                ['RETRASAR_POS', 0.8],
                                ['MANTENER_POS', 0.2]
                            ]
                        ]
                    )
                elif j.posicion == _config.POSICIONES[1]: #Medio campo
                    jugador_acciones.append(
                        [
                            j,
                            [
                                ['RETRASAR_POS', 0.65],
                                ['MANTENER_POS', 0.35]
                            ]
                        ]
                    )
                elif j.posicion == _config.POSICIONES[2]: #Defensa
                    jugador_acciones.append(
                        [
                            j,
                            [
                                ['RETRASAR_POS', 0.95],
                                ['MANTENER_POS', 0.05]
                            ]
                        ]
                    )
                    
            elif j.ubc == _config.IA.Zona.CENTRO:
                if j.posicion == _config.POSICIONES[0]: #Delantero
                    jugador_acciones.append(
                        [
                            j,
                            [
                                ['AVANZAR_POS', 0.2],
                                ['RETRASAR_POS', 0.2],
                                ['MANTENER_POS', 0.6]
                            ]

                        ]
                    )
                elif j.posicion == _config.POSICIONES[1]: #Medio campo
                    jugador_acciones.append(
                        [
                            j,
                            [
                                ['AVANZAR_POS', 0.1],
                                ['RETRASAR_POS', 0.35],
                                ['MANTENER_POS', 0.55]
                            ]

                        ]
                    )
                elif j.posicion == _config.POSICIONES[2]: #Defensa
                    jugador_acciones.append(
                        [
                            j,
                            [
                                ['AVANZAR_POS', 0.05],
                                ['RETRASAR_POS', 0.65],
                                ['MANTENER_POS', 0.35]
                            ]

                        ]
                    )
            
            elif j.ubc == _config.IA.Zona.DEFENSA:
                if j.posicion == _config.POSICIONES[0]: #Delantero
                    jugador_acciones.append(
                        [
                            j,
                            [
                                ['AVANZAR_POS', 0.75],
                                ['MANTENER_POS', 0.25]
                            ]

                        ]
                    )
                elif j.posicion == _config.POSICIONES[1]: #Medio campo
                    jugador_acciones.append(
                        [
                            j,
                            [
                                ['AVANZAR_POS', 0.45],
                                ['MANTENER_POS', 0.55]
                            ]

                        ]
                    )
                elif j.posicion == _config.POSICIONES[2]: #Defensa
                    jugador_acciones.append(
                        [
                            j,
                            [
                                ['AVANZAR_POS', 0.05],
                                ['MANTENER_POS', 0.95]
                            ]

                        ]
                    )

        elif zona_actual == _config.IA.Zona.CENTRO:
            if j.ubc == _config.IA.Zona.ATAQUE:
                if j.posicion == _config.POSICIONES[0]: #Delantero
                    jugador_acciones.append(
                        [
                            j,
                            [
                                ['RETRASAR_POS', 0.35],
                                ['MANTENER_POS', 0.65]
                            ]

                        ]
                    )
                elif j.posicion == _config.POSICIONES[1]: #Medio campo
                    jugador_acciones.append(
                        [
                            j,
                            [
                                ['RETRASAR_POS', 0.65],
                                ['MANTENER_POS', 0.35]
                            ]

                        ]
                    )
                elif j.posicion == _config.POSICIONES[2]: #Defensa
                    jugador_acciones.append(
                        [
                            j,
                            [
                                ['RETRASAR_POS', 0.85],
                                ['MANTENER_POS', 0.15]
                            ]

                        ]
                    )
            
            elif j.ubc == _config.IA.Zona.CENTRO:
                if j.posicion == _config.POSICIONES[0]: #Delantero
                    jugador_acciones.append(
                        [
                            j,
                            [
                                ['AVANZAR_POS', 0.2],
                                ['RETRASAR_POS', 0.05],
                                ['MANTENER_POS', 0.75]
                            ]

                        ]
                    )
                elif j.posicion == _config.POSICIONES[1]: #Medio campo
                    jugador_acciones.append(
                        [
                            j,
                            [
                                ['AVANZAR_POS', 0.1],
                                ['RETRASAR_POS', 0.1],
                                ['MANTENER_POS', 0.8]
                            ]

                        ]
                    )
                elif j.posicion == _config.POSICIONES[2]: #Defensa
                    jugador_acciones.append(
                        [
                            j,
                            [
                                ['AVANZAR_POS', 0.05],
                                ['RETRASAR_POS', 0.65],
                                ['MANTENER_POS', 0.3]
                            ]

                        ]
                    )
            
            elif j.ubc == _config.IA.Zona.DEFENSA:
                if j.posicion == _config.POSICIONES[0]: #Delantero
                    jugador_acciones.append(
                        [
                            j,
                            [
                                ['AVANZAR_POS', 0.85],
                                ['MANTENER_POS', 0.15]
                            ]

                        ]
                    )
                elif j.posicion == _config.POSICIONES[1]: #Medio campo
                    jugador_acciones.append(
                        [
                            j,
                            [
                                ['AVANZAR_POS', 0.65],
                                ['MANTENER_POS', 0.35]
                            ]

                        ]
                    )
                elif j.posicion == _config.POSICIONES[2]: #Defensa
                    jugador_acciones.append(
                        [
                            j,
                            [
                                ['AVANZAR_POS', 0.25],
                                ['MANTENER_POS', 0.75]
                            ]

                        ]
                    )
                    
        elif zona_actual == _config.IA.Zona.ATAQUE:
            if j.ubc == _config.IA.Zona.ATAQUE:
                if j.posicion == _config.POSICIONES[0]: #Delantero
                    jugador_acciones.append(
                        [
                            j,
                            [
                                ['RETRASAR_POS', 0.05],
                                ['MANTENER_POS', 0.95]
                            ]

                        ]
                    )
                elif j.posicion == _config.POSICIONES[1]: #Medio campo
                    jugador_acciones.append(
                        [
                            j,
                            [
                                ['RETRASAR_POS', 0.35],
                                ['MANTENER_POS', 0.65]
                            ]

                        ]
                    )
                elif j.posicion == _config.POSICIONES[2]: #Defensa
                    jugador_acciones.append(
                        [
                            j,
                            [
                                ['RETRASAR_POS', 0.65],
                                ['MANTENER_POS', 0.35]
                            ]

                        ]
                    )
            
            elif j.ubc == _config.IA.Zona.CENTRO:
                if j.posicion == _config.POSICIONES[0]: #Delantero
                    jugador_acciones.append(
                        [
                            j,
                            [
                                ['AVANZAR_POS', 0.65],
                                ['RETRASAR_POS', 0.05],
                                ['MANTENER_POS', 0.3]
                            ]

                        ]
                    )
                elif j.posicion == _config.POSICIONES[1]: #Medio campo
                    jugador_acciones.append(
                        [
                            j,
                            [
                                ['AVANZAR_POS', 0.25],
                                ['RETRASAR_POS', 0.05],
                                ['MANTENER_POS', 0.7]
                            ]

                        ]
                    )
                elif j.posicion == _config.POSICIONES[2]: #Defensa
                    jugador_acciones.append(
                        [
                            j,
                            [
                                ['AVANZAR_POS', 0.05],
                                ['RETRASAR_POS', 0.65],
                                ['MANTENER_POS', 0.3]
                            ]

                        ]
                    )
            
            elif j.ubc == _config.IA.Zona.DEFENSA:
                if j.posicion == _config.POSICIONES[0]: #Delantero
                    jugador_acciones.append(
                        [
                            j,
                            [
                                ['AVANZAR_POS', 0.95],
                                ['MANTENER_POS', 0.05]
                            ]

                        ]
                    )
                elif j.posicion == _config.POSICIONES[1]: #Medio campo
                    jugador_acciones.append(
                        [
                            j,
                            [
                                ['AVANZAR_POS', 0.65],
                                ['MANTENER_POS', 0.35]
                            ]

                        ]
                    )
                elif j.posicion == _config.POSICIONES[2]: #Defensa
                    jugador_acciones.append(
                        [
                            j,
                            [
                                ['AVANZAR_POS', 0.35],
                                ['MANTENER_POS', 0.65]
                            ]

                        ]
                    )
    return jugador_acciones
      
def comportamiento_defensa_detenido_BLF(partido, equipo):
    jugador_acciones = []
    for j in equipo.jugadores_en_campo:
        if j.ubc == _config.IA.Zona.ATAQUE:
            if j.posicion == _config.POSICIONES[0]: # DEL
                jugador_acciones.append(
                    [
                        j,
                        [
                            ['RETRASAR_POS', 0.65],
                            ['RETRAZAR_POS_DEF', 0.3],
                            ['MANTENER_POS', 0.05]
                        ]
                    ]
                )
            elif j.posicion == _config.POSICIONES[1]: # MED
                jugador_acciones.append(
                    [
                        j,
                        [
                            ['RETRASAR_POS', 0.3],
                            ['RETRAZAR_POS_DEF', 0.65],
                            ['MANTENER_POS', 0.05]
                        ]
                    ]
                )
            elif j.posicion == _config.POSICIONES[2]: # DEF
                jugador_acciones.append(
                    [
                        j,
                        [
                            ['RETRASAR_POS', 0.1],
                            ['RETRAZAR_POS_DEF', 0.85],
                            ['MANTENER_POS', 0.05]
                        ]
                    ]
                )

        elif j.ubc == _config.IA.Zona.CENTRO:
            if j.posicion == _config.POSICIONES[0]: # DEL
                jugador_acciones.append(
                    [
                        j,
                        [
                            ['RETRASAR_POS', 0.3],
                            ['AVANZAR_POS', 0.05],
                            ['MANTENER_POS', 0.65]
                        ]
                    ]
                )
            elif j.posicion == _config.POSICIONES[1]: # MED
                jugador_acciones.append(
                    [
                        j,
                        [
                            ['RETRASAR_POS', 0.75],
                            ['AVANZAR_POS', 0.05],
                            ['MANTENER_POS', 0.2]
                        ]
                    ]
                )
            elif j.posicion == _config.POSICIONES[2]: # DEF
                jugador_acciones.append(
                    [
                        j,
                        [
                            ['RETRASAR_POS', 0.85],
                            ['AVANZAR_POS', 0.05],
                            ['MANTENER_POS', 0.1]
                        ]
                    ]
                )

        elif j.ubc == _config.IA.Zona.DEFENSA:
            if j.posicion == _config.POSICIONES[0]: # DEL
                jugador_acciones.append(
                    [
                        j,
                        [
                            ['AVANZAR_POS', 0.55],
                            ['MANTENER_POS', 0.45]
                        ]
                    ]
                )
            elif j.posicion == _config.POSICIONES[1]: # MED
                jugador_acciones.append(
                    [
                        j,
                        [
                            ['AVANZAR_POS', 0.35],
                            ['MANTENER_POS', 0.65]
                        ]
                    ]
                )
            elif j.posicion == _config.POSICIONES[2]: # DEF
                jugador_acciones.append(
                    [
                        j,
                        [
                            ['AVANZAR_POS', 0.05],
                            ['MANTENER_POS', 0.95]
                        ]
                    ]
                )
    return jugador_acciones

def comportamiento_defensa_detenido_CF_ZA(partido, equipo):
    jugador_acciones = []
    for j in equipo.jugadores_en_campo:
        if j.ubc == _config.IA.Zona.ATAQUE:
            if j.posicion == _config.POSICIONES[0]: #DEL
                jugador_acciones.append(
                    [
                        j,
                        [
                            ['RETRASAR_POS', 0.15],
                            ['MANTENER_POS', 0.85]
                        ]
                    ]
                )
            elif j.posicion == _config.POSICIONES[1]: #MED
                jugador_acciones.append(
                    [
                        j,
                        [
                            ['RETRASAR_POS', 0.45],
                            ['MANTENER_POS', 0.55]
                        ]
                    ]
                )    
            elif j.posicion == _config.POSICIONES[2]: #DEF
                jugador_acciones.append(
                    [
                        j,
                        [
                            ['RETRASAR_POS', 0.45],
                            ['REGRESAR_POS', 0.35],
                            ['MANTENER_POS', 0.2]
                        ]
                    ]
                ) 

        elif j.ubc == _config.IA.Zona.CENTRO:
            if j.posicion == _config.POSICIONES[0]: #DEL
                jugador_acciones.append(
                    [
                        j,
                        [
                            ['AVANZAR_POS', 0.65],
                            ['RETRASAR_POS', 0.05],
                            ['MANTENER_POS', 0.3]
                        ]
                    ]
                )
            elif j.posicion == _config.POSICIONES[1]: #MED
                jugador_acciones.append(
                    [
                        j,
                        [
                            ['AVANZAR_POS', 0.25],
                            ['RETRASAR_POS', 0.05],
                            ['MANTENER_POS', 0.7]
                        ]
                    ]
                )    
            elif j.posicion == _config.POSICIONES[2]: #DEF
                jugador_acciones.append(
                    [
                        j,
                        [
                            ['RETRASAR_POS', 0.55],
                            ['AVANZAR_POS', 0.1],
                            ['MANTENER_POS', 0.35]
                        ]
                    ]
                ) 

        elif j.ubc == _config.IA.Zona.DEFENSA:
            if j.posicion == _config.POSICIONES[0]: #DEL
                jugador_acciones.append(
                    [
                        j,
                        [
                            ['AVANZAR_POS', 0.45],
                            ['REGRESAR_POS', 0.55],
                            ['MANTENER_POS', 0.05]
                        ]
                    ]
                )
            elif j.posicion == _config.POSICIONES[1]: #MED
                jugador_acciones.append(
                    [
                        j,
                        [
                            ['AVANZAR_POS', 0.55],
                            ['AVANZAR_POS_DEL', 0.3],
                            ['MANTENER_POS', 0.15]
                        ]
                    ]
                )    
            elif j.posicion == _config.POSICIONES[2]: #DEF
                jugador_acciones.append(
                    [
                        j,
                        [
                            ['AVANZAR_POS_DEL', 0.05],
                            ['AVANZAR_POS', 0.3],
                            ['MANTENER_POS', 0.65]
                        ]
                    ]
                ) 
    return jugador_acciones

def comportamiento_defensa_detenido_CF_ZC(partido, equipo):
    jugador_acciones = []
    for j in equipo.jugadores_en_campo:
        if j.ubc == _config.IA.Zona.ATAQUE:
            if j.posicion == _config.POSICIONES[0]: #DEL
                jugador_acciones.append(
                    [
                        j,
                        [
                            ['RETRASAR_POS_DEF', 0.15],
                            ['RETRASAR_POS', 0.25],
                            ['MANTENER_POS', 0.6]
                        ]
                    ]
                )
            elif j.posicion == _config.POSICIONES[1]: #MED
                jugador_acciones.append(
                    [
                        j,
                        [
                            ['RETRASAR_POS', 0.65],
                            ['MANTENER_POS', 0.3],
                            ['RETRASAR_POS_DEF', 0.05]
                        ]
                    ]
                )    
            elif j.posicion == _config.POSICIONES[2]: #DEF
                jugador_acciones.append(
                    [
                        j,
                        [
                            ['RETRASAR_POS', 0.3],
                            ['REGRESAR_POS', 0.65],
                            ['MANTENER_POS', 0.05]
                        ]
                    ]
                ) 

        elif j.ubc == _config.IA.Zona.CENTRO:
            if j.posicion == _config.POSICIONES[0]: #DEL
                jugador_acciones.append(
                    [
                        j,
                        [
                            ['AVANZAR_POS', 0.25],
                            ['RETRASAR_POS', 0.05],
                            ['MANTENER_POS', 0.7]
                        ]
                    ]
                )
            elif j.posicion == _config.POSICIONES[1]: #MED
                jugador_acciones.append(
                    [
                        j,
                        [
                            ['AVANZAR_POS', 0.15],
                            ['RETRASAR_POS', 0.25],
                            ['MANTENER_POS', 0.6]
                        ]
                    ]
                )    
            elif j.posicion == _config.POSICIONES[2]: #DEF
                jugador_acciones.append(
                    [
                        j,
                        [
                            ['RETRASAR_POS', 0.65],
                            ['AVANZAR_POS', 0.05],
                            ['MANTENER_POS', 0.3]
                        ]
                    ]
                ) 

        elif j.ubc == _config.IA.Zona.DEFENSA:
            if j.posicion == _config.POSICIONES[0]: #DEL
                jugador_acciones.append(
                    [
                        j,
                        [
                            ['AVANZAR_POS', 0.45],
                            ['REGRESAR_POS', 0.2],
                            ['MANTENER_POS', 0.35]
                        ]
                    ]
                )
            elif j.posicion == _config.POSICIONES[1]: #MED
                jugador_acciones.append(
                    [
                        j,
                        [
                            ['AVANZAR_POS', 0.55],
                            ['AVANZAR_POS_DEL', 0.05],
                            ['MANTENER_POS', 0.4]
                        ]
                    ]
                )    
            elif j.posicion == _config.POSICIONES[2]: #DEF
                jugador_acciones.append(
                    [
                        j,
                        [
                            ['AVANZAR_POS_DEL', 0.05],
                            ['AVANZAR_POS', 0.3],
                            ['MANTENER_POS', 0.65]
                        ]
                    ]
                ) 
    return jugador_acciones 

def comportamiento_defensa_detenido_CF_ZD(partido, equipo):
    jugador_acciones = []
    for j in equipo.jugadores_en_campo:
        if j.ubc == _config.IA.Zona.ATAQUE:
            if j.posicion == _config.POSICIONES[0]: #DEL
                jugador_acciones.append(
                    [
                        j,
                        [
                            ['RETRASAR_POS_DEF', 0.25],
                            ['RETRASAR_POS', 0.6],
                            ['MANTENER_POS', 0.05]
                        ]
                    ]
                )
            elif j.posicion == _config.POSICIONES[1]: #MED
                jugador_acciones.append(
                    [
                        j,
                        [
                            ['RETRASAR_POS', 0.5],
                            ['MANTENER_POS', 0.05],
                            ['RETRASAR_POS_DEF', 0.45]
                        ]
                    ]
                )    
            elif j.posicion == _config.POSICIONES[2]: #DEF
                jugador_acciones.append(
                    [
                        j,
                        [
                            ['RETRASAR_POS', 0.2],
                            ['REGRESAR_POS', 0.75],
                            ['MANTENER_POS', 0.05]
                        ]
                    ]
                ) 

        elif j.ubc == _config.IA.Zona.CENTRO:
            if j.posicion == _config.POSICIONES[0]: #DEL
                jugador_acciones.append(
                    [
                        j,
                        [
                            ['AVANZAR_POS', 0.1],
                            ['RETRASAR_POS', 0.2],
                            ['MANTENER_POS', 0.7]
                        ]
                    ]
                )
            elif j.posicion == _config.POSICIONES[1]: #MED
                jugador_acciones.append(
                    [
                        j,
                        [
                            ['AVANZAR_POS', 0.1],
                            ['RETRASAR_POS', 0.3],
                            ['MANTENER_POS', 0.6]
                        ]
                    ]
                )    
            elif j.posicion == _config.POSICIONES[2]: #DEF
                jugador_acciones.append(
                    [
                        j,
                        [
                            ['RETRASAR_POS', 0.65],
                            ['AVANZAR_POS', 0.05],
                            ['MANTENER_POS', 0.3]
                        ]
                    ]
                ) 

        elif j.ubc == _config.IA.Zona.DEFENSA:
            if j.posicion == _config.POSICIONES[0]: #DEL
                jugador_acciones.append(
                    [
                        j,
                        [
                            ['AVANZAR_POS', 0.35],
                            ['REGRESAR_POS', 0.1],
                            ['MANTENER_POS', 0.55]
                        ]
                    ]
                )
            elif j.posicion == _config.POSICIONES[1]: #MED
                jugador_acciones.append(
                    [
                        j,
                        [
                            ['AVANZAR_POS', 0.55],
                            ['AVANZAR_POS_DEL', 0.05],
                            ['MANTENER_POS', 0.4]
                        ]
                    ]
                )    
            elif j.posicion == _config.POSICIONES[2]: #DEF
                jugador_acciones.append(
                    [
                        j,
                        [
                            ['AVANZAR_POS_DEL', 0.05],
                            ['AVANZAR_POS', 0.2],
                            ['MANTENER_POS', 0.75]
                        ]
                    ]
                ) 
    return jugador_acciones 


####            ATAQUE         ####

# Balon sale por la banda
def comportamiento_ataque_detenido_BB(partido, equipo):
    jugador_acciones = []
    zona_actual = partido.ultima_accion.agente.ubc
    jugadores_pos_actual = map(lambda x: x.ubc == zona_actual, equipo.jugadores_en_campo)
    ###
    # CREO Q HAY Q VERIFICAR QUE EL LENGTH DE jugadores_pos_actual SEA > 0
    ###
    jugador_saque_bb = jugadores_pos_actual[random.randint[0, len(jugadores_pos_actual) - 1]]
    for j in equipo.jugadores_en_campo:
        if j == jugador_saque_bb:
            continue

def comportamiento_ataque_detenido_CF_ZA(partido, equipo):
    pass

def comportamiento_ataque_detenido_CF_ZC(partido, equipo):
    pass

def comportamiento_ataque_detenido_CF_ZD(partido, equipo):
    pass

#El portero saca de portería y los otros jugadores se ubican en sus respectivas posiciones
def comportamiento_ataque_detenido_BLF_1(partido, equipo): 
    jugador_acciones = []
    for j in equipo.jugadores_en_campo:
        if j is Portero:
            jugador_acciones.append(
                [
                    j,
                    [
                        ['SAQUE_PORTERIA', 1]
                    ]
                ]
            )
        else:
            jugador_acciones.append(
                [
                    j,
                    [
                        ['REGRESAR_POS', 1]
                    ]
                ]
            )
    return jugador_acciones
            

def comportamiento_ataque_detenido_BLF_2(partido, equipo):
    pass



##############################################################################################


