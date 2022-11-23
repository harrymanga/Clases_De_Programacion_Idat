""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 5

# Ingreso de Datos

import math

a = float(input("Ingrese la medida de la arista del icosaedro : "))

# Operación

a1 = 5 * (math.sqrt(3)) * (a**2)

v = (5 * (3 + math.sqrt(5)) * (a**3)) / 12

# Resultados

print("El Área del icosaedro es : ", round(a1, 2))

print("El Volumen del icosaedro es : ", round(v, 2))

print("Muchas Gracias, programa terminado.")
