""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 10

print("Ingrese los datos necesarios")

# Ingreso de Datos

n = int(input("Ingrese el total de tablas: "))

# Operación

for j in range(1, n + 1):

    print("\nTabla de multiplicar del", j)

    print("**************************")

    for i in range(1, 13):

        print(i, "*", j, "=", i * j)

# Resultados

print("Muchas Gracias, programa terminado.")
