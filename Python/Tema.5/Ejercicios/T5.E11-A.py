""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 11 - A

print("Ingrese los datos necesarios")

# Ingreso de datos

lista_usuario = ["Alpha", "Omega"]

lista_clave = ["enero", "diciembre"]

u = input("Ingrese su nombre de usuario: ").capitalize()

c = input("Ingrese su clave de usuario: ").lower()

# Operaciones

if u in lista_usuario and c in lista_clave:

    res = "Bienvenido usuario: " + u

else:

    res = "Nombre de usuario o clave no válido"

# Resultados

print(res)

print("Muchas Gracias, programa terminado.")
