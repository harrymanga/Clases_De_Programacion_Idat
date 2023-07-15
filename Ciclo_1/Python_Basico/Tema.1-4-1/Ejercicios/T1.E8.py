""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Ejercicio 8

print("Por favor ingrese los datos para calcular los importes")

# Ingreso de Datos

c = float(input("Ingrese el costo unitario del producto: "))

u = int(input("Ingrese la cantidad en unidades del producto: "))

# Operación

ic = c * u

id = ic * 0.11

ip = ic - id

# Resultados

print("El importe de la compra es: ", round(ic, 2))

print("El importe del descuento es: ", round(id, 2))

print("El importe a pagar es: ", round(ip, 2))

print("Muchas Gracias, programa terminado.")
