""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 9 - D

print("Ingrese los datos necesarios")

# Ingreso de Datos

n = int(input("Ingrese la cantidad de términos: "))

# Operación

suma = 0

a = 2

b = 3

for i in range(1, n + 1):

    print(str(a) + "/" + str(b))

    suma += a / b

    a += 3

    b += 2

# Resultados

print("Suma:", round(suma, 2))

print("Muchas Gracias, programa terminado.")