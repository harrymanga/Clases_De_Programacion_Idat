""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 7

print("Ingrese los datos necesarios")

# Ingreso de Datos

while True:

    num = input("Ingrese un numero entero que este en el rango de 100 a 999 : ")

    if num.isalpha() or int(num) < 100 or int(num) > 999:

        print(
            "Error dato incorrecto, ingrese un numero entero en el rango de 100 a 999"
        )

    else:

        break

# Operación

from random import randint

lista = []

for i in range(20):

    numRan = randint(100, 999)

    lista.append(numRan)

lista1 = []

for i in lista:

    if int(num) < i:

        lista1.append(i)

# Resultados

print("Lista Completa de Números generados")

print(lista)

print("Lista Reducida de Números generados")

print(lista1)

print("Muchas Gracias, programa terminado.")
