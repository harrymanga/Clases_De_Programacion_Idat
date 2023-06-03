""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 16

print("Ingrese los datos necesarios")

# Ingreso de datos

while True:

    ng = input("Ingrese la cantidad de números a generar: ")

    if ng.isalpha() or ng == "":

        print("Dato ingresado incorrecto, ingrese solo números")

    else:

        break

while True:

    a = input("Ingrese el limite inferior del rango de números a generar: ")

    if a.isalpha() or a == "":

        print("Dato ingresado incorrecto, ingrese solo números")

    else:

        break

while True:

    b = input("Ingrese el limite superior del rango de números a generar: ")

    if b.isalpha() or b == "":

        print("Dato ingresado incorrecto, ingrese solo números")

    else:

        break

# Operación

from random import randint

print("N°\tNumero generado")

for i in range(int(ng)):

    nr = randint(int(a), int(b))

    print(i + 1, "\t", nr)

# Resultados

print("Muchas Gracias, programa terminado.")
