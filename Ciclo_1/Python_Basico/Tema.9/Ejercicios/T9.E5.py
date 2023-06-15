""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 5

print("Ingrese los datos necesarios")

# Ingreso de Datos

# Operación

lista = []

from random import randint

for i in range(100):

    n = randint(30, 100)

    lista.append(n)

par = 0

for n in lista:

    if n % 2 == 0:

        par += 1

impar = len(lista) - par

# Resultados

print("Números generados:", lista)

print("La cantidad de números pares es: ", par)

print("La cantidad de números impares es: ", impar)

print("Muchas Gracias, programa terminado.")
