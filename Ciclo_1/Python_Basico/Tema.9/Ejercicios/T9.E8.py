""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 8

print("Ingrese los datos necesarios")

# Ingreso de Datos

lista = []

for i in range(5):

    while True:

        num = input("Ingrese la nota N°" + str(i + 1) + " : ")

        if num.isalpha() or num == "" or int(num) < 0 or int(num) > 20:

            print("Error dato incorrecto, ingrese una nota de 0 a 20")

        else:

            break

    lista.append(int(num))

# Operación

if lista[4] < 20:

    lista[4] += 2

    if lista[4] >= 20:

        lista[4] = 20

lista.remove(lista[0])

prom = sum(lista) / len(lista)

# Resultados

print("El promedio de las notas es :", round(prom, 2))

print("Muchas Gracias, programa terminado.")
