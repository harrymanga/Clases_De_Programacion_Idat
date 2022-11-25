""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 4

print("Ingrese los datos necesarios")

# Ingreso de Datos

l = float(input("Ingrese la medida del Lado del prisma : "))

h = float(input("Ingrese la medida de La altura del prisma: "))

# Operación

v = ((3 ** (1 / 2)) * (l**2) * h) / 12

# Resultados

print("El Volumen del prisma es : ", round(v, 2))

print("Muchas Gracias, programa terminado.")
