""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Ejercicio 3

print("Por favor ingrese los datos del producto para calcular el total a pagar")

# Ingreso de Datos

c = float(input("Ingrese el costo unitario del producto: "))

u = int(input("Ingrese la cantidad en unidades del producto: "))

# Operación

t = c * u

# Resultados

print("El costo total a pagar es: ", round(t, 2))

print("Muchas Gracias, programa terminado.")
