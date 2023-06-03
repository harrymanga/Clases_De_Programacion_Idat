""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 10 - C

print("Ingrese los datos necesarios")

# Ingreso de Datos

n = int(input("Ingrese la cantidad de términos: "))

# Operación

suma = 0

a = 1

b = 2

for i in range(1, n+1):

    print(str(a)+"/"+str(b))

    suma += a / b

    a += 3

    b += 2

# Resultados

print('Suma:', round(suma,2))

print("Muchas Gracias, programa terminado.")