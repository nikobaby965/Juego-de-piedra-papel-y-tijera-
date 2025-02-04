import random
def jugar():
    print ("Hola jugador")
    print ("El juego se trata de 3 Rondas, si empatas en una ronda ¡son 4!")
    print ("el juego tiene las siguientes reglas")
    print ("tienes que elegir entre piedra , papel o tijera")
    print  ("si eliges piedra y el rival tijera, gana ¡piedra!")
    print ("si eliges tijera y el rival papel, gana ¡tijera!")
    print ("si eliges papel y el rival piedra, gana ¡papel!")
    print ("¿Estas listo? Si,No")
    print ("Comencemos")
    usuario = input("Elige: Piedra, Papel o Tijera: ").lower()
    rival = random.choice(["piedra", "papel", "tijera"])

    print(f"Tu elegiste {usuario}, rival eligio {rival}.")

    if usuario == rival:
        return "¡Empate!"

    if ganador(usuario, rival):
        return "¡Victorioso!"

    return "¡Que pena, perdiste!"

def ganador(jugador1, jugador2):
    if (jugador1 == "piedra" and jugador2 == "tijera") or \
       (jugador1 == "papel" and jugador2 == "piedra") or \
       (jugador1 == "tijera" and jugador2 == "papel"):
        return True
    return False

print(jugar())
