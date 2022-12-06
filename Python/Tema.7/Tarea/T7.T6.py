""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 6

print("Solicite sus cartas para jugar a 21\n")

# Ingreso de datos

from random import randint

sumCartas = 0

while True:

    pedirCarta = input("¿Desea pedir una cartas (Si / No): ").capitalize()

    if pedirCarta == "Si":

        carta = randint(1, 13)

        print(carta)

        sumCartas += carta

        if sumCartas > 21:

            res = "Usted a Perdido, la suma de sus cartas es " + str(sumCartas)

            break

        if sumCartas == 21:

            res = "Usted a Ganado, la suma de sus cartas es " + str(sumCartas)

            break

    elif pedirCarta == "No":

        if sumCartas == 0:

            res = "Usted no eligió ninguna carta"

            break

        else:

            res = "Usted a Terminado de elegir cartas\n"

            break

    else:

        print("Respuesta incorrecta coloque Si o No")

# Operación

print(res)

if sumCartas != 0 and sumCartas < 21:

    print("La casa pedirá 3 cartas para competir con las tuyas\n")

    sumCartaGene = 0

    for i in range(3):

        cartaGene = randint(1, 13)

        sumCartaGene += cartaGene

        print("Carta generada Nº", i + 1, "es :", cartaGene)

    print()

    if sumCartaGene > 21:

        print("La casa Pierde con :", sumCartaGene, ", Usted Gana con :", sumCartas)

    elif sumCartas < sumCartaGene <= 21:

        print("La casa Gana con :", sumCartaGene, ", Usted Pierde con :", sumCartas)

    elif sumCartas == sumCartaGene:

        print("La casa Empata con :", sumCartaGene, ", Usted Empata con :", sumCartas)

    else:

        print("La casa Pierde con :", sumCartaGene, ", Usted Gana con :", sumCartas)

# Resultados

print("Muchas Gracias, programa terminado.")
