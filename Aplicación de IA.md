# Aplicación de los conocimientos de IA

Para la implementación de que decisión va a tomar cada jugador a partir de un estado del partido se tomó como idea base el algoritmo de Minimax; aunque este no se puede aplicar de manera directa pues este algoritmo parte de que que se tienen dos jugadores y en este caso son **n** jugadores. Por tanto lo que se piensa hacer es marcar los objetivos de los jugadores en dependencia del estado del partido. 

Cada jugador puede actuar de dos modos: en ataque o en defensa. Si su equipo tiene el balón entonces jugará en modo ataque, de lo contrario en modo defensa. 

Es válido aclarar que con el objetivo de realizar una simulación más precisa, se divide el campo en tres zonas:

![Zonas del campo](/home/sheila/Escritorio/photo_2022-01-11_02-34-23.jpg)

La zona roja, amarilla y azul se le nombran como Finalización, Creación e Inicialización respectivamente. 

El árbol de los objetivos de los jugadores es: 

![Objetivos de jugador](/home/sheila/Escritorio/photo_2022-01-11_02-34-19.jpg)

Particularmente, el árbol del portero es: 

![Objetivos del portero](/home/sheila/Escritorio/photo_2022-01-11_02-34-27.jpg)
