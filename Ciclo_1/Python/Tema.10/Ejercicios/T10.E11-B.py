""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 11 - B

print("Ingrese los datos necesarios")

# Funciones


def números(a, b):

    if a == b:

        r = "GANÓ! Los números " + str(a) + " y " + str(b) + " son iguales"

    else:

        r = "PERDIÓ! Los números " + str(a) + " y " + str(b) + " no son iguales"

    return r


# Ingreso de Datos

while True:

    n1 = int(input("Ingrese un número de 1 a 6: "))

    if n1 >= 1 and n1 <= 6:

        break

# Operación

from random import randint

n2 = randint(1, 6)

# Resultados

print(números(n1, n2))

print("Muchas Gracias, programa terminado.")
