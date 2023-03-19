""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 1

print("Ingrese los datos necesarios")

# Funciones

# Ingreso de Datos

print("Ingrese los Nombres y Apellidos de 5 alumnos")

alumnos = {}

for i in range(5):

    while True:

        print(f"Ingrese los datos del alumno {i + 1}")

        while True:

            nombre = input(f"Ingrese el Nombre del {i + 1} alumno : ").capitalize()

            if nombre.isalpha():

                break

            else:

                print("Dato Invalido, Ingrese un nombre correcto")

        while True:

            apellido = input(f"Ingrese el Apellido del {i + 1} alumno : ").capitalize()

            if apellido.isalpha():

                break

            else:

                print("Dato Invalido, Ingrese un Apellido correcto")

        alumnos[nombre] = apellido

        break


# Operación

# Resultados

print(alumnos)

print("Muchas Gracias, programa terminado.")
