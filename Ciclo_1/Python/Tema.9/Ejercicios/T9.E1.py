""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 1

print("Ingrese los datos necesarios")

# Ingreso de Datos

lista = []

for i in range(1, 11):

    while True:

        nota = int(input(str(i) + ".- Ingrese la nota: "))

        if 0 <= nota <= 20:

            lista.append(nota)

            break

        else:

            print("Ingrese una nota entre 0 y 20")

# Operación

p = sum(lista) / len(lista)

# Resultados

print("Notas Ingresadas:", lista)

print("Promedio de notas:", round(p, 2))

print("Muchas Gracias, programa terminado.")
