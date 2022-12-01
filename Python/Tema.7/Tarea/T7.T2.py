""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 2

print("Ingrese los datos necesarios")

# Ingreso de datos

# Operación

a = 10

s = 0

print("Nº\tSerie")

for i in range(20):

    a += i

    s += a

    print(i + 1, "------>", a)

# Resultados

print("La suma de la serie es:", s)

print("El promedio de la serie es:", round(s / 20, 2))

print("Muchas Gracias, programa terminado.")
