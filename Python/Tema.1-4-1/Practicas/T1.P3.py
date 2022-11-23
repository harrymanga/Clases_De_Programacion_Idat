""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 3

# Ingreso de Datos

import math

r = float(input("Ingrese el Radio : "))

# Operación

a = 4 * math.pi * (r**2)

v = (4 * math.pi * (r**3)) / 3

# Resultados

print("El Área de la Esfera es : ", round(a, 2))

print("El Volumen de la Esfera es : ", round(v, 2))

print("Muchas Gracias, programa terminado.")
