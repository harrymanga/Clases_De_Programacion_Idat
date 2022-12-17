""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 7 - A

print("Ingrese los datos necesarios")

# Funciones


def pagoTotal(a, b):

    pagoTotal = a * b

    if a > 50:

        pagoTotal *= 0.8

    print("El monto total a pagar es:", pagoTotal)


# Ingreso de Datos

a = float(input("ingrese las unidades a comprar: "))

b = float(input("ingrese el costo por unidad: "))

# Operación

# Resultados

pagoTotal(a, b)

print("Muchas Gracias, programa terminado.")
