""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 9

print("Ingrese los datos necesarios")

# Ingreso de Datos

n = int(input("Ingrese el valor de N: "))

# Operación

f = 1

if n < 0:

    res = "No existe factorial de números negativos"

else:

    for i in range(1, n + 1):

        f *= i

    res = "El factorial de " + str(n) + " = " + str(f)

# Resultados

print(res)

print("Muchas Gracias, programa terminado.")
