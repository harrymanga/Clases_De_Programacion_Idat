""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 21

print("Ingrese los datos necesarios")

# Ingreso de datos

# Operación

c = 1

s = 0

while True:

    n = int(input(str(c) + ".- Ingrese un número: "))

    s += n

    if n == 0:

        break

    c += 1

# Resultados

print("La suma de los número ingresados es: ", s)

print("Muchas Gracias, programa terminado.")
