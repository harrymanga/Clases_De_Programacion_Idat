""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 11 - B

print("Ingrese los datos necesarios")

# Ingreso de datos

u = input("Ingrese su nombre de usuario: ").capitalize()

c = input("Ingrese su clave de usuario: ").lower()

# Operaciones

if u == "Alpha" and c == "enero":

    res = "Bienvenido usuario: " + u

elif u == "Omega" and c == "diciembre":

    res = "Bienvenido usuario: " + u

else:

    res = "Nombre de usuario o clave no válido"

# Resultados

print(res)

print("Muchas Gracias, programa terminado.")
