""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 17

print("Ingrese los datos necesarios")

# Ingreso de datos

# Operación

from random import randint

print("N°\tNumero generado")

i = 0

while True:

    nr = randint(1, 6)

    i += 1

    print(i, "\t", nr)

    if nr == 6:

        break

# Resultados

print("Muchas Gracias, programa terminado.")
