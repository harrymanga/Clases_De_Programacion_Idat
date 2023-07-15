""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Ejercicio 7

print("Por favor ingrese los datos para calcular el monto por persona")

# Ingreso de Datos

mt = float(input("Ingrese el monto total a repartir: "))

e1 = int(input("Ingrese la edad de la primera persona: "))

e2 = int(input("Ingrese la edad de la segunda persona: "))

e3 = int(input("Ingrese la edad de la tercera persona: "))

# Operación

m1 = (e1 * mt) / (e1 + e2 + e3)

m2 = (e2 * mt) / (e1 + e2 + e3)

m3 = (e3 * mt) / (e1 + e2 + e3)

# Resultados

print("El Monto que recibe la primera persona es: ", round(m1, 2))

print("El Monto que recibe la segunda persona es: ", round(m2, 2))

print("El Monto que recibe la tercera persona es: ", round(m3, 2))

print("Muchas Gracias, programa terminado.")
