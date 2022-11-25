""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 7

print("Ingrese 1 si desea calcular el área de un triángulo")

print("Ingrese un número diferente a 1 si desea calcular el área de un círculo")

# Ingreso de datos

n = int(input("Ingrese el número de la operación que desee hacer: "))

# Operación

import math

if n == 1:

    print("Ingrese los datos del triángulo")

    b = float(input("Ingrese la medida de la base del triángulo: "))

    h = float(input("Ingrese la medida de la altura del triángulo: "))

    at = (b * h) / 2

    res = "El área del triángulo es: " + str(round(at, 2))

else:

    print("Ingrese los datos del círculo")

    r = float(input("Ingrese la medida del radio del círculo: "))

    ac = math.pi * (r**2)

    res = "El área del triángulo es: " + str(round(ac, 2))

# Resultado

print(res)

print("Muchas Gracias, programa terminado.")
