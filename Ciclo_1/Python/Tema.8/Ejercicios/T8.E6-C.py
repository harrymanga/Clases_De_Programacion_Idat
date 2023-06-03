""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 6 - C

print("Ingrese los datos necesarios")

# Ingreso de Datos

while True:

    n1 = int(input('Ingrese el menor número: '))

    n2 = int(input('Ingrese el mayor número: '))

    if n1 >= n2:

        print('El primero debe ser menor que el segundo')

    else:

        break

# Operación

for i in range(n1, n2 + 1):

    if i % 2 != 0:

        print(i)

# Resultados

print("Muchas Gracias, programa terminado.")