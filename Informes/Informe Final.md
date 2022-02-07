# Proyecto de Compilación, IA y Simulación: Football Simulation

## Integrantes

- Sheila Artiles Fagundo
- Grettel Hernández Garbey
- Gustavo Despaigne Dita

---

## Definición del problema

Se tiene como objetivo principal del proyecto brindar una herramienta para la simulación de un partido de fútbol donde el usuario pueda definir los agentes que se relacionan en un partido: jugadores, managers y árbitros. Es importante destacar que los jugadores durante la simulación siempre tomarán la decisión de que hacer dado un estado del partido de acuerdo a las características que el usuario le definió.

La corrida de una simulación de un partido devuelve un reporte con las estadísticas del mismo por cada equipo.

## Pasos para poder programar en el lenguaje que se propone

Para tener una mejor experiencia al programar en el lenguaje que se propone se debe instalar la extensión FSIM para ello es necesario que se sigan los siguientes pasos:

1. Descargar y descomprimir el archivo `FSIM.zip` que se encuentra en el repositorio
2. Abrir una terminal donde se encuentra la carpeta anterior
3. Ejecutar en la terminal el comando `cp -r FSIM ~/.vscode/extensions`
4. Entrar normalmente al Visual Studio Code y crear un archivo con la extension `fsim` y listo!! ya puede programar en este lenguaje.

## Sintaxis del Lenguaje de Programación

### Keywords

* player
* team
* game
* manager
* referee
* for
* if
* elif
* else
* return
* function
* in
* OR
* AND
* NOT

### Symbols

* Assignment: =
* Brackets: (, ), {, }, [, ]
* Operators: >, <, >=, <=, ==, !=

### Separators

* ;
* ,
* :

### Definición de tipos

#### PLAYER

```
player = {
    #required
    'name':"", # str
    'pos':"", # DEL, MC, DEF or GK
    'age':"", # int
    'country':"", # str
    'list_prob': [], #list de 12 elementos con las prob de que jugador ejecute correctamente las acciones
     'st': None #Estrategia (opcional)
}
```

#### TEAM

```
team = {
    #required
    'name':"", # str
    'players':"", # list of player
    'manager':"", # manager
    'country':"" # str
}
```

#### GAME

```
game = {
    #required
    'eq1':"", # Team
    'eq2':"", # Team
    'referees':"", # list of referee
}
```

#### MANAGER

```
manager = {
    'name':"", # str
    'experience':"", # int
    'country':"", # str
    'age':"", # int
}
```

#### REFEREE

```
referee = {
    'name':"", # str
    'experience':"", # int
    'country':"", # str
    'age':"", # int
    'list_prob': #lista de 4
}
```

### Ejemplo de sintaxis

#### Inicialización

```
#Inicializacion de un player
    player p1 = ( args );

    #Inicializacion de un team
    team t1 = ( args );

    #Inicializacion de un game
    game g1 = ( args );
```

#### Declaración de listas

```
    player p [ p1, p2, p3, .... ]
```

#### Indexación de listas

#### Asignación

```
    p1 = p2 # se le asigna a p1 el valor de p2
```

#### Acceso a propiedades

```
    player.name # se accede a la propiedad name de player
```

#### For

```
    for item in t.player{
        ...
    }
```

#### Condicionales

```
    if <condicion> { };
    if <condicion> { } elif { };
    if <condicion> { } elif { } else { };
```

#### Operadores lógicos

```
    OR AND NOT
```

#### Definición de funciones

```
    function type id (args) { }
```

#### Definición de estrategias

```
estrategy name{
	variables{
	   name_action = value,
	   name_action1 = rangeint(0, 5, f),
	   name_action2 = rangebool(),
	};
	execute(state_game, player){
		if name_action1 > 10 and state_game.pos_balon == player:
			return 'BALL_PASS'
	};
}
```

---

# Detalles de la implementación

## Implementación de la simulación de un partido

### Definición de `Accion`

Para definir las acciones se tiene la clase abstracta `Accion`. Se tomó como plantilla representación de acciones en STRIPS que se vió en las clases de IA, por tanto los métodos que tiene esta clase son:

- Descripción
- Precondición
- Ejecutar
- Poscondición

### Definición de `Agente`

Para definir los agentes se tiene una clase abstracta Agente de la cual todos los agentes va a heredar, pues todos deben tener:

Un método `acciones_dict` donde van a estar definidas todas las acciones que va a tener el agente.

Un método `escoger_accion_estrategia` que es el que se encarga de, dado un estado el partido y los valores de las variables de la estrategia que tiene asignado el agente, hacer un llamado al execute de la misma, y devuelve la instancia de la acción correspondiente. En caso de que la acción que decida la estrategia no se pueda ejecutar, ya que no se cumple su precondición, o que el agente no se le asigne una estrategia en su creación, entonces se hace una llamada al método `escoger_acción_base` donde se aplica una especie de lógica difusa pues en dependecia de determinados estados del partido es la acción que se realiza, además de tener siempre en cuenta que las precondiciones de las acciones.

Importante destacar que todos los agentes tienen un diccionario de acciones donde se guardan una instancia de las mismas.

#### `Jugador`

Para inicializar un jugador se necesita su nombre, una lista que representan, por cada acción que puede realizar, la probabilidad de que la ejecute correctamente. Además tiene como parámetro opcional el poder asignarle una estrategia. Además cuando un jugador pasa a pertenecer a un equipo entonces se actualiza el atributo con dicho nombre.

Las acciones que puede realizar un jugador son:

- Pase del balón
- Tiro a portería
- Interceptar un balón
- Hacer falta
- Recibir balón
- Sacar de banda
- Sacar de esquina
- Sacar por falta
- Despejar balón
- Avanzar posición
- Retroceder posición

En `escoger_accion_base` se tiene en cuenta las reglas convencionales establecidas para un partido de fútbol, por tanto, si el estado del partido es `INICIAR_PARTIDO` o `REANUDAR_PARTIDO`, si se cumple la precondición de `PASE` entonces esta es la acción que se elige. Si este no es el caso, entonces, se filtra todas las acciones que puede ejecutar el jugador y si la ultima acción es un `Pase` y entre las acciones que puede realizar está `Recibir Balón` entonces es esta la acción que se escoge, en caso contrario se escoge aleatoriamente entre todas las acciones posibles o no hacer nada (`DEFAULT`).

En caso de que se escoja hacer un pase, para escoger al jugador al que se le hace el pase se tiene en cuenta su ubicación y la de los demás jugadores del su equipo, ya que se tiene más posibilidad de que se le haga un pase a un jugador que esté en su misma zona en el campo que de otra.

#### `Portero`

La clase `Portero` hereda de la clase `Jugador` pues es un tipo particular de esta, pues puede realizar las mismas acciones que un jugador a excepción de `SAQUE_BANDA` y `DESPEJAR_BALON` y además se le suman dos más: `ATAJAR` y `SAQUE_PORTERIA`, lo que trae consigo que se agreguen la probabilidad de que ejecute correctamente estas acciones.

En `escoger_accion_base` si la última acción es un tiro a portería y el estado del partido es `EN_JUEGO` entonces la acción que se elige es `ATAJAR`. Por otro lado, si se cumple la precondición de `Saque_Banda` entonces es la acción que se elige. Luego si la última acción es `ATAJAR` y esta se realizó sin rebote entonces, el portero realizará un pase. Si ninguno de los anteriores es el caso, entonces, elige la acción a realizar igual que lo hace un jugador cuando no se cumple ninguno de los casos particulares.

#### `Manager`

Para inicializar un `Manager` se necesita su nombre y experiencia, además por supuesto si se desea, una estrategia. El árbitro solo puede realizar dos acciones:   `Escoger_alineacion `y `Hacer_cambio`. La acción `Escoger_alineacion` solo se ejecuta al inicializar un partido.

#### `Árbitro`

Para inicializar un `Árbitro` se necesita sun nombre, pais, experiencia y edad, además por supuesto si se desea una estrategia. Luego cuando se cree un equipo y se le asigne como su propio manager entonces se actualiza el atributo  `equipo `. El árbitro solo puede realizar dos acciones:   `Sacar_tarjeta` y `Cantar_Falta`. La acción `Cantar_Falta` solo se ejecuta si la última acción fue hacer falta y se saca tarjeta según las reglas del fútbol.

### Definición de `Equipo`

Un equipo se conforma por un conjunto de jugadores y un manager, tiene un nombre y una lista con los jugadores en el campo y otra con los jugadores en la banca que se actualiza cuando el manager elige la alineación para un partido.

### Definición de `Partido`

Para la simulación de un partido se tiene una clase ``Partido`` que contiene como atributos:

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
- Tiempo
- Cambios pendientes
- Reporte

Además tiene como método principal para la simulación del partido `simula` y como secundarios: `__iniciar_partido` y `__reanudar_partido_pos_gol`.

El método ``simular`` consiste en que por cada iteración, hasta que se cumplan los 90 minutos de un partido, cada agente decide para el estado actual del partido que acción van a realizar con el método `escoger_accion_estrategia`, para luego ejecutarlas.

### Definición de `Reporte`

El atributo reporte es una instancia de la clase `Reporte` donde se guardan y se actualizan, a medida que esté corriendo la similación del partido, por cada uno de los equipos las siguientes estadísticas:

- goles
- remates
- tiros de esquina
- pases
- balones perdidos
- balones recuperados
- paradas portero
- faltas
- tarjetas amarillas
- tarjetas rojas

---

## Optimización de los agentes

### Definición de `Range`

`Range` es una clase abstracta de la cual hereda los diferentes tipos de variables que se pueden utilizar para la definición de una estrategia. `Range` tiene el método `get_value` que devuelve un valor de acuerdo al tipo de `Range`. Es válido aclarar que el tipo de los valores que va a devolver depende del tipo de `Range` que se puede reconocer fácilmente por el tipo de `Range`.

#### `RangeInt` y `RangeFloat`

Para inicializar una variable de tipo `RangeInt` se necesita el límite inferior y superior del intervalo en el que se encuentran los valores, además se le puede pasar una función que reciba un parámetro del mismo tipo de la variable que representa la distribución de como se va a comportar la variable.

#### `RangeBool`

Este tipo de `Range` no recibe un intervalo pues, como se puede intuir del nombre, solo existen dos posibles valores que puede tomar: `True` y `False`, luego solo recibe, si se desea, una función que represente una distribución.

#### `RangeChoice`

Este tipo da la libertad que los valores que puede tomar no tienen que ser de ningúnj tipo específico por lo tanto recibe una lista de valores y una función que representa una distribución si se desea.

### Definición de `Estrategia`

La clase `Estrategia` consta de un diccionario de variables y un execute. El diccionario de variables pueden contener variables con un valor específico o de cualquier tipo que herede de `Range`. El execute es la función que implementa el usuario para decidir que acción va a realizar el agente al que se le asigna al tener en cuenta los valores que se le asigna a las variables en el proceso de optimización.

### Definición de `Optimizador`

La clase `Optimizador` es la que se va a encargar de al inicializar un partido asignarle valores exactos a las variables de tipo `Range` que tenga la estrategia de cada uno de los agentes que se relacionan en el partido. Para ello se realiza una metaheurística genérica, donde por cada partido se se crea varias versiones del mismo al variar los valores de la estrategia de cada agente del equipo y con ellos se realiza un torneo, luego por cada jugador se escogen las variables que hicieron que tuviera el mejor rendimiento.

## Implementación de la compilación del lenguaje

Se implementó el parse LR 1, con el que se parsea las expresiones regulares y la cadena de entrada del programa. Para interpretar las expresiones regulares, se construye el AST utilizando la gramática atributada definida en regex_grammar.py, en la cual los atributos fueron definidos utilizando expresiones lambda. Utilizando dicho AST se construyó el automata de cada expresion regular y se aplico la propiedad de union de automatas dado en conferencia. Luego como dicho automata es finito no determinista, se aplico el algoritmo para transformarlo en una automata finito determinista. Una vez transformado, se utilizo en la creacion de los tokens de la cadena de entrada. Al obtener los tokens pasamos a eliminar todos los que representen caracteres de espacio, saltos de linea, etc y luego pasamos a la creacion del AST.
Ya obtenido el AST, realizamos es chequeo semantico y el chequeo de tipos por cada nodo. Por ultimo, si el chequeo semántico y de tipos es satisfactorio pasamos a la ejecucion de cada instrucción.
