""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 3

print("Ingrese los datos necesarios")

# Ingreso de datos

vocal = ["a", "e", "i", "o", "u"]

v = input("Ingrese una vocal: ").lower()

# Operación

while v not in vocal:

    v = input("Ingrese una vocal: ").lower()

# Resultados

print("Muchas Gracias, programa terminado.")
