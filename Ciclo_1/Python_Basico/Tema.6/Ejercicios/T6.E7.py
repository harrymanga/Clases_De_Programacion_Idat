""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 7

print(
    "Si desea hallar el área del Rectángulo ingrese 1 \nSi desea hallar el área del Trapecio ingrese 2 \nSi desea hallar el área del Pentágono ingrese 3"
)

# Ingreso de Datos

co = int(input("Ingrese el número de la operación que desee hacer: "))

# Operación

if co == 1:

    print("Ingrese los datos del Rectángulo")

    b = float(input("Ingrese la medida de la base del Rectángulo: "))

    h = float(input("Ingrese la medida de la altura del Rectángulo: "))

    a = b * h

    res = "El área del Rectángulo es: " + str(a)

elif co == 2:

    print("Ingrese los datos del Trapecio")

    b1 = float(input("Ingrese la medida de la base mayor del Trapecio: "))

    b2 = float(input("Ingrese la medida de la base menor del Trapecio: "))

    h = float(input("Ingrese la medida de la altura del Trapecio: "))

    a = h * (b1 + b2) / 2

    res = "El área del Trapecio es: " + str(a)

elif co == 3:

    print("Ingrese los datos del Pentágono")

    pr = float(input("Ingrese la medida del perímetro del Pentágono: "))

    ap = float(input("Ingrese la medida del apotema del Pentágono: "))

    a = (pr * ap) / 2

    res = "El área del Pentágono es: " + str(a)

else:

    res = "Numero de operación no es valido"

# Resultado

print(res)

print("Muchas Gracias, programa terminado.")
