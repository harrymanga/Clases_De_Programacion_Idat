""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 13

print(
    "Por favor ingrese los datos para calcular el porcentaje de estudiantes varones y mujeres"
)

# Ingreso de Datos

e = int(input("Ingrese el numero total de estudiantes: "))

v = int(input("Ingrese el numero de estudiantes varones: "))

# Operación

pv = (v / e) * 100

pm = ((e - v) / e) * 100

# Resultados

print("El porcentaje de varones es: ", pv)

print("El porcentaje de mujeres es: ", pm)

print("Muchas Gracias, programa terminado.")
