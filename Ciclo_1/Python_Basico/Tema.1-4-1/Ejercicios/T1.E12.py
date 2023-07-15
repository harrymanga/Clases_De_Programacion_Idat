""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Ejercicio 12

print("Por favor ingrese los datos para calcular los precios de los productos")

# Ingreso de Datos

p = float(input("Ingrese el costo de la compra de los polos: "))

g = float(input("Ingrese el costo de la compra de las gorras: "))

# Operación

ic = p + g

dp = p * 0.15

dg = g * 0.05

id = dp + dg

ip = ic - id

# Resultados

print("El importe de la compra es: ", round(ic, 2))

print("El importe del descuento es: ", round(id, 2))

print("El importe a pagar es: ", round(ip, 2))

print("Muchas Gracias, programa terminado.")
