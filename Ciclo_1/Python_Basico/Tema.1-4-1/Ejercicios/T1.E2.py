""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Ejercicio 2

print("Por favor ingrese los datos para calcular el Área de un trapecio")

# Ingreso de Datos

B = float(input("Ingrese la medida de la base mayor del trapecio: "))

b = float(input("Ingrese la medida de la base menor del trapecio: "))

h = float(input("Ingrese la medida de la altura del trapecio: "))

# Operación

a = ((B + b) * h) / 2

# Resultados

print("El Área del trapecio es: ", round(a, 2))

print("Muchas Gracias, programa terminado.")
