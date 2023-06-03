""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 6

print("Ingrese los datos necesario para realizar su compra ")

# Ingreso de Datos

pr = int(input("Ingrese el precio del producto: "))

ed = int(input("Ingrese su edad: "))

di = input("Que día es hoy: ").capitalize()

un = int(input("Cuantas unidades del producto esta comprando: "))

# Operación

if un > 0:

    if ed > 40 and di == "Viernes" and un > 5:

        des = 0.16

    elif ed > 40 and di == "Viernes":

        des = 0.12

    elif ed > 40 and un > 5:

        des = 0.09

    elif di == "Viernes" and un > 5:

        des = 0.11

    elif ed > 40:

        des = 0.05

    elif di == "Viernes":

        des = 0.07

    elif un > 5:

        des = 0.04

    else:

        des = 0

    imv = un * pr

    imd = imv * des

    imt = imv - imd

    # Resultados

    print("El importe de la venta es: S/.", round(imv, 2))

    print("El importe del descuento es: S/.", round(imd, 2))

    print("El importe a pagar es: S/.", round(imt, 2))

else:

    print("Ha ingresado un valor no valido para la cantidad")


# Datos

unid = int(input("Ingrese la unidades compradas: "))

prec = float(input("Ingrese el precio por unidad: "))

dia = input("Ingrese el día de la compra: ").title()

edad = int(input("Ingrese la edad del cliente: "))

# Descuentos:

porcD = 0

if unid > 5:

    porcD += 0.04  # descuento # 4%

if edad > 40:

    porcD += 0.05  # descuento # 5%

if dia == "Viernes":

    porcD += 0.07  # descuento # 7%

# Operaciones:

impV = unid * prec

impD = impV * porcD

impF = impV - impD

# Resultados:

print("***********************************************")

print("El importe de venta es:", impV)

print("El importe de descuento acumulado es:", round(impD, 2))

print("El importe final es:", round(impF, 2))

print("Muchas Gracias, programa terminado.")