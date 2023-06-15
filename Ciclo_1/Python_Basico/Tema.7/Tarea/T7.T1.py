""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 1

print("Ingrese los datos necesarios")

# Ingreso de datos

# Operación

a = 7

s = 0

print("Nº\tSerie")

for i in range(50):

    a += i

    s += a

    print(i + 1, "------>", a)

# Resultados

print("La suma de la serie es:", s)

print("Muchas Gracias, programa terminado.")
