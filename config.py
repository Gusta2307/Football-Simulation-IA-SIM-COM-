
class Config:
    def __init__(self) -> None:
        #POSICIONES
        self.POSICIONES = ['DEL', 'MC', 'DEF', 'GK']
        
        #ESTADOS DEL PARTIDO
        self.INICIAR_PARTIDO = 'INICIAR PARTIDO'
        self.REANUDAR_PARTIDO = 'REANUDAR PARTIDO'
        self.EN_JUEGO = 'EN JUEGO'
        self.DETENIDO = 'JUEGO DETENIDO'

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
