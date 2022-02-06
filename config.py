
class Config:
    class ZONA:
        ATAQUE = 'ATAQUE'
        CENTRO = 'CENTRO'
        DEFENSA = 'DEFENSA'

        REL_ZONA_POS = {
            'DEL': ATAQUE,
            'MC': CENTRO,
            'DEF': DEFENSA,
            'GK': DEFENSA
        }

        SIGUIENTE_ZONA = {
            DEFENSA: CENTRO,
            CENTRO: ATAQUE
        }

        ANTERIOR_ZONA = {
            ATAQUE: CENTRO,
            CENTRO: DEFENSA
        }


    class POSICIONES:
        POS = ['DEL', 'MC', 'DEF', 'GK']

    class PARTIDO:
        class ESTADO:
            INICIAR_PARTIDO = 'INICIAR PARTIDO'
            REANUDAR_PARTIDO = 'REANUDAR PARTIDO'
            EN_JUEGO = 'EN JUEGO'
            DETENIDO = 'JUEGO DETENIDO'

        class CONFIG:
            CANT_JUGADORES_BANCA = 7
            VENTANAS_DE_CAMBIOS = 3
            TOTAL_DE_CAMBIOS = 1
    class ACCIONES:
        class JUGADOR:
            #TIPOS DE ACCIONES
            ACT_PASE = 'ACT PASE'
            ACT_TIRO_PORTERIA = 'ACT TIRO PORTERIA'
            ACT_HACER_FALTA = 'ACT HACER FALTA'
            ACT_INTERCEPTAR_BALON = 'ACT INTERCEPTAR BALON'
            ACT_ATAJAR = 'ATAJAR'
            ACT_RECIBIR_BALON = 'ACT RECIBIR BALON'
            ACT_SAQUE_BANDA = 'ACT SAQUE BANDA'
            ACT_SAQUE_PORTERIA = 'ACT SAQUE PORTERIA'
            ACT_SAQUE_ESQUINA = 'ACT SAQUE ESQUINA'
            ACT_DEFAULT ='ACT DEFAULT'
            ACT_SAQUE_FALTA = 'ACT SAQUE FALTA'
            ACT_DESPEJAR_BALON = 'ACT DESPEJAR BALON'
            ACT_AVANZAR_POSICION = 'ACT AVANZAR POSICION'
            ACT_RETROCEDER_POSICION = 'ACT RETROCEDER POSICION'
        
        class MANAGER:
            ACT_ESCOGER_ALINEACION = 'ACT ESCOGER ALINEACION'
            ACT_HACER_CAMBIOS = 'ACT HACER CAMBIOS'
            # [DEL, MC, DEF, GK]
            ESQUEMA_DE_JUEGO = [[3, 3, 4, 1]]

        class ARBITRO:
            ACT_CANTAR_FALTA = 'ACT CANTAR FALTA'
            ACT_SACAR_TARJETA = 'ACT SACA TARJETA'


        #ESTADOS DE LAS ACCIONES
        class ESTADO:
            class TIRO_PORTERIA:
                A_PORTERIA = 'A PORTERIA'
                POR_FUERA = 'POR FUERA'

            class RECIBIR_BALON:
                RECIBIR_BALON = 'RECIBE EL BALON'
                NO_RECIBE_BALON = 'NO RECIBE EL BALON'
                BANDA = 'SE FUE POR LA BANDA'
                LINEA_FINAL = 'SE FUE POR LA LINEA FINAL'

            class FALTA:
                SEL_NIVEL = {
                    1: 'LEVE',
                    2: 'MODERADA',
                    3: 'GRAVE'
                }

            class INTERCEPCION:
                SIN_FALTA = 'SIN FALTA'
                CON_FALTA = 'CON FALTA'

            class ATAJAR:
                ATAJO = 'ATAJO'
                NO_ATAJO = 'NO ATAJO'
                SIN_REBOTE = 'ATAJO SIN REBOTE'
                REBOTE_BANDA = 'ATAJO CON REBOTE Y EL BALON SALE POR BANDA'
                REBOTE_LINEA_FINAL = 'ATAJO CON REBOTE Y EL BALON SALE POR LINEA FINAL'
                REBOTE_JUGADOR = 'ATAJO CON REBOTE Y EL BALON QUEDA SUELTO'

            class ARBITRO:
                NO_CANTA_FALTA = 'NO CANTA FALTA'
                CANTA_FALTA = 'CANTA FALTA'

            class SACAR_TARJETA:
                MUESTRA_AMARILLA = 'MUESTA TARJETA AMARILLA'
                MUESTRA_ROJA = 'MUESTA TARJETA ROJA'

            class DESPEJAR_BALON:
                DESPEJE_LINEA_FINAL = 'DESPEJO EL BALON Y SALE POR LINEA FINAL'
                DESPEJE_BANDA = 'DESPEJO EL BALON Y SALE POR BANDA'
                DESPEJE_JUGADOR = 'DESPEJE EL BALON Y EL BALON QUEDA SUELTO JUGADOR'
    
    class TRADUCTOR_ACT:
        ACT = {
            'BALL_PASS': "PASE",
            'SHOT_ON_GOAL': "TIRO",
            'INTERCEPT_BALL': "INTERCEPCION",
            "RECEIVE_BALL" : "RECIBIR_BALON",
            "THROW_IN" : "SAQUE_BANDA",
            "CORNER_KICK" : 'SAQUE_ESQUINA',
            "CLEAR_BALL": 'DESPEJAR_BALON',
            "COMMIT_FOUL": 'HACER_FALTA',
            "ADVANCE_POSITION": "AVANZAR_POSICION",
            "BACK_POSITION": 'RETROCEDER_POSICION',
        }
    class TRADUCTOR_ID:
        ID = {
            "name": 'nombre',
            "experence": "experiencia",
            "country": "pais", 
            "age": "edad",
            'team': "equipo",
            'st': "estrategia",
            'location' : 'ubicacion_campo',
            'actions' : "acciones",
            'coach' : 'manager',
            "players" : 'jugadores',
            'playersCamp': "_jugadores_en_campo",
            'playersBench' : "_jugadores_en_banca",
            'pos' : "posicion",
            'cards_count' : "cantidad_tarjetas",
            'team1' : 'eq1',
            'team2' : "eq2",
            "referees" : "arbitros",
            "goalscore": "marcador",
            "pt"
            "reporte"
            'time': "__tiempo",
            "state": "estado",
            "lastaction" : "ultima_accion",
            "pos_ball" : "pos_balon",
            "pos_ball_1_time" : "pos_balon_1er_tiempo",
            "name_eq2" : "_eq2",
            "name_eq1" : "_eq1",
            'goal': "_goles",
            'shots': "_remates",
            'corner kick' : "_tiros_de_esquina",
            'outside': '_fuera_de_juego',
            "ball_pass": "pases",
            "lost_ball": "balones_perdidos",
            'recovered_balls': "balones_recuperados",
            'saves': "paradas_portero",
            "foul": "faltas",
            "cards_yellow" : "tarjetas_amarillas",
            "cards_red":"tarjetas_rojas",
            "abstrac":"_resumen",
            "get_value": "get_value"
        }
