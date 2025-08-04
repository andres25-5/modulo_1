"""
Crea un juego donde el programa "piensa" un número secreto entre 1 y 100
(puedes definirlo estáticamente, por ejemplo, numero_secreto = 42). El usuario
debe adivinarlo. En cada intento, el programa le dirá si el número ingresado es
mayor o menor que el número secreto. El juego termina cuando el usuario adivina
el número.
"""
import random

numero_secreto = random.randint(1, 100)


def adivinar_numero():
    """
    Esta función permite al usuario adivinar un número secreto entre 1 y 100.
    El usuario recibe pistas si su intento es mayor o menor que el número secreto.

     Args:
        numero_usuario (int): Numero a adivinar
        intentos(int): contador de intentos
    Returns:
        El numero adivinado (int)
        La cantidad de intentos (int)
    """


intentos = 0
while True:
    try:
        numero_usuario = int(input("Adivina el número secreto (entre 1 y 100): "))
        intentos += 1

        if numero_usuario < 1 or numero_usuario > 100:
            print("Por favor, ingresa un número entre 1 y 100.")
            continue

        if numero_usuario < numero_secreto:
            print("El número es mayor. Intenta de nuevo.")
        elif numero_usuario > numero_secreto:
            print("El número es menor. Intenta de nuevo.")
        else:
            print(f"¡Felicidades! Adivinaste el número {numero_secreto} en {intentos} intentos.")
            break
    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número entero.")
