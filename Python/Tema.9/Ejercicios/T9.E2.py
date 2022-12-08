""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 2

print("Ingrese los datos necesarios")

# Ingreso de Datos

# Operación

from random import randint

lista = []

for i in range(50):

    n = randint(10, 100)

    lista.append(n)

mayor = max(lista)

menor = min(lista)

indMayor = []

indMenor = []

for i in range(50):

    if lista[i] == mayor:

        indMayor.append(i)

    if lista[i] == menor:

        indMenor.append(i)

# Resultados

print("Numeros generados:", lista)

print("Numero mayor:", mayor, "\tIndice", indMayor)

print("Numero menor:", menor, "\tIndice", indMenor)

print("Muchas Gracias, programa terminado.")
