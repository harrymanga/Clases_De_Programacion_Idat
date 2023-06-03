""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 7 - D

print("Ingrese los datos necesarios")

# Funciones


def impC(p, c):

    return p * c


def impD(p, c):

    d = 0

    if c > 50:

        d = 0.2 * impC(p, c)

    return d


def impP(p, c):

    return impC(p, c) - impD(p, c)


# Ingreso de Datos

precio = float(input("Ingrese el precio del producto: "))

cantidad = int(input("Ingrese la cantidad: "))

# Operación

# Resultados

print("Importe de la compra:", impC(precio, cantidad))

print("Importe del descuento:", impD(precio, cantidad))

print("Importe a pagar:", impP(precio, cantidad))

print("Muchas Gracias, programa terminado.")
