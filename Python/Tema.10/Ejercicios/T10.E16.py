""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 16

print("Ingrese los datos necesarios")

# Funciones

from random import randint

lista = []


def generarNum():

    for i in range(5):

        num = randint(0, 20)

        lista.append(num)

        print("Nº", i + 1, "=", num)

    return num


def resultado(a):

    b = sum(a) / len(a)

    if 13 <= b:

        res = "El alumno aprobó con : " + str(b)

    else:

        res = "El alumno desaprobó con : " + str(b)

    return res


# Ingreso de Datos

# Operación

# Resultados

print("Notas del alumno")

generarNum()

print(resultado(lista))

print("Muchas Gracias, programa terminado.")
