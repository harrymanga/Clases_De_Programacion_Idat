""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 10

print("Por favor ingrese los datos para calcular los importes")

# Ingreso de Datos

mtv = float(input("Ingrese el monto total vendido: "))

# Operación

cm = mtv * 0.09

sb = 300 + cm

dc = sb * 0.11

sn = sb - dc

# Resultados

print("El importe de la comisión es: ", round(cm, 2))

print("El importe del sueldo bruto es: ", round(sb, 2))

print("El importe del descuento es: ", round(dc, 2))

print("El importe del sueldo neto es: ", round(sn, 2))

print("Muchas Gracias, programa terminado.")
