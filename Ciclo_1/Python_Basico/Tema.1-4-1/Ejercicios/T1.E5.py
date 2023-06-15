""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 5

print("Por favor ingrese los datos para hallar la hipotenusa del triangulo rectángulo")

# Ingreso de Datos

import math

a = float(input("Ingrese la medida del cateto a: "))

b = float(input("Ingrese la medida del cateto b: "))

# Operación

h = math.sqrt((a**2) + (b**2))

# Resultados

print("La hipotenusa es: ", round(h, 2))

print("Muchas Gracias, programa terminado.")
