""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 7 - B

print("Ingrese los datos necesarios")

# Funciones


def operaciones(p, c):

    totalP = p * c

    if c > 50:

        impD = 0.2 * (totalP)

        impC = totalP - impD

    else:

        impD = 0

        impC = totalP

    print("El importe de la compra es: ", totalP)

    print("El importe de descuento es: ", impD)

    print("El importe a pagar es: ", impC)


# Ingreso de Datos

precio = float(input("Ingrese el precio del producto: "))

cantidad = int(input("Ingrese la cantidad: "))

# Operación

# Resultados

operaciones(precio, cantidad)

print("Muchas Gracias, programa terminado.")
