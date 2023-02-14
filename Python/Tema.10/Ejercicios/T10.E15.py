""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 15

print("Ingrese los datos necesarios")

# Funciones

from random import randint

lista = []


def generarNum():

    for i in range(10):

        num = randint(10, 100)

        lista.append(num)

        print("Nº", i + 1, "=", num)

    return num


def rango(a):

    ran = 0

    for i in lista:

        if 60 <= i <= 70:

            ran += 1

    return ran


def múltiplo(b):

    mul = 0

    for i in lista:

        if i % 7 == 0:

            mul += 1

    return mul


def mayor(c):

    may = 0

    for i in lista:

        if 80 <= i:
            
            may += 1

    return may


# Ingreso de Datos

# Operación

# Resultados

print("Números Generados")

generarNum()

print("La cantidad de números generados en el rango de 60 a 70 es :", rango(lista))

print("La cantidad de números generados que son múltiplos de 7 son :", múltiplo(lista))

print("La cantidad de números generados mayores a 80 es :", mayor(lista))

print("Muchas Gracias, programa terminado.")
