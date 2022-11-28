""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 19

print("Ingrese los datos necesarios")

# Ingreso de datos

# Operación

from random import randint

print("N°\tNúmero generado")

i = 0

c = 0

lista = {}

while True:

    nr = randint(10, 99)

    i += 1

    print(i, "\t", nr)

    if nr % 13 == 0:

        lista[str(i)] = str(nr)

        c += 1

    if c == 3:

        break

# Resultados

print()

print("N°\tMúltiplo de 13")

for c, v in lista.items():

    print(c, "\t", v)

print("Muchas Gracias, programa terminado.")
