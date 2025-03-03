import random
import os

def limpiar_pantalla():
    """Limpia la pantalla de la consola."""
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_mensaje_bienvenida():
    """Muestra el mensaje de bienvenida al juego."""
    print("Bienvenido al juego de Piedra, Papel o Tijera")
    print("El juego consiste en cuatro rondas.")
    print("Elige entre piedra, papel o tijera.")
    print("Reglas:")
    print("  - Piedra vence a tijera")
    print("  - Papel vence a piedra")
    print("  - Tijera vence a papel")
    print("  - Si ambos eligen lo mismo, es un empate")

def obtener_nombre_jugador():
    """Obtiene el nombre del jugador."""
    while True:
        nombre = input("Ingresa tu nombre: ").strip()
        if nombre:
            return nombre
        else:
            print("¡El nombre no puede estar vacío!")

def obtener_eleccion_jugador(nombre_jugador):
    """Obtiene la elección del jugador."""
    while True:
        eleccion = input(f"{nombre_jugador}, elige (piedra, papel, tijera): ").lower()
        if eleccion in ["piedra", "papel", "tijera"]:
            return eleccion
        else:
            print("¡Elección inválida! Elige piedra, papel o tijera.")

def obtener_eleccion_computadora():
    """Obtiene la elección de la computadora."""
    return random.choice(["piedra", "papel", "tijera"])

def determinar_ganador(jugador, computadora):
    """Determina el ganador de la ronda."""
    if jugador == computadora:
        return "Empate"
    elif (
        (jugador == "piedra" and computadora == "tijera") or
        (jugador == "papel" and computadora == "piedra") or
        (jugador == "tijera" and computadora == "papel")
    ):
        return "Jugador"
    else:
        return "Computadora"

def jugar_ronda(nombre_jugador, estadisticas, nombre_jugador2=None):
    """Juega una ronda del juego."""
    if nombre_jugador2:  
        eleccion_jugador1 = obtener_eleccion_jugador(nombre_jugador)
        limpiar_pantalla()
        eleccion_jugador2 = obtener_eleccion_jugador(nombre_jugador2)
        print(f"{nombre_jugador} eligió: {eleccion_jugador1}")
        print(f"{nombre_jugador2} eligió: {eleccion_jugador2}")
        ganador = determinar_ganador(eleccion_jugador1, eleccion_jugador2)
    else:  
        eleccion_jugador = obtener_eleccion_jugador(nombre_jugador)
        eleccion_computadora = obtener_eleccion_computadora()
        print(f"{nombre_jugador} eligió: {eleccion_jugador}")
        print(f"Computadora eligió: {eleccion_computadora}")
        ganador = determinar_ganador(eleccion_jugador, eleccion_computadora)

    if ganador == "Empate":
        print("¡Empate!")
        estadisticas["empates"] += 1
    elif ganador == "Jugador":
        print(f"¡{nombre_jugador} gana!")
        estadisticas["victorias_jugador"] += 1
    else:
        if nombre_jugador2:
            print(f"¡{nombre_jugador2} gana!")
        else:
            print("¡Computadora gana!")
        estadisticas["victorias_computadora"] += 1

    estadisticas["rondas_jugadas"] += 1

def mostrar_estadisticas(estadisticas, nombre_jugador, nombre_jugador2=None):
    """Muestra las estadísticas del juego."""
    print("\nEstadísticas:")
    print(f"Rondas jugadas: {estadisticas['rondas_jugadas']}")
    print(f"Victorias de {nombre_jugador}: {estadisticas['victorias_jugador']}")
    if nombre_jugador2:
        print(f"Victorias de {nombre_jugador2}: {estadisticas['victorias_computadora']}")
    else:
        print(f"Victorias de la computadora: {estadisticas['victorias_computadora']}")
    print(f"Empates: {estadisticas['empates']}")

def mostrar_estadisticas_ultima_partida(estadisticas_ultima_partida, nombre_jugador, nombre_jugador2=None):
    """Muestra las estadísticas de la última partida."""
    print("\nEstadísticas de la última partida:")
    print(f"Rondas jugadas: {estadisticas_ultima_partida['rondas_jugadas']}")
    print(f"Victorias de {nombre_jugador}: {estadisticas_ultima_partida['victorias_jugador']}")
    if nombre_jugador2:
        print(f"Victorias de {nombre_jugador2}: {estadisticas_ultima_partida['victorias_computadora']}")
    else:
        print(f"Victorias de la computadora: {estadisticas_ultima_partida['victorias_computadora']}")
    print(f"Empates: {estadisticas_ultima_partida['empates']}")

def jugar_de_nuevo():
    """Pregunta si el jugador quiere jugar de nuevo."""
    while True:
        respuesta = input("¿Jugar de nuevo? (si/no): ").lower()
        if respuesta in ["si", "no"]:
            return respuesta == "si"
        else:
            print("Respuesta inválida. Ingresa 'si' o 'no'.")

def main():
    """Función principal del juego."""
    mostrar_mensaje_bienvenida()
    nombre_jugador = obtener_nombre_jugador()
    estadisticas_ultima_partida = {}  

    while True:
        estadisticas = {
            "rondas_jugadas": 0,
            "victorias_jugador": 0,
            "victorias_computadora": 0,
            "empates": 0,
        }

        print("\nMenú:")
        print("1. Jugar contra la computadora")
        print("2. Multijugador (2 jugadores)")
        print("3. Ver estadísticas de la última partida")
        print("4. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            for _ in range(4):
                jugar_ronda(nombre_jugador, estadisticas)
            estadisticas_ultima_partida = estadisticas.copy()
            mostrar_estadisticas(estadisticas, nombre_jugador)
        elif opcion == "2":
            nombre_jugador2 = obtener_nombre_jugador()
            for _ in range(4):
                jugar_ronda(nombre_jugador, estadisticas, nombre_jugador2)
            estadisticas_ultima_partida = estadisticas.copy()
            mostrar_estadisticas(estadisticas, nombre_jugador, nombre_jugador2)
        elif opcion == "3":
            if estadisticas_ultima_partida:  
                if "nombre_jugador2" in estadisticas_ultima_partida:
                    mostrar_estadisticas_ultima_partida(estadisticas_ultima_partida, nombre_jugador, estadisticas_ultima_partida["nombre_jugador2"])
                else:
                    mostrar_estadisticas_ultima_partida(estadisticas_ultima_partida, nombre_jugador)
            else:
                print("No hay estadísticas de la última partida disponibles.")
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")

        if not jugar_de_nuevo():
            break

if __name__ == "__main__":
    main()