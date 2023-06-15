""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 10 - B

print("Ingrese los datos necesarios")

# Funciones


def vocalCont(nom):

    cont = 0

    lista = list(nom)

    for i in "aeiou":

        a = lista.count(i)

        cont += a

    print('"' + nom + '"' + " tiene " + str(cont) + " vocales.")


# Ingreso de Datos

nom = input("ingrese una palabra o frase: ").lower()

# Operación

# Resultados

vocalCont(nom)

print("Muchas Gracias, programa terminado.")
