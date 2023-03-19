""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 1

print("Ingrese los datos necesarios")

# Funciones

# Ingreso de Datos

print("Ingrese los Nombres y Apellidos de 5 alumnos")

alumnos = {}

for i in range(1):

    while True:

        print(f"Ingrese los datos del alumno {i + 1}")

        while True:

            nombre = input(f"Ingrese el Nombre del {i + 1} alumno : ").capitalize()

            if nombre.isalpha():

                break

            else:

                print("Dato Invalido, Ingrese un Nombre correcto")

        while True:

            apellido = input(f"Ingrese el Apellido del {i + 1} alumno : ").capitalize()

            if apellido.isalpha():

                break

            else:

                print("Dato Invalido, Ingrese un Apellido correcto")

        alumnos[nombre] = apellido

        break

# Operación

while True:

    buscar = input(f"Ingrese el Nombre del alumno que desea buscar : ").capitalize()

    if buscar.isalpha():

        break

    else:

        print("Dato Invalido, Ingrese un Nombre de búsqueda correcto")

if buscar in alumnos.keys():

    print(f"El alumno {buscar} {alumnos.get(buscar)} si esta registrado")

else:

    print(f"El nombre ingresado no esta registrado")

# Resultados

print("Muchas Gracias, programa terminado.")
