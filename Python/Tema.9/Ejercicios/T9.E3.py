""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 3

print("Ingrese los datos necesarios")

# Ingreso de Datos

vocales = ["a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú", "ü"]

while True:
    nom = input("Ingrese su nombre: ").lower()

    if nom.isalpha():

        break

    else:

        print("Ingrese solo letras")

# Operación

cantV = 0

for letra in nom:

    if letra in vocales:

        cantV += 1

cantL = len(nom)

cantC = cantL - cantV

# Resultados

print("La cantidad de letras es:", cantL)

print("La cantidad de vocales es:", cantV)

print("La cantidad de consonantes es:", cantC)

print("Muchas Gracias, programa terminado.")
