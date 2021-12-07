# Football-Simulation-IA-SIM-COM-
Proyecto de IA-SIM-COM

# Definición del proyecto

Con este proyecto se intenta hacer una simulación de un partido de fútbol lo más real posible con el objetivo de obtener estadísticas de los resultados del partido en una especie de reporte. Los aspectos que tendrá este reporte son: 

- *Duelos ganados
- *Remates
- *Remates a portería
- *Tiros de esquina
- Fuera de juego
- *Pases
- *Balones perdidos
- *Balones recuperados
- *Paradas de portero
- *Faltas cometidas
- *Tarjetas amarillas
- *Tarjetas rojas

**Nota**: Los marcados con (*) son los aspectos de los que podemos obtener los resultados con la implementacion existente hasta el día de este reporte

## Definición de partido

Partido será el ambiente con el que los agentes como son: jugadores, arbitros, manager, etc interactuarán. Esta interación entre agente y partido será de la siguiente manera: dado un estado del partido el agente en cuestión decidirá que acción realizará. 
Se entiende por estado de un partido por:

- Equipos que se enfrentan
- Árbitros
- Marcador
- Estado, que será una de las siguientes opciones:  
    - INICIAR PARTIDO
    - REANUDAR PARTIDO
    - EN JUEGO  
    - JUEGO DETENIDO
- Jugador que posee el balón
- Última acción que se ha realizado hasta dicho momento

# Estructura de la simulación

### Definicion de los agentes

Para definir los agentes se tiene una clase abstracta **Agente** de la cual todos los agentes va a heredar, pues todos deben tener:

- Un método `acciones_dict` donde van a estar definidas todas las acciones que va a tener el agente.

- Un método `escoger_accion` que es el encargado de, dado un estado el partido escoger que acción va ha realizar el agente. Hasta este momento esto se tiene implementado para elegir las acciones que cumplan la precondición de manera aleatoria que va a realizar teniendo en cuenta la probabilidad de que realice cada acción, aunque hay casos donde solo puede ejecutar una acción determinada por las politicas propias de un partido de fútbol. Pero, para la versión final del proyecto en este método sería uno de los lugares donde aplicaríamos los conocimientos de Inteligencia Artificial. 

Importante destacar que todos los agentes tendrán un diccionario de acciones donde estaran guardadas una instancia y la probabilidad de que realice por cada acción que pueda realizar. 

### Definición de las Acciones

Para definir las acciones se tiene implementado una clase abstracta **Accion**. Se tomó como plantilla la forma de definir las acciones que se vio en las clases de IA por tanto los métodos que tiene esta clase son:

- Descripción
- Precondición
- Ejecutar
- Poscondición

#### Acciones por cada agente

##### JUGADOR

- Pase
- Tira Porteria
- Interceptar balón
- Hacer Falta
- Recibir balón
- Saque banda
- Saque esquina
- Saque falta

##### PORTERO

Ademas de las mismas que tiene JUGADOR tiene otras dos.

- Atajar
- Saque porteria

##### ARBITRO

- Sacar tarjeta
- Cantar falta

Luego teniendo en cuenta esta estructura se propuso una serie de tareas a implementar.

# Reporte del dia 6 - dic - 2021

Definimos una estructura mas elaborada para la parte de la simulación del proyecto. Para ver los detalles de esta nueva estructura dirigirse al encabezado `Estructura de la simulación` que se encuenttra al principio del documento. 

## Tareas hechas hasta el momento

1. ✅ Al iniciar/reanudar el partido lo primero que se debe hacer es dar un pase.

2. ✅ Bajar la probabilidad de disparo/gol y AUMENTAR LA DE PASES

3. ✅ Implementar las ENTRADAS(es cuando un jugador intenta robarle la pelota a otro jugardor), estas pueden ser: 

    3.1. ✅ Leves: se canta falta y nada más,  también el árbitro puede dejar seguir jugando sin cantar falta

    3.2 ✅ Moderadas: se canta falta y el árbitro puede mostrar la tarjeta amarilla

    3.3 ✅ Graves: se canta falta y el árbitro puede mostrar tarjeta amarilla o roja
    
    3.4 ✅ Exitosa: es cuando un jugador le roba el balon a otro, sin hacerle falta
    
4. ✅ Implementar las paradas de los porteros, esta pueden ser:

    4.1 ✅ Atajada: es cuando se produce un disparo y el portero se queda con el balón sin dar rebotes. Luego el portero tiene la posesión del balón y realiza un pase
  
    4.2 ✅ Atajada con rebote: se produce un disparo y el portero da rebote. Aqui hay que elegir quien coge ese rebote, puede ser el mismo portero, o CUALQUIER JUGADOR, PROBABILIDAD DE GOL ALTAAAAAA
    
    4.3 ✅ Atajada y el balón sale por la banda: luego de esto se produce un saque de banda

    4.4 ✅ Atajada y el balón sale por linea final: luego de esto se produce un saque de esquina
 
## Tareas propuestas

1. ✅ Implementar los saques de esquina. Aqui casi siempre hay un jugador que realiza los saques de esquina del equipo. En el saque de esquina se pueden pasar varias cosas:

    1.1 Rechace o Despeje: es cuando un jugador del equipo contrario del jugador q saca el saque de esquina despeja el balon(PUEDE SER EL PORTERO). Este rechace tiene BAJA PROBABILIDAD que el balón lo mantenga el equipo que rechazó el balón
    
    1.2 Marcar Gol: Se marca gol
    
    1.3 El portero se queda con el balon y autoseguido viene un pase

2. Implementar los rechaces/despejes, es cuando un jugar despeja el balón, esto puede terminar en: 

    2.1 Saque de banda

    2.2 Saque de esquina

    2.3 Lo equivalente a un pase

    2.4 Cambio de la posesión del balón

3. Modificar el equipo con el objetivo de separar el once inicial y los que se quedan en la banca para el partido.

4. Implementar el Manager con sus acciones. 

