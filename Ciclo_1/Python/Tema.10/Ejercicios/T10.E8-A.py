""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 8 - A

print("Ingrese los datos necesarios")

# Funciones


def tabla(n):

    print("Tabla de multiplicar de ", n, ":")

    for i in range(0, 13):

        p = n * i

        print(n, " x ", i, " = ", p)


# Ingreso de Datos

numero = int(input("Ingrese el numero de la tabla de multiplicar que desee: "))

# Operación

# Resultados

tabla(numero)

print("Muchas Gracias, programa terminado.")
