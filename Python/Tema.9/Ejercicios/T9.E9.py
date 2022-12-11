""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 9

print("Ingrese los datos necesarios")

# Ingreso de datos

lista = ["Juan", "Pedro", "Pablo", "Antonio", "Lucas"]

while True:

    nom = input("Ingrese el nombre del cliente: ").capitalize()

    if nom.isdigit() or nom == "":

        print("Error dato incorrecto, ingrese un Nombre")

    else:

        break

while True:

    can = input("Ingrese la cantidad en unidades de producto: ")

    if can.isalpha() or can == "" or int(can) < 0:

        print("Error dato incorrecto, ingrese la cantidad de producto comprado")

    else:

        break

while True:

    pres = input("Ingrese el precio del producto: ")

    if pres.isalpha() or pres == "" or float(pres) < 0:

        print("Error dato incorrecto, ingrese el precio del producto")

    else:

        break

# Operaciones

impoCompra = int(can) * float(pres)

if nom in lista:

    impoDescue = impoCompra * 0.15

else:

    impoDescue = 0

imporPagar = impoCompra - impoDescue

# Resultados

print("El importe de la compra es: S/.", round(impoCompra, 2))

print("Los clientes que cuentan con descuento de 15%", "son : ", lista)

print("El importe del descuento es: S/.", round(impoDescue, 2))

print("El importe a pagar es: S/.", round(imporPagar, 2))

print("Muchas Gracias, programa terminado.")
