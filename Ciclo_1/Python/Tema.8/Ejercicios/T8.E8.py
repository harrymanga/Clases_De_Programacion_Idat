""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 8

print("Ingrese los datos necesarios")

# Ingreso de Datos

# Operación

c = 0

s = 0

for i in range(1, 51):

    c += 1

    i *= 2

    s += i

    print(str(c) + ".-", i)

# Resultados

print("La suma es:", s)

print("Muchas Gracias, programa terminado.")