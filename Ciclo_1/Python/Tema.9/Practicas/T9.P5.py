""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 5

print("Ingrese los datos necesarios")

# Ingreso de Datos

# Operación

lista = []

c = 0

while True:

    n = int(input(str(c + 1) + ".- Ingrese un numero: "))

    if n == 0:

        break

    if n % 5 == 0:

        lista.append(n)

    c += 1

# Resultados

print("Números Ingresados:", lista)

print("Muchas Gracias, programa terminado.")
