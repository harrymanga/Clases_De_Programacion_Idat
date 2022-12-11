""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 10

print("Ingrese los datos necesarios")

# Ingreso de Datos

# Operación

lista = []

from random import randint

for i in range(20):

    n = randint(50, 100)

    lista.append(n)

# Resultados

print("Números generados:", lista)

print("Nº\tRepeticiones")

for i in range(50, 100):

    if lista.count(i) > 1:

        print(i, " -->   ", lista.count(i))

print("Muchas Gracias, programa terminado.")
