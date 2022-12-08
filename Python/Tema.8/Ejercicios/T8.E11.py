""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 11

print("Ingrese los datos necesarios")

# Ingreso de Datos

# Operación

from random import randint

lista = []

for i in range(45):

    nota = randint(0, 20)

    print("La nota Nª", i + 1, "es", nota)

    lista.append(nota)

prom = sum(lista) / len(lista)

notaMax = max(lista)

notaMin = min(lista)

# Resultados

print("El promedio de las notas es:", round(prom, 2))

print("La nota maxima es:", notaMax)

print("La nota minima es:", notaMin)

print("Muchas Gracias, programa terminado.")
