""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Ejercicio 6

print("Por favor ingrese los datos para calcular el pago mensual")

# Ingreso de Datos

t = float(input("Ingrese la tarifa por hora trabajada: "))

h = float(input("Ingrese las horas trabajadas: "))

# Operación

s1 = t * h

s2 = s1 + (s1 * 0.2)

s3 = s2 - (s2 * 0.1)

# Resultados

print("El Sueldo Básico es: ", round(s1, 2))

print("El Sueldo Bruto es: ", round(s2, 2))

print("El Sueldo Neto es: ", round(s3, 2))

print("Muchas Gracias, programa terminado.")
