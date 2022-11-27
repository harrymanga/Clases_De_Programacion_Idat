""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 15

print("Ingrese los datos necesarios")

# Ingreso de datos

print("Se generara números aleatorios entre 10 y 200")

# Operación

from random import randint

print("N°\tNumero generado")

for i in range(20):

    nr = randint(10, 200)

    print(i + 1, "\t", nr)

# Resultados

print("Muchas Gracias, programa terminado.")
