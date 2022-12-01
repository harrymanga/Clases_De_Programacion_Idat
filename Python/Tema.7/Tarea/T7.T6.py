""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 6

print("Ingrese los datos necesarios")

# Ingreso de datos

l = ["", "+", "-", " ", ".", "*", "/"]

while True:

    n1 = input("Ingrese el primer número entre 0 y 20: ")

    if n1.isalpha() or n1 in l or 0 > int(n1) or int(n1) > 20:

        print("Dato ingresado incorrecto, ingrese solo números entre 0 y 20")

    else:

        break

while True:

    n2 = input("Ingrese el primer número entre 0 y 20: ")

    if n2.isalpha() or n2 in l or 0 > int(n2) or int(n2) > 20:

        print("Dato ingresado incorrecto, ingrese solo números entre 0 y 20")

    else:

        break

# Operación

from random import randint

lng = []

print("Nº\tNumero Generado")

for i in range(2):

    ng = randint(0, 20)

    lng.append(ng)

    print(i + 1, "\t", ng)

if n1 in lng and n2 in lng:

    res = "El par de números ingresados coinciden"

else:

    res = "El par de números son diferentes"

# Resultados

print(res)

print("Muchas Gracias, programa terminado.")
