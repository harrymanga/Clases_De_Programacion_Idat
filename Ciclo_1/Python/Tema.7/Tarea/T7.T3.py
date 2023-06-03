""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 3

print("Ingrese los datos necesarios")

# Ingreso de datos

c = 1

s = 0

l = ["", "+", "-", " ", ".", "*", "/"]

while True:

    while True:

        n = input(str(c) + ".- Ingrese un numero: ")

        if n.isalpha() or n in l:

            print("Dato ingresado incorrecto, ingrese solo precios de los productos")

        else:

            break

    s += int(n)

    if n == "0":

        break

    c += 1

# Operación

# Resultados

print("La suma de los números es: ", s)

print("Muchas Gracias, programa terminado.")
