""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 8 - A

print("Ingrese los datos necesarios")

# Ingreso de Datos

n = int(input("Ingrese el total de números naturales pares: "))

# Operación

s = 0

for i in range(1, n + 1):

    npar = i * 2

    print("Numero ", i, ":", npar)

    s = s + npar

# Resultados

print("La suma de  los", n, "números pares es: ", s)

print("Muchas Gracias, programa terminado.")
