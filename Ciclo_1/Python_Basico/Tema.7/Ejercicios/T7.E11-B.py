""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 11 - B

print("Ingrese los datos necesarios")

# Ingreso de datos

# Operación

c = 1

s = 0

n = int(input(str(c) + ".- Ingrese un numero: "))

while n != 0:

    if n % 2 == 0:

        s += n

    c += 1

    n = int(input(str(c) + ".- Ingrese un numero: "))

# Resultados

print("La suma de las estaturas es: ", s)

print("Muchas Gracias, programa terminado.")

