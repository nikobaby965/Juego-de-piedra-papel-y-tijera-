# Juego-de-piedra-papel-y-tijera-
Descripción 

" Piedra, papel o tijera , es un juego muy simple y a la vez muy divertido y rápido de jugar
 
¿Como se juega?

En este juego, tienes dos opciones para  jugar ya sea  con un amigo o con la computadora de manera individual, las reglas son muy simples de entender, solmente tienes que elegir tres opciones, en las cuales son la piedra, el papel y la tijera no puedes escribir ningún otro elemento que no sean estos tres. Ejemplo si el jugador 1 elige piedra y el jugador dos o la computadora elige papel, aqui gana papel, ya que el papel envuelve a la piedra, otro ejemplo podría ser si tu eliges piedra y el rival piedra esto es un empate nadie gana, otro ejemplo podría ser si tu eliges tijera y el rival papel gana tijera ya que la tijera recorta al papel, y por último si tu eliges piedra y el rival tijera tu ganas ya que la piedra destroza a la tijera. 


¿En donde se creo este lenguaje de programación?

Se creo en Visual Studio Code, el lenguaje de programación fue pyton con la versión 3.11.9

Principales funcionalidades del código 

Implementa las reglas clásicas del juego.
Permite al jugador elegir entre "piedra", "papel" o "tijera".
La computadora realiza una elección aleatoria.
Determina el ganador de cada ronda.
Modo de Juego Contra la Computadora:
Permite al jugador enfrentarse a la computadora en una serie de rondas.
Modo Multijugador:
Ofrece la opción de que dos amigos se enfrenten entre sí.
Validación de Entrada del Usuario:
Asegura que el jugador ingrese opciones válidas (nombres y elecciones).
Registro de Estadísticas:
Lleva un registro de:
Rondas jugadas.
Victorias del jugador.
Victorias de la computadora (o del segundo jugador).
Empates.
Guarda las estadisticas de la ultima partida jugada.
Presentación de Estadísticas:
Muestra las estadísticas al final de cada partida.
Muestra las estadisticas de la ultima partida cuando el usuario lo solicita.
Menú de Opciones:
Proporciona un menú claro para que el jugador elija entre:
Jugar contra la computadora.
Jugar en modo multijugador.
Ver las estadisticas de la ultima partida.
Salir del juego.
Función de Repetición del Juego:
Pregunta al jugador si desea jugar otra partida.
Limpieza de Pantalla:
Limpia la consola para mejorar la experiencia del usuario entre rondas.
Funcionalidades Detalladas:

limpiar_pantalla():
Limpia la pantalla de la consola, adaptándose a diferentes sistemas operativos (Windows o Linux/macOS).
mostrar_mensaje_bienvenida():
Muestra un mensaje de bienvenida con las reglas del juego.
obtener_nombre_jugador():
Solicita y valida el nombre del jugador.
obtener_eleccion_jugador():
Solicita y valida la elección del jugador.
obtener_eleccion_computadora():
Genera una elección aleatoria para la computadora.
determinar_ganador():
Compara las elecciones del jugador y la computadora (o los dos jugadores) y determina el ganador.
jugar_ronda():
Ejecuta una ronda del juego, registrando el resultado y actualizando las estadísticas.
mostrar_estadisticas():
Muestra las estadísticas acumuladas de la partida actual.
mostrar_estadisticas_ultima_partida():
Muestra las estadisticas de la ultima partida jugada.
jugar_de_nuevo():
Pregunta si el jugador quiere jugar otra partida.
main():
La función principal que coordina todas las demás funciones y ejecuta el juego.



