""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 4

print("Ingrese los datos necesarios")

# Ingreso de Datos

# Operación

lista = []

from random import randint

for i in range(50):

    n = randint(1, 10)

    lista.append(n)

# Resultados

print("Números generados:", lista)

print("Nº\tRepeticiones")

for i in range(1, 10):

    print(i, " -->   ", lista.count(i))

print("Muchas Gracias, programa terminado.")
