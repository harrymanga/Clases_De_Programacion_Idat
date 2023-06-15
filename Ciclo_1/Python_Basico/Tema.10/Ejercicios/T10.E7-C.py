""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 7 - C

print("Ingrese los datos necesarios")

# Funciones


def condición(a, b):

    t = a * b

    d = t * 0.2

    r = t - (t * 0.2)

    if t > 50:

        print("El total a pagar es sin descuento:", t)

        print("El descuento es:", d)

        print("El total de la compra con descuenta es:", r)

    else:

        print("El total a pagar es:", t)


# Ingreso de Datos

cant = int(input("Ingresa la cantidad de productos: "))

costo = float(input("Ingresa el precio del producto: "))

# Operación

# Resultados

condición(cant, costo)

print("Muchas Gracias, programa terminado.")
