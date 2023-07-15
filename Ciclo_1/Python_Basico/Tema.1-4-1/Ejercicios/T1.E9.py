""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Ejercicio 9

print("Por favor ingrese los datos para calcular los importes")

# Ingreso de Datos

u = int(input("Ingrese la cantidad en unidades del producto: "))

# Operación

ic = u * 17.5

id = ic * 0.11

ip = ic - id

os = int(u / 12) * 5

# Resultados

print("El importe de la compra es: ", round(ic, 2))

print("El importe del descuento es: ", round(id, 2))

print("El importe a pagar es: ", round(ip, 2))

print("El obsequio correspondiente es: ", os)

print("Muchas Gracias, programa terminado.")
