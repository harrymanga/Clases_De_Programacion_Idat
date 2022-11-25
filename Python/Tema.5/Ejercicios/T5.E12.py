""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 12

print("Ingrese los datos necesarios")

# Ingreso de datos

d = input("Ingrese el día de su compra: ").capitalize()

p = float(input("Ingrese el precio del producto por unidad: "))

u = int(input("Ingrese la cantidad de producto comprado en unidades : "))

# Operaciones

imc = p * u

if d == "Viernes":

    imd = imc * 0.1

else:

    imd = 0

imp = imc - imd

# Resultados

print("El importe de la compra es: S/.", round(imc, 2))

print("El importe del descuento por comprar en el día ", d, "es : S/.", round(imd, 2))

print("El importe a pagar es: S/.", round(imp, 2))

print("Muchas Gracias, programa terminado.")
