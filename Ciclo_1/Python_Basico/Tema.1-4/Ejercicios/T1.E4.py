""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Ejercicio 4

print("Ingrese los datos necesarios")

# Ingreso de Datos

s = float(input("Ingrese el Sueldo: "))

m = float(input("Ingrese los minutos de tardanza: "))

d = float(input("Ingrese los días de inasistencia: "))

# Operación

dt = m * 1.5

dd = d * 34

pnt = s - (dt + dd)

# Resultados

print("El monto de descuento por minutos de tardanza es: ", dt)

print("El monto de descuento por dia de inasistencia es: ", dd)

print("El pago neto es: ", pnt)

print("Muchas Gracias, programa terminado.")
