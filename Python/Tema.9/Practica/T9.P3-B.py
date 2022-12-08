""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 3 - B

print("Ingrese los datos necesarios")

# Ingreso de Datos

lista = []

cantidad = int(input("Ingrese la cantidad de términos de la lista: "))

# Operación

for i in range(1, cantidad + 1):

    n = int(input(str(i) + ".- Ingrese un numero: "))

    lista.append(n)

# Resultados

print("Números Ingresados:", lista)

print("Muchas Gracias, programa terminado.")
