""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 8 - B

print("Ingrese los datos necesarios")

# Ingreso de Datos

n = int(input("Ingrese el total de números naturales pares: "))

# Operación

s = 0

for i in range(2, 2 * n + 1, 2):

    print(i)

    s += i

# Resultados

print("La suma de  los", n, "números pares es: ", s)

print("Muchas Gracias, programa terminado.")
