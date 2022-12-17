""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 10 - A

print("Ingrese los datos necesarios")

# Funciones


def contV(n):

    v = ["a", "e", "i", "o", "u"]

    contV = 0

    lista = list(n)

    for i in v:

        a = lista.count(i)

        contV += a

    return contV


# Ingreso de Datos

nombre = input("Ingrese su nombre: ").lower()

# Operación

# Resultados

print("El número de vocales es: ", contV(nombre))

print("Muchas Gracias, programa terminado.")
