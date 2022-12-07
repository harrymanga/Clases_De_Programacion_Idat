""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 11

print("Ingrese los datos necesarios")

# Ingreso de Datos

n = int(input("Ingrese la cantidad de notas: "))

# Operación

from random import randint

lista = []

for i in range(n):

    nota = randint(0, 20)

    lista.append(nota)

# Resultados

print("Las notas generadas son:", lista)

print("La nota promedio es:", round(sum(lista) / len(lista), 2))

print("La nota mayor es:", max(lista))

print("La nota menor es:", min(lista))

print("Muchas Gracias, programa terminado.")