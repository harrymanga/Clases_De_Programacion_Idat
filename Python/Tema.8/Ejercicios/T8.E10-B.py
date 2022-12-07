""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 10 - B

print("Ingrese los datos necesarios")

# Ingreso de Datos

# Operación

from fractions import Fraction

i = 1

suma = 0

for j in range(2, 201, 2):

    k = Fraction(i, j)

    print(k)

    suma += k

    i += 3

# Resultados

print('Suma:', Fraction(suma))

print("Muchas Gracias, programa terminado.")