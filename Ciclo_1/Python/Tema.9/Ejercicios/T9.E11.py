""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 11

print("Ingrese los datos necesarios")

# Ingreso de Datos

lista = []

for i in range(10):

    while True:

        num = input(
            "Ingrese 10 números enteros en el rango de 10 a 50 , N°"
            + str(i + 1)
            + " : "
        )

        if num.isalpha() or num == "" or int(num) < 10 or int(num) > 50:

            print(
                "Error dato incorrecto, ingrese un numero entero en el rango de 10 a 50"
            )

        else:

            break

    lista.append(int(num))

# Operación

# Resultados

print("Los números ingresados son :")

for i in lista:

    res = i

    print(res, end=" ")

print()

print("Muchas Gracias, programa terminado.")
