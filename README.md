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

Para tener una mejor experiencia al programar en el lenguaje que se propone se debe instalar la extensión FSIM, para ello es necesario que se sigan los siguientes pasos:

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
* strategy
* report
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
* rangeint
* rangefloat
* rangechoice
* rangebool

### Symbols

* Assignment: =
* Brackets: (, ), {, }, [, ]
* Operators: >, <, >=, <=, ==, !=

### Separators

* ;
* ,


### Definición de tipos

#### PLAYER

``` 
player:
   - name: str
   - pos: DEL, MC, DEF or GK
   - age: int
   - country: str
   - list_prob: lista de 12 elementos 
   -  st: Estrategia (opcional)
```

#### Goalkeeper

```
goalkeeper:
   - name: str
   - pos: DEL, MC, DEF or GK
   - age: int
   - country: str
   - list_prob: lista de 12 elementos 
   - goalkeeper_prob:lista de 5 elementos
   -  st: Estrategia (opcional)
```


**Nota**: Los elementos de la lista de probabilidades (*list_prob*) de que un jugador ejecute correctamente las acciones. El orden de los valores es el siguiente: 

* Tiro a portería
* Pase
* Interceptar balón
* Recibir balón
* Saque de banda
* saque de esquina
* Despejar balón
* Avanzar posición
* Falta leve
* Falta moderada
* Falta grave
* Retroceder posicion

Los elementos de la lista de probabilidades  (*goalkeeper_prob*) de que un portero ejecute correctamente las acciones. El orden de los valores es el siguiente:

* Atajar balón
* Sin rebote
* Rebote por banda
* Rebote por línea final
* Rebote jugador
* Saque de portería

#### TEAM

```
team:
  -  name: str
  -  players: list of player
  -  manager: manager
  -  country: str
```

#### GAME

```
game:
  - eq1: Team
  - eq2: Team
  - referees: list of referee
```

#### MANAGER

```
manager:
   - name: str
   - experience: int
   - country: str
   - age: int
```

#### REFEREE

```
referee:
   - name: str
   - experience: int
   - country: str
   - age: int
   - list_prob : lista de 4 elementos

```

**Nota**: Los elementos de la lista de probabilidades (*list_prob*) de que un árbitro ejecute correctamente las acciones. El orden de los valores es el siguiente: 

* Cantar falta
* Sacar tarjeta
* Sacar tarjeta amarilla
* Sacar tarjeta roja

### Ejemplo de sintaxis

#### Inicialización

```
Inicialización de un player
    player p1 = (name="Leonel Messi", age=34, pos="DEL", list_prob=[...], country="Argentina");

Inicialización de un goalkeeper
    goalkeeper g1 = (name="Ter Stergen", country="Alemania", age=32, pos="GK", goalkeeper_prob=[...], list_prob=[...]);

Inicialización de un manager
    manager m1 = (name="Xavi", country="Spain", experience=76, age=45);

Inicialización de un referee
    referee r1 = (name="Juan", country="Portugal", experience=89, age=56, list_prob=[...]);

Inicialización de un team
    team t1 = (name="Real Madrid", country="Spain", coach=m1, players=[...]);

Inicializacion de un game
    game g1 = (eq1= t1, eq2= t2, referees = [r1, r2]);
```
#### Declaración de listas

```
    player p [ p1, p2, p3, .... ];
```

#### Indexación de listas

```
   int a[1,2,3];
   int b = a[0];
   int c = a[-21];    
```

**Nota**: La indexación en las listas es muy parecida a la de los lenguajes más utilizados, la única diferencia es que se trata como una lista "circular" por lo que no existen excepciones por índices fuera de rango.  
#### Asignación

```
    p1 = p2; # se le asigna a p1 el valor de p2
```

#### Acceso a propiedades

```
    player.name; # se accede a la propiedad name de player
```

#### For

```
    for item in t.players{
        ...
    };
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
    function type id (args) { };
```

#### Definición de range

```
    rangeint r1 = (li=3, ls=8, distribution=f)
    rangebool r2 = ()
    rangefloat r3 = (li=2.1, ls=4.7)
    rangechoice r4 = (values=[...])
```

#### Definición de estrategias

```
strategy name{
	variables{
	   name_action = value,
	   name_action1 = rangeint(0, 5, f),
	   name_action2 = rangebool(),
	};
	execute(state_game, player){
		if name_action1 > 10 and state_game.pos_balon == player:
			return 'BALL_PASS'
	};
};
```
**Nota**: `execute` de una estrategia debe devolver un *str* que corresponda al nombre de una de las variables que se definieron en el apartado de las variables.

---
# Detalles de la implementación

## Implementación de la compilación del lenguaje

Se implementó el parser LR 1, con el que se parsea las expresiones regulares y la cadena de entrada del programa. La decisión de implementar este parser viene dada porque al ser compleja la gramática del lenguaje que se propone puede traer como consecuencia ambigüedades en la misma. 

### Análisis Léxico

Primeramente se define las expresiones regulares del lenguaje para el reconocimiento de cada posible token y una gramática para parsear cada una de estas expresiones, esto se encuentra en `regex.py` y consiste en un diccionario donde se guardan los elementos de la forma que la llave es el tipo de token y el valor es la expresión regular correspondiente. Por otro lado, la gramática para las expresiones regulares se define en `regex_gramar.py`, o sea, los terminales, los no terminales y las produciones, en la cual los atributos se definen con el uso de expresiones lambda.

Luego para interpretar las expresiones regulares, se crea el AST con el uso de la gramática atributada y consigo un autómata por cada expresion regular en `lrparser.py`; para después aplicar la propiedad de unión de autómata, todo se encuentra en `lexer.py`.

Como dicho automata es finito no determinista, se aplicó el algoritmo que se dió en conferencias para transformarlo en una autómata finito determinista. Una vez que se trasnforma, se utiliza en la creación de los tokens de la cadena de entrada. Al obtener los tokens pasamos a eliminar todos los que representen caracteres de espacio, saltos de línea, etc.

### Análisis Sintáctico

Se utiliza los tokens que devuelve por el lexer, se aplica el parser LR 1 y se obtiene el AST correspondiente a la cadena de entrada.

Para el diseño del AST, se clasificaron las expresiones del lenguaje en expresiones e instrucciones. 

Las expresiones constan de un método `evaluate` y se clasifican en expresiones atómicas y operadores. Las expresiones atómicas son: `arrayAtom`, `boolNode`, `funcCall`, `idNode`, `idProperty`, `indexNode`, `lenNode`, `numberNode` y `strNode`. Los operadores se componen por todos los operadores definidos en el lenguaje.

Las instrucciones tienen un método `execute`. Se tiene un tipo específico de instrucción que es `variableNode` que es cuando se va a inicializar cualquier tipo de variable, estas a su vez se dividen en 4 tipos: `arrayDeclaration`, `assignNode`, `declaration`, `reassignNode`. El resto de las instrucciones heredan directamente de la clase `instruction`, estas son:  `breakNode`, `continueNode`, `conditional`, `executeNode`, `forNode`, `functionNode`, `printNode`, `returnNode` y `strategyNode`.

Cada uno de los nodos del AST contienen un método `checkSemantic` que recibe un scope y contiene un método `visit` que se emplea en el chequeo de tipos

### Análisis Semántico y Ejecución

Después de obtener el AST, se realiza el chequeo semántico y el chequeo de tipos por cada nodo. Por último, si el chequeo semántico y de tipos es satisfactorio se pasa a la ejecución de cada instrucción.

## Implementación de la simulación de un partido

Un partido es el ambiente donde los agentes se desarrollan e interactúan entre sí. Este ambiente se cataloga como:

- *Accesible*, pues los agentes, para tomar la decisión de que acción realizar, tienen acceso a un estado del partido y a toda su información. 

- *No determinista*, pues no se puede saber con exactitud que consecuencias tendrán las acciones de los agentes sobre él. Un ejemplo de esto es si un jugador *X* realiza un pase al jugador *Y*, entonces el balón puede ser que llegue a su destino o sea interceptado por otro jugador.  

- *Episódico*, pues los agentes para decidir que acción tomar solo tienen en cuenta el estado actual del partido sin tener en cuenta las consecuencias que puede traer la misma.

- *Estático*, pues un partido solo se modifica si uno de los agentes realiza una acción en él.

- *Discreto*, pues en un partido exiten un número fijo y finito de acciones que lo pueden modificar que son exactamente el conjuto de las acciones que puede realizar un agente.


### Definición de `Accion`

Para definir las acciones se tiene la clase abstracta `Accion`. Se tomó como plantilla la representación de acciones en STRIPS que se vió en las clases de IA, por tanto los métodos que tiene esta clase son:

- Descripción
- Precondición
- Ejecutar
- Poscondición

### Definición de `Agente`

Para definir los agentes se tiene una clase abstracta `Agente` de la cual todos van a heredar, pues deben tener:

- El método `acciones_dict` donde se inicializa y se retorna un diccionario con todas las acciones que va a tener el agente.

- El método `escoger_accion_estrategia` que es el que se encarga de, dado un estado de un partido y los valores de las variables de la estrategia que tiene el agente, hacer un llamado al execute de la misma, y devuelve la instancia de la acción correspondiente. En caso de que la acción que decida la estrategia no se pueda ejecutar, ya que no se cumple su precondición, o que el agente no se le asigne una estrategia en su creación, entonces se hace una llamada al método `escoger_acción_base` donde se aplica una especie de lógica difusa, ya que en dependencia de determinados estados del partido es la acción que se realiza, además de tener siempre en cuenta que las precondiciones de las mismas se cumplan.

#### `Jugador`

En `escoger_accion_base` se tiene en cuenta las reglas convencionales establecidas para un partido de fútbol, por tanto, si el estado del partido es `INICIAR_PARTIDO` o `REANUDAR_PARTIDO` y se cumple la precondición de `PASE` entonces esta es la acción que se elige. Si este no es el caso, entonces, se filtra todas las acciones que puede ejecutar el jugador, si la ultima acción es un `Pase` y entre las acciones que puede realizar está `Recibir Balón` entonces es esta la acción que se escoge, en caso contrario, se escoge aleatoriamente entre todas las acciones posibles o no hacer nada (`DEFAULT`).

En caso de que se escoja hacer un pase, para escoger al jugador al que se le hace el pase se tiene en cuenta su ubicación en el campo y la de los demás jugadores de su equipo, ya que hay más posibilidad de que se le haga un pase a un jugador que esté en su misma zona en el campo que de otra.

#### `Portero`

La clase `Portero` hereda de la clase `Jugador` pues es un tipo particular de esta, ya que puede realizar las mismas acciones que un jugador a excepción de `SAQUE_BANDA` y `DESPEJAR_BALON` y además se le suman dos más: `ATAJAR` y `SAQUE_PORTERIA`, lo que trae consigo que se agreguen la probabilidad de que ejecute correctamente estas acciones.

En `escoger_accion_base` si la última acción es un tiro a portería y el estado del partido es `EN_JUEGO` entonces la acción que se elige es `ATAJAR`. Por otro lado, si se cumple la precondición de `SAQUE_PORTERIA` entonces es la acción que se elige. Por otro lado si la última acción es `ATAJAR` y esta se realizó sin rebote entonces, el portero realizará un pase. Si ninguno de los anteriores es el caso, entonces, elige la acción a realizar igual que lo hace un jugador cuando no se cumple ninguno de los casos particulares.

#### `Manager`

El manager solo puede realizar dos acciones: `Hacer_cambio` y `Escoger_alineacion`, esta última solo la realizará al inicializar un partido.

Luego cuando se cree un equipo y se le asigne como su propio manager entonces se actualiza el atributo `equipo`. 

#### `Árbitro`

El árbitro solo puede realizar dos acciones: `Sacar_tarjeta` y `Cantar_Falta`. La acción `Cantar_Falta` solo se ejecuta si un jugador realiza una falta. En caso de que el árbitro decida cantarla entonces se muestra la tarjeta correspondiente según la gravedad de la falta. 

### Definición de `Equipo`

Un equipo se conforma por un conjunto de jugadores y un manager, tiene un nombre y una lista con los jugadores en el campo y otra con los jugadores en la banca que se actualiza cuando el manager elige la alineación para un partido.

### Definición de `Partido`

Para la simulación de un partido se tiene una clase con el mismo nombre que contiene como atributos:

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

Además tiene como método principal para la simulación del partido `simular` y como secundarios: `__iniciar_partido` y `__reanudar_partido_pos_gol`.

El método ``simular`` recibe la cantidad de minutos que se quiere simular (por defecto 90), luego por cada iteración, hasta que se cumplan estos minutos de un partido, cada agente decide para el estado actual del partido que acción van a realizar con el método `escoger_accion_estrategia`, para luego ejecutarlas.

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

`Range` es una clase abstracta de la cual heredan los diferentes tipos de variables que se pueden utilizar para la definición de una estrategia. `Range` tiene el método `get_value` que devuelve un valor de acuerdo al tipo de `Range`. 

#### `RangeInt` y `RangeFloat`

Para inicializar una variable de tipo `RangeInt` se necesita el límite inferior y superior del intervalo en el que se encuentran los valores, además se le puede pasar una función que reciba un parámetro del mismo tipo de la variable que representa la distribución de como se va a comportar la variable.

#### `RangeBool`

Este tipo de variable no recibe un intervalo pues, como se puede intuir del nombre, solo existen dos posibles valores que puede tomar: `True` o `False`, luego solo recibe, si se desea, una función que represente una distribución.

#### `RangeChoice`

Este tipo de variable da la libertad que los valores que puede tomar no tienen que ser de ningún tipo específico por lo tanto recibe una lista de valores y una función que representa una distribución si se desea.

### Definición de `Estrategia`

La clase `Estrategia` consta de un diccionario de variables y un execute. El diccionario de variables pueden contener variables con un valor específico o de cualquier tipo que herede de `Range`. El execute es la función que implementa el usuario para decidir el comportamiento del agente. 

### Definición de `Optimizador`

La clase `Optimizador` es la que se va a encargar de al inicializar un partido asignarle valores exactos a las variables de tipo `Range` que tenga la estrategia de cada uno de los agentes que se relacionan en el partido. Para ello se realiza una metaheurística genérica, donde por cada equipo se crea varias instancias del mismo con variaciones en los valores de la estrategia de cada agente del equipo. Con estas instancias se realiza un torneo de eliminación directa. En cada uno de los enfrentamientos los equipos se mezclan teniendo en cuenta el rendimiento de cada agente, luego con el resultado de cada mezcla se crean nuevos enfrentamientos, o sea, es el equipo que pasa a la siguiente fase y se repite el proceso, hasta llegar a la final, donde el equipo final es con el que se realiza la simulación.

