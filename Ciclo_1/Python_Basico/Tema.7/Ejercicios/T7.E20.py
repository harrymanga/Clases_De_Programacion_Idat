""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 20

print("Ingrese los datos necesarios")

# Ingreso de datos

while True:

    while True:

        nom = input("Ingrese un Nombre: ").capitalize()

        if nom.isdigit() or nom == "":

            print("Error ingrese solo letras")

        else:

            break

    print("Hola", nom, "como estas")

    while True:

        men = input(
            "¿Desea ingresar otro Nombre? , para continuar ingrese Si, si desea terminar ingrese No: "
        ).lower()

        if men.isdigit() or men == "":

            print("Error ingrese Si o No")

        else:

            break

    if men != "si":

        break

# Operación


# Resultados

print("Muchas Gracias, programa terminado.")
