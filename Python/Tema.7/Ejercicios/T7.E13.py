""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 13

print("Ingrese los datos necesarios")

# Ingreso de datos

productos = {}

c = 1

s = 0

while True:

    print("Ingrese el producto N°:", c)

    c += 1

    while True:

        pr = input("Ingrese el precio del producto: ")

        if pr.isalpha() or pr == "":

            print("Dato ingresado incorrecto, ingrese solo precios de los productos")

        else:

            break

    while True:

        ct = input("Ingrese la cantidad de en unidades del producto: ")

        if ct.isalpha() or ct == "":

            print(
                "Dato ingresado incorrecto, ingrese la cantidad de los productos en números"
            )

        else:

            break

    while True:

        men = input(
            "¿Desea registrar otro producto? , para continuar ingrese Si, si desea terminar ingrese No: "
        ).lower()

        if men.isdigit() or men == "":

            print("Error ingrese Si o No")

        else:

            break

    productos[c - 1] = [pr, ct]

    mt1 = float(pr) * int(ct)

    s += mt1

    if men != "si":

        break

# Operación

print("N°\tPrecio\tCantidad\tTotal")

for c, v in productos.items():

    print(c, "\t", v[0], "\t", v[1], "\t      S/.", float(v[0]) * int(v[1]))

# Resultados

print("El monto total a pagar es: S/.", s)

print("Muchas Gracias, programa terminado.")
