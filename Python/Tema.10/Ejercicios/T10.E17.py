""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 17

print("Ingrese los datos necesarios")

# Funciones

from random import randint

listaSumas = []


def generarNota():

    suma = 0

    for i in range(5):

        nota = randint(0, 20)

        suma += nota

        print("Nº", i + 1, "=", nota)

    if len(listaSumas) > 0:

        listaSumas.remove(listaSumas[0])

    return listaSumas.append(suma)


def resultado(b):

    c = round(b / 5, 2)

    if 13 <= c:

        res = "El alumno aprobó con : " + str(c)

    else:

        res = "El alumno desaprobó con : " + str(c)

    return res


# Ingreso de Datos

# Operación

# Resultados

print("Notas del alumno")

for i in range(10):

    print("Las notas del alumno N°", i + 1, "son :")

    generarNota()

    print(resultado(listaSumas[0]), "\n")


print("Muchas Gracias, programa terminado.")
