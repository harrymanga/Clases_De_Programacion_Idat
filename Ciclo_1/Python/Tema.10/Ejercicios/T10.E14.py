""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 14

print("Ingrese los datos necesarios")

# Funciones


def numeroInt(a):

    numInt = input(a)

    while True:

        if numInt.isdigit():

            numInt = int(numInt)

            break

        else:

            numInt = input("Dato invalido, Ingresar el numero de ventas a registrar : ")

    return numInt


def numeroFloat(b):

    numFloat = input(b)

    while True:

        if numFloat.isalpha() or float(numFloat):

            numFloat = float(numFloat)

            break

        else:

            numFloat = input("Dato invalido, Ingresar el monto a registrar : ")

    return numFloat


def promedioVent(c):

    return sum(c) / len(c)


# Ingreso de Datos

ventas = numeroInt("Ingrese el numero de ventas a registrar : ")

# Operación

lista = []

for i in range(ventas):

    montos = numeroFloat("Ingrese el monto de las venta Nº " + str(i + 1) + " : ")

    lista.append(montos)

# Resultados

print("El promedio de las ventas es : S/.", round(promedioVent(lista), 2))

print("Muchas Gracias, programa terminado.")
