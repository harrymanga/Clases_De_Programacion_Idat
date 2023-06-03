""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 5 - B

print("Ingrese los datos necesarios")

# Funciones


def condición(n):

    if n > 0 and n < 18:

        r = "Usted es menor de edad"

    elif n >= 18:

        r = "Usted es mayor de edad"

    else:

        r = "Valor de edad no válido"

    print(r)


# Ingreso de Datos

edad = int(input("Ingrese su edad: "))

# Operación

# Resultados

condición(edad)

print("Muchas Gracias, programa terminado.")
