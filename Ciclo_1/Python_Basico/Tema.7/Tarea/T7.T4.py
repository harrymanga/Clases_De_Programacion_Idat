""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 4

print("Ingrese los datos necesarios")

# Ingreso de datos

c = 1

sumPares = 0

sumImpares = 0

l = ["", "+", "-", " ", ".", "*", "/"]

while True:

    while True:

        n = input(str(c) + ".- Ingrese un número: ")

        if n.isalpha() or n in l:

            print("Dato ingresado incorrecto, ingrese solo números")

        else:

            break

    if int(n) % 2 == 0:

        sumPares += int(n)

    else:

        sumImpares += int(n)

    if n == "0":

        break

    c += 1

# Operación

# Resultados

print("La suma de los números pares es: ", sumPares)

print("La suma de los números impares es: ", sumImpares)

print("La suma de los números totales es: ", sumPares + sumImpares)

print("Muchas Gracias, programa terminado.")
