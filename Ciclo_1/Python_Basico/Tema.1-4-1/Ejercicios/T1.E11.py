""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Ejercicio 11

print("Por favor ingrese los datos para calcular el precio de venta de la pieza")

# Ingreso de Datos

pc = float(input("Ingrese el precio de compra de la pieza: "))

pr = float(input("Ingrese el porcentaje de ganancia: "))

# Operación

pg = pc * (pr / 100)

pv = pc + pg

# Resultados

print("El precio de venta es: ", round(pv, 2))

print("Muchas Gracias, programa terminado.")
