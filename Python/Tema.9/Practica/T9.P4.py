""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 4

print("Ingrese los datos necesarios")

# Ingreso de Datos

# Operación

lista = []

c = 0

while True:

    n = int(input(str(c + 1) + ".- Ingrese un numero: "))

    if n == 0:

        break

    lista.append(n)

    c += 1

# Resultados

print("Números Ingresados:", lista)

print("Tamaño de la lista:", c)

print("Muchas Gracias, programa terminado.")
