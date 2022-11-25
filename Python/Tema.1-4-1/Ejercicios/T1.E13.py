""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 13

print("Por favor ingrese los datos para calcular el sueldo del trabajador")

# Ingreso de Datos

h = float(input("Ingrese las horas trabajadas: "))

p = float(input("Ingrese el pago por hora trabajada: "))

# Operación

sb = h * p

dpe = sb * 0.09

dpa = sb * 0.125

dt = dpe + dpa

sn = sb - dt

# Resultados

print("El sueldo bruto es: ", round(sb, 2))

print("El descuento por ESSALUD es: ", round(dpe, 2))

print("El descuento por AFP es: ", round(dpa, 2))

print("El sueldo neto es: ", round(sn, 2))

print("Muchas Gracias, programa terminado.")
