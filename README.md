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

Además de las mismas que tiene JUGADOR tiene otras dos.

- Atajar
- Saque portería

##### ARBITRO

- Sacar tarjeta
- Cantar falta

#### Manager 

- Alineación
- Cambiar jugador

### Definición del reporte 
#### Propiedades
- Equipos
- Marcador
- Remates
- Tiros de esquina
- Fuera de juego
- Pases
- Balones perdidos
- Balones recuperados
- Paradas del portero
- Faltas
- Tarjetas amarillas
- tarjetas rojas

Estas propiedades se van a ir actualizando en el transcurso del partido, para ello la clase reporte tiene un método por cada propiedad que se encarga de actualizarlas. 

# Estructura de Compilación
## Keywords
- player
- team
- game
- manager
- referee
- filter
- for
- if
- elif
- else
- return
- by
- function
- in
- OR
- AND
- NOT

## Symbols
- Assignment: =
- Underscore: _
- Brackets: (, ), {, }, [, ]
- Operators: >, <, >=, <=, ==, !=

## Separators 
- ;
- ,
- :


## Definición de tipos 

### PLAYER
```
player = {
    #required
    'name':"", # str
    'position':"", # DEL, MC, DEF or GK
    'media':"", # int
    #optional
    'age':"", # int
    'potencial':"", # int
    'country':"", # str
    'team':"", # str
    'DEF':"", # int 
    'MC':"", # int
    'DEF':"", # int
    'status':"" # available, injured or sanctioned
}
```
### TEAM
```
team = {
    #required
    'name':"", # str
    'player':"", # list of player
    'manager':"", # manager
    'country':"", # str
    #optional
    'stadium':"", # str
}
```
### GAME

```
game = {
    #required
    'team1':"", # Team
    'team2':"", # Team
    'stadium':"", # str
    'referee':"", # list of referee
    #optional
    'weather':"", # str
    'date':"", # date
}
```
### MANAGER
```
manager = {
    #required
    'name':"", # str
    'team':"", # str
    'experience':"", # int
    #optional
    'country':"", # str
    'age':"", # int
}
```
### REFEREE

```
referee = {
    #required
    'name':"", # str
    'experience':"", # int
    #optional
    'country':"", # str
    'age':"", # int
}
```
## Ejemplo de sintaxis
### Inicialización

```
#Inicializacion de un player
    player p1 ( args );

    #Inicializacion de un team
    team t1 ( args );

    #Inicializacion de un game
    game g1 ( args );
```
### Declaración de listas 
```
    player p [ p1, p2, p3, .... ]
```
### Indexación de listas 
```
    p[0] # se accede al elemento 0 de la lista p
    #p[-1] devuelve el ultimo elemento del array, si hacemos p[-2]  devuelve el penultimo
    #p[23] en este caso hace 23%(p.length) y cae siempre en una posicion dentro del array
```
### Asignacion 
```
    p1 = p2 # se le asigna a p1 el valor de p2
```
### Acceso a propiedades 
```
player.name # se accede a la propiedad name de player
```
### For
```
    for item in t.player{
        ...
    }
```
### Filtrar por una propiedad
```
    filter t.players by (_.age > 20) # devuelve todo los jugadores mayores de 20 años de un equipo
```
### Condicionales
```
    if <condicion> { }
    if <condicion> { } elif { }
    if <condicion> { } elif { } else { }
```
### Operadores lógicos
```
    OR AND NOT
```
### Definición de funciones
```
    function type id (args) { }
    #En caso de ser void se representa el type con _
```

# Reporte hasta el dia 6 - dic - 2021

Definimos una estructura mas elaborada para la parte de la simulación del proyecto. Para ver los detalles de esta nueva estructura dirigirse al encabezado `Estructura de la simulación` que se encuenttra al principio del documento. 

## Tareas hechas hasta el momento

- [x] 1. Al iniciar/reanudar el partido lo primero que se debe hacer es dar un pase.

- [x] 2. Bajar la probabilidad de disparo/gol y AUMENTAR LA DE PASES

- [x] 3. Implementar las ENTRADAS(es cuando un jugador intenta robarle la pelota a otro jugardor), estas pueden ser: 

    - [x] 3.1 Leves: se canta falta y nada más,  también el árbitro puede dejar seguir jugando sin cantar falta

    - [x] 3.2 Moderadas: se canta falta y el árbitro puede mostrar la tarjeta amarilla

    - [x] 3.3 Graves: se canta falta y el árbitro puede mostrar tarjeta amarilla o roja
    
    - [x] 3.4 Exitosa: es cuando un jugador le roba el balon a otro, sin hacerle falta
    
- [x] 4. Implementar las paradas de los porteros, esta pueden ser:

    - [x] 4.1 Atajada: es cuando se produce un disparo y el portero se queda con el balón sin dar rebotes. Luego el portero tiene la posesión del balón y realiza un pase
  
    - [x] 4.2 Atajada con rebote: se produce un disparo y el portero da rebote. Aqui hay que elegir quien coge ese rebote, puede ser el mismo portero, o CUALQUIER JUGADOR, PROBABILIDAD DE GOL ALTAAAAAA
    
    - [x] 4.3 Atajada y el balón sale por la banda: luego de esto se produce un saque de banda

    - [x] 4.4 Atajada y el balón sale por linea final: luego de esto se produce un saque de esquina
 
## Tareas propuestas

- [x] 1. Implementar los saques de esquina. Aqui casi siempre hay un jugador que realiza los saques de esquina del equipo. En el saque de esquina se pueden pasar varias cosas:

    - [x] 1.1  Rechace o Despeje: es cuando un jugador del equipo contrario del jugador q saca el saque de esquina despeja el balon(PUEDE SER EL PORTERO). Este rechace tiene BAJA PROBABILIDAD que el balón lo mantenga el equipo que rechazó el balón
    
    - [x] 1.2 Marcar Gol: Se marca gol
    
    - [x] 1.3 El portero se queda con el balón y autoseguido viene un pase

- [x] 2. Implementar los rechaces/despejes, es cuando un jugar despeja el balón, esto puede terminar en: 

    - [x] 2.1 Saque de banda

    - [x] 2.2 Saque de esquina

    - [x] 2.3 Lo equivalente a un pase

    - [x] 2.4 Cambio de la posesión del balón

- [x] 3. Modificar el equipo con el objetivo de separar el once inicial y los que se quedan en la banca para el partido.

- [x] 4. Implementar el Manager con sus acciones. 

- [x] 5. Agregar tiempo y medio tiempo

- [x] 6. Implementar reporte (estadísticas del partido)

# REPORTE DEL DIA 29 - DIC - 2021

Completamos todas las tareas que se quedaron propuestas de la semana pasada; por lo que ya tenemos implementado el agente Manager y el reporte, que es donde se van a guardar las estadísticas del juego. Para ambas clases se puede ver al principio del documento como están estructuradas. 

Con estas tareas terminadas se podría decir que ya esta bastante completa la parte de simulación del proyecto, solo quedaría agregar los conocimientos de IA, que se hara más adelante. 

Teniendo en cuenta lo anterior, empezamos a trabajar en la parte de compilacion del proyecto. 
___

Lo primero que se hizo fue definir las reglas sintácticas y semánticas, además de la clasifición de tokens, este último se puede ver en la sesión de la estrutura de compilación.

## Validación reglas sintácticas

```
<program> := <stat-list>
<stat-list> := <stat> ";"
	     | <stat> ";" <stat-list>
     <stat> := <player-var>
     	     | <team-var>
     	     | <game-var>
     	     | <manager-var>
     	     | <referee-var>
   	     | <assign-var>
   	     | <const-var>
     	     | <for-cycle>
     	     | <if-cond>
     	     | <function-func>
     	     | <def-array>
     	     | <array-index>
<player-var>:= "player" ID "("<arg-list>")"
  <team-var>:= "team" ID "("<arg-list>")"
  <game-var>:= "game" ID "("<arg-list>")"
<manager-var>:= "manager" ID "("<arg-list>")"
<referee-var>:= "referee" ID "("<arg-list>")"
<assign-var> := ID "<-" ID
	      | <type> ID "<-" ID
 <const-var>:= "const" <type> ID
 <for-cycle>:= "for" ID "in" ID ":" "{"<stat>"}"
             | "for" ID "in" ID"."ID" ":" "{"<stat>"}"
   <if-cond>:= "if" <expr> ":" "{"<stat>"}"
             | "if" <expr> ":" "{"<stat>"}" "else" "{"<stat>"}"
<function-func> := "function" <type> ID "("<arg-list>")" "{"<stat>"}"
  <def-array>:= <type> ID "["<ID-list>"]"
<array-index>:= ID "["NUMBER"]"
  <arg-list>:= ID
             | ID "=" <atom>
             | ID "=" <atom> "," <arg-list>
   <ID-list>:= ID
             | ID "," <ID-list>
      <type>:= player
             | team
             | game
             | manager
             | referee
      <expr>:= <expr> "OR" <expr>
             | <expr> "AND" <expr>
             | "NOT" <expr>
             | <term>
      <term>:= <term> ">" <term>
             | <term> ">=" <term>
             | <term> "<" <term>
             | <term> "<=" <term>
             | <term> "==" <term>
             | <term> "!=" <term>
             | <atom>
      <atom>:= ID
             | NUMBER
             | <func-call>
 <func-call>:= ID "("<expr-list>")"
 <expr-list>:= <expr>
             | <expr> "," <expr-list>

```

## Reglas semanticas

- Una variable solo puede ser definida una vez en todo el programa.
- Los nombres de variables y funciones no comparten el mismo ámbito (pueden existir una variable y una función llamadas igual).
- No se pueden redefinir las funciones predefinidas (en nuestro caso un ejemplo es: filter).
- Una función puede tener distintas definiciones siempre que tengan distinta cantidad de argumentos.
- Toda variable y función tiene que haber sido definida antes de ser usada en una expresión (salvo las funciones pre-definidas).
- Todos los argumentos definidos en una misma función tienen que ser diferentes entre sí, aunque pueden ser iguales a variables definidas globalmente o a argumentos definidos en otras funciones.
- En el cuerpo de una función, los nombres de los argumentos ocultan los nombres de variables iguales.

___

Luego de esto, se empezo con la implementación. Dado la clasificación de los tokens antes mencionada, si realizó el análisis léxico, para ello se tiene `token.py`, `compiling.py` y `lexicalAnalizer.py`. 

En `compiling.py` se registran todos los tokens definidos y en `lexicalAnalizer.py` es donde se hace la tokenización, para la cual definimos una máquina de estado, en el método `tokenize`, para tu mejor implementación. `tokenize` devuelve una lista de elementos de tipo `token`. 

___


