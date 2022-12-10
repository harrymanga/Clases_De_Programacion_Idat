""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 6

print("Ingrese los datos necesarios")

# Ingreso de Datos

meses = [
    "Enero",
    "Febrero",
    "Marzo",
    "Abril",
    "Mayo",
    "Junio",
    "Julio",
    "Agosto",
    "Septiembre",
    "Octubre",
    "Noviembre",
    "Diciembre",
]

numMeses = int(input("Ingrese la cantidad de meses a evaluar: "))

mesAgrup = []

for i in range(numMeses):

    while True:

        mes = input("Ingrese el mes: ").capitalize()

        if mes not in meses:

            print("ERROR ingrese un dato valido")

        else:

            break

    ventas = float(input("Ingrese el monto de la venta del mes: "))

    mesAgrup.append((mes, ventas))


print("Ingreso terminado\n")

# Operación

montos = []

for i in range(len(mesAgrup)):

    montos.append(mesAgrup[i][1])

for i in range(len(mesAgrup)):

    print(i + 1, ".-", mesAgrup[i][0], mesAgrup[i][1])

pos = 0

for maxVenta in range(1, len(mesAgrup)):

    if mesAgrup[maxVenta][1] > mesAgrup[pos][1]:

        pos = maxVenta

print()

# Resultados

print("El monto de la venta máxima es: S/.", mesAgrup[pos][1])

print("El mes con la máxima venta es: ", mesAgrup[pos][0])

print("El monto total de las ventas es: S/.", sum(montos))

print(
    "El monto promedio de las ventas es: S/.", round((sum(montos) / len(mesAgrup)), 2)
)

print("Muchas Gracias, programa terminado.")
