""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 4 - B

print("Ingrese los datos necesarios")

print("**************************************")

print("Selecciones el código de su producto: ")

print("Producto 1 código:(101)....costo(17.5)")

print("Producto 2 código:(102)....costo(25.0)")

print("Producto 3 código:(103)....costo(15.5)")

print("**************************************")

# Ingreso de datos

cod = float(input("Ingrese el código de su producto: "))

uni = float(input("Ingrese las unidades a comprar: "))

# Operaciones

if 10 >= uni >= 1:

    des = 0.05

elif 20 >= uni > 10:

    des = 0.075

else:

    des = 0.1

if cod == 101:

    pag = uni * (1 - des) * 17.5

    i = 1

elif cod == 102:

    pag = uni * (1 - des) * 25

    i = 1

elif cod == 103:

    pag = uni * (1 - des) * 15.5

    i = 1

else:

    i = 0

# Resultados

if i == 1:

    print("**************************************")

    desT = des * 100

    res = "Ud tiene un descuento del: " + str(round(desT, 2)) + " %\ny un importe total de: " + str(round(pag, 2))

else:

    res = "Código inexistente"

# Resultados

print(res)

print("Muchas Gracias, programa terminado.")