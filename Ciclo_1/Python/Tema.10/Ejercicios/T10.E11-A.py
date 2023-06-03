""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 11 - A

print("Ingrese los datos necesarios")

# Funciones


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


# Ingreso de Datos

numIng = pedirN("Ingrese un número en el rango de [1-6]: ")

# Operación

import random

numGen = random.randint(1, 6)

# Resultados

print("Número generado:", numGen)

adivinaNum(numIng, numGen)

print("Muchas Gracias, programa terminado.")
