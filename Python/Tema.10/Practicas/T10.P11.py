""

# Ejercicio 10

import random


def pedirN(m):

    while True:

        n = int(input("ingrese un numero en el rango de [1-6]: "))

        if 1 <= n <= 6:

            break

        else:

            print("Dato incorrecto")

    return n


def adivinaNum(x, y):
    if x == y:

        m = "Ud. ha ganado"

    else:

        m = "Ud. ha perdido"

    print(m)


# Programa Principal

numIng = pedirN("Ingrese un número en el rango de [1-6]: ")

numGen = random.randint(1, 6)

print("Número generado:", numGen)

adivinaNum(numIng, numGen)
