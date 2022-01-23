
class Config:
    class IA:
        class Estrategia:
            ATAQUE =  'ATAQUE'
            DEFENSA = 'DEFENSA'

        class Zona:
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

    def __init__(self) -> None:
        #POSICIONES
        self.POSICIONES = ['DEL', 'MC', 'DEF', 'GK']
        
        #ESTADOS DEL PARTIDO
        self.INICIAR_PARTIDO = 'INICIAR PARTIDO'
        self.REANUDAR_PARTIDO = 'REANUDAR PARTIDO'
        self.EN_JUEGO = 'EN JUEGO'
        self.DETENIDO = 'JUEGO DETENIDO'

        self.CANT_JUGADORES_BANCA = 7
        self.VENTANAS_DE_CAMBIOS = 3
        self.TOTAL_DE_CAMBIOS = 1


        #TIPOS DE ACCIONES
        self.ACT_PASE = 'ACT PASE'
        self.ACT_TIRO_PORTERIA = 'ACT TIRO PORTERIA'
        self.ACT_HACER_FALTA = 'ACT HACER FALTA'
        self.ACT_INTERCEPTAR_BALON = 'ACT INTERCEPTAR BALON'
        self.ACT_ATAJAR = 'ATAJAR'
        self.ACT_RECIBIR_BALON = 'ACT RECIBIR BALON'
        self.ACT_SAQUE_BANDA = 'ACT SAQUE BANDA'
        self.ACT_SAQUE_PORTERIA = 'ACT SAQUE PORTERIA'
        self.ACT_SAQUE_ESQUINA = 'ACT SAQUE ESQUINA'
        self.ACT_DEFAULT ='ACT DEFAULT'
        self.ACT_CANTAR_FALTA = 'ACT CANTAR FALTA'
        self.ACT_SACAR_TARJETA = 'ACT SACA TARJETA'
        self.ACT_SAQUE_FALTA = 'ACT SAQUE FALTA'
        self.ACT_DESPEJAR_BALON = 'ACT DESPEJAR BALON'
        self.ACT_ESCOGER_ALINEACION = 'ACT ESCOGER ALINEACION'
        self.ACT_HACER_CAMBIOS = 'ACT HACER CAMBIOS'
        self.ACT_AVANZAR_POSICION = 'ACT AVANZAR POSICION'
        self.ACT_RETROCEDER_POSICION = 'ACT RETROCEDER POSICION'

        #ESTADOS DE LAS ACCIONES
        #TIRO A PORTERIA
        self.A_PORTERIA = 'A PORTERIA'
        self.POR_FUERA = 'POR FUERA'

        #PASE
        

        #RECIBIR BALON
        self.RECIBIR_BALON = 'RECIBE EL BALON'
        self.NO_RECIBE_BALON = 'NO RECIBE EL BALON'
        self.BANDA = 'SE FUE POR LA BANDA'
        self.LINEA_FINAL = 'SE FUE POR LA LINEA FINAL'

        #FALTA
        self.SEL_NIVEL = {
            1: 'LEVE',
            2: 'MODERADA',
            3: 'GRAVE'
        }

        #INTERCEPCION
        self.SIN_FALTA = 'SIN FALTA'
        self.CON_FALTA = 'CON FALTA'

        #ATAJAR
        self.ATAJO = 'ATAJO'
        self.NO_ATAJO = 'NO ATAJO'
        self.SIN_REBOTE = 'ATAJO SIN REBOTE'
        self.REBOTE_BANDA = 'ATAJO CON REBOTE Y EL BALON SALE POR BANDA'
        self.REBOTE_LINEA_FINAL = 'ATAJO CON REBOTE Y EL BALON SALE POR LINEA FINAL'
        self.REBOTE_JUGADOR = 'ATAJO CON REBOTE Y EL BALON QUEDA SUELTO'

        #ARBITRO
        self.NO_CANTA_FALTA = 'NO CANTA FALTA'
        self.CANTA_FALTA = 'CANTA FALTA'

        #SACAR TARJETA
        self.MUESTRA_AMARILLA = 'MUESTA TARJETA AMARILLA'
        self.MUESTRA_ROJA = 'MUESTA TARJETA ROJA'

        #DESPEJAR BALON
        self.DESPEJE_LINEA_FINAL = 'DESPEJO EL BALON Y SALE POR LINEA FINAL'
        self.DESPEJE_BANDA = 'DESPEJO EL BALON Y SALE POR BANDA'
        self.DESPEJE_JUGADOR = 'DESPEJE EL BALON Y EL BALON QUEDA SUELTO JUGADOR'


        #MANAGER
        # [DEL, MC, DEF, GK]
        self.ESQUEMA_DE_JUEGO = [[3, 3, 4, 1]]


        #