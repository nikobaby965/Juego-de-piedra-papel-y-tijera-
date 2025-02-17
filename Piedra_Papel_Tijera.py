import random
import os
print("Bienvenido")
print ("el juego consiste de cuatro rondas, en donde tienes que elegir una de las tres opciones válidas")
print ("puedes elegir entre piedra, papel o tijera")
print ("si eliges piedra y tu rival tijera, ganas la primera ronda")
print("si eliges ya sea piedra, papel o tijera y tu rival elige la misma opción, es un ¡empate!")
print ("si eliges papel y tu rival piedra, ganas la ronda")
print ("Si eliges papel y tu rival tijera,pierdes la ronda")
print("hasta alcanzar las 4 rondas")
def obtener_nombre_jugador():
    """ingresa tu Nickname favorito"""
    while True:
        nombre = input("Ingresa tu Nickname: ")
        if nombre.strip(): 
            return nombre.strip()
        else:
            print("¡El nombre es obligatorio, ingresa tu nombre favorito :).")

def obtener_eleccion_jugador(nombre_jugador):
    """Elige una de las tres opciones válidas."""
    while True:
        eleccion = input(f"{nombre_jugador}, elige piedra, papel o tijera: ").lower()
        if eleccion in ["piedra", "papel", "tijera"]:
            return eleccion
        else:
            print("¡Elige entre piedra,papel o tijera, y se el ganador.")

def obtener_eleccion_computadora():
    """La computadora elige aleatoriamente piedra, papel o tijera."""
    return random.choice(["piedra", "papel", "tijera"])

def determinar_ganador(jugador, computadora):
    """Determina quién gana según las reglas del juego."""
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

def jugar_contra_computadora(nombre_jugador, estadisticas):
    """Juega contra la computadora y actualiza las estadísticas."""
    for i in range(4):
        eleccion_jugador = obtener_eleccion_jugador(nombre_jugador)
        eleccion_computadora = obtener_eleccion_computadora()

        print(f"Tu elección: {eleccion_jugador}")
        print(f"Elección de la computadora: {eleccion_computadora}")

        ganador = determinar_ganador(eleccion_jugador, eleccion_computadora)

        if ganador == "Empate":
            print("¡Es un empate, adelantate a tu contricante!")
            estadisticas["empates"] += 1
        elif ganador == "Jugador":
            print(f"¡{nombre_jugador} ganaste una de 4 rondas, sigue así !")
            estadisticas["victorias_jugador"] += 1
        else:
            print("¡Perdiste, piensa mejor la otra ronda, y sal victorioso !")
            estadisticas["victorias_computadora"] += 1

        estadisticas["rondas_jugadas"] += 1

def jugar_multijugador(nombre_jugador1, nombre_jugador2, estadisticas):
    """Juega multijugador y actualiza las estadísticas."""
    for i in range(4):  
    
        os.system('cls' if os.name == 'nt' else 'clear')

        eleccion_jugador1 = obtener_eleccion_jugador(nombre_jugador1)

        os.system('cls' if os.name == 'nt' else 'clear')

        eleccion_jugador2 = obtener_eleccion_jugador(nombre_jugador2)

        print(f"Elección de {nombre_jugador1}: {eleccion_jugador1}")
        print(f"Elección de {nombre_jugador2}: {eleccion_jugador2}")

        ganador = determinar_ganador(eleccion_jugador1, eleccion_jugador2)

        if ganador == "Empate":
            print("¡Es un empate, no se den por vencidos!")
            estadisticas["empates"] += 1
        elif ganador == "Jugador":
            print(f"¡{nombre_jugador1} ganaste, tienes la delantera!")
            estadisticas["victorias_jugador"] += 1
        else:
            print(f"¡{nombre_jugador2} ganaste, sigue así!")
            estadisticas["victorias_computadora"] += 1

        estadisticas["rondas_jugadas"] += 1

def mostrar_estadisticas(estadisticas):
    """Muestra las estadísticas del juego."""
    print("\nEstadísticas del juego:")
    print(f"Rondas jugadas: {estadisticas['rondas_jugadas']}")
    print(f"Victorias de {nombre_jugador} : {estadisticas['victorias_jugador']}")
    print(f"Victorias de la computadora: {estadisticas['victorias_computadora']}")
    print(f"Empates: {estadisticas['empates']}")

def mostrar_estadisticas_ultima_partida(estadisticas_ultima_partida):
    """Muestra las estadísticas de la última partida."""
    print("\nEstadísticas de la última partida:")
    print(f"Rondas jugadas: {estadisticas_ultima_partida['rondas_jugadas']}")
    print(f"Victorias de {nombre_jugador}: {estadisticas_ultima_partida['victorias_jugador']}")
    print(f"Victorias de la computadora: {estadisticas_ultima_partida['victorias_computadora']}")
    print(f"Empates: {estadisticas_ultima_partida['empates']}")

def jugar_de_nuevo():
    """No te quedes picado, juega nuevamente"""
    while True:
        respuesta = input("¿dale otra? (si/no): ").lower()
        if respuesta in ["si", "no"]:
            return respuesta == "si"
        else:
            print("¡Entrada no válida! Inténtalo de nuevo.")

nombre_jugador = obtener_nombre_jugador()

estadisticas = {
    "rondas_jugadas": 0,
    "victorias_jugador": 0,
    "victorias_computadora": 0,
    "empates": 0,
}

estadisticas_ultima_partida = {
    "rondas_jugadas": 0,
    "victorias_jugador": 0,
    "victorias_computadora": 0,
    "empates": 0,
}

while True:
    print("\nMenú principal:")
    print("1. Jugar contra la computadora")
    print("2. Multijugador (2 jugadores)")
    print("3. Ver estadísticas de la última partida")
    print("4. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        jugar_contra_computadora(nombre_jugador, estadisticas)
        estadisticas_ultima_partida = estadisticas.copy() 
    elif opcion == "2":
        nombre_jugador2 = obtener_nombre_jugador()
        jugar_multijugador(nombre_jugador, nombre_jugador2, estadisticas)
        estadisticas_ultima_partida = estadisticas.copy() 
    elif opcion == "3":
        mostrar_estadisticas_ultima_partida(estadisticas_ultima_partida)
    elif opcion == "4":
        break
    else:
        print("Opción no válida. Inténtalo de nuevo.")

    mostrar_estadisticas(estadisticas) 
    if not jugar_de_nuevo():
        break
