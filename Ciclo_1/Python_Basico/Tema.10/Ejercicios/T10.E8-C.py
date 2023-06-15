""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 8 - C

print("Ingrese los datos necesarios")

# Funciones


def tabla(n):

    for i in range(1, 13):

        print(str(i) + ".-", str(n), "x", str(i), ":", n * i)


# Ingreso de Datos

num = int(input("Ingresa un número entero positivo: "))

# Operación

# Resultados

tabla(num)

print("Muchas Gracias, programa terminado.")
