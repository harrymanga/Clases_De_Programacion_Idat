""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 5 - C

print("Ingrese los datos necesarios")

# Funciones


def edad(n):

    if n > 18:

        print("Mayor de edad")

    elif n > 0:

        print("Menor de edad")

    else:

        print("Dato no correcto")


# Ingreso de Datos

numero = int(input("1.-Ingrese la edad: "))

# Operación

# Resultados

edad(numero)

print("Muchas Gracias, programa terminado.")
