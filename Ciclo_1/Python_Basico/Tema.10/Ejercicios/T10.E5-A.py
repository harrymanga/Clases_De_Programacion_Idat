""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 5 - A

print("Ingrese los datos necesarios")

# Funciones


def edad(e):

    if e < 0:

        return "Error edad no valida"

    elif 0 <= e < 18:

        return "Es menor de edad"

    else:

        return "Es mayor de edad"


# Ingreso de Datos

ed = int(input("Ingrese su edad: "))

# Operación

# Resultados

print(edad(ed))

print("Muchas Gracias, programa terminado.")
