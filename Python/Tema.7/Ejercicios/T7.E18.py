""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 18

print("Ingrese los datos necesarios")

# Ingreso de datos

while True:

    ng = input("Ingrese un numero comprendido entre 50 y 500: ")

    if ng.isalpha() or ng == "":

        print("Dato ingresado incorrecto, ingrese solo números")

    else:

        break

# Operación

from random import randint

print("N°\tNumero generado")

i = 0

while True:

    nr = randint(50, 600)

    i += 1

    print(i, "\t", nr)

    if nr > int(ng):

        break

# Resultados

print("Muchas Gracias, programa terminado.")
