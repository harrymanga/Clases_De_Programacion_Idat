""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 6 - C

print("Ingrese los datos necesarios")

# Funciones


def opeTriangulo(a, b, c):

    p = (a + b + c) / 2

    área = (p * (p - a) * (p - b) * (p - c)) ** 0.5

    print("el área es:", round(área, 2), "\nel perímetro es", 2 * p)


# Ingreso de Datos

a = float(input("ingrese lado 1: "))

b = float(input("ingrese lado 2: "))

c = float(input("ingrese lado 3: "))

# Operación

# Resultados

opeTriangulo(a, b, c)

print("Muchas Gracias, programa terminado.")
