""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 9

print("Ingrese los datos necesarios")

# Funciones

print("")

operaciones = ["cuadrado", "cubo", "raiz"]


def cuadrado(a):

    return a**2


def cubo(b):

    return b**3


def raíz(c):

    return round(c**0.5, 2)


# Ingreso de Datos

while True:

    try:

        num = int(input("Ingrese un número entero positivo: "))

    except ValueError:

        print("Debes escribir un número.")

        continue

    if num < 0:

        print("Debes escribir un número positivo.")

        continue

    else:

        break

print("Seleccione una operación para realizar")

print("Si dese elevar el numero al cuadrado escriba: Cuadrado")

print("Si dese elevar el numero al cubo escriba: Cubo")

print("Si dese obtener la raíz cuadrada escriba: Raíz")

# Operación

while True:

    op = input("Que operación desea realizar: ").lower()

    if op not in operaciones:

        print("Error operación no valida")

    else:

        break

if op == "cuadrado":

    print("El numero", num, "al cuadrado es:", cuadrado(num))

elif op == "cubo":

    print("El numero", num, "al cubo es:", cubo(num))

else:

    print("La raíz cuadrada del  numero", num, "es:", raíz(num))

# Resultados

print("Muchas Gracias, programa terminado.")
