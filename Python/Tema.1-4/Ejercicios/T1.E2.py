
""

#!/usr/bin/env python

# -*- coding: utf-8 -*-

#Ejercicio 2

# Ingreso de Datos

a = float(input("Ingrese el precio: "))

b = int(input("Ingrese la cantidad: "))

c = float(input("Ingrese el porcentaje de descuento: "))

# Operación

n1 = a * b

n2 = (c/100) * n1

n3 = n1 - n2

# Resultados

print("El importe de la compra es: ", n1)

print("El importe del descuento es: ", n2)

print("El importe a pagar es: ", n3)

print("Muchas Gracias, programa terminado.")
