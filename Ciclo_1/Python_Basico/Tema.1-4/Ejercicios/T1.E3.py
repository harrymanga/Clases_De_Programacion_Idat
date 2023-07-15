""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Ejercicio 3

print("Ingrese los datos necesarios")

# Ingreso de Datos

a = float(input("Ingrese la medida del Lado A: "))

b = float(input("Ingrese la medida del Lado B: "))

c = float(input("Ingrese la medida del Lado C: "))

# Operación

p = (a + b + c) / 2

area = (p * (p - a) * (p - b) * (p - c)) ** (1 / 2)

# Resultados

print("El area del triangulo es: ", round(area, 5))

print("Muchas Gracias, programa terminado.")
