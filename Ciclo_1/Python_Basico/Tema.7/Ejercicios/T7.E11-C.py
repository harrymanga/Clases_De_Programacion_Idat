""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 11 - C

print("Ingrese los datos necesarios")

# Ingreso de datos

# Operación

c = 1

s = 0

while True:

    n = int(input(str(c) + ".- Ingrese un numero: "))

    if n % 2 == 0:

        s += n

    if n == 0:

        break

    c += 1


# Resultados

print("La suma de las estaturas es: ", s)

print("Muchas Gracias, programa terminado.")
