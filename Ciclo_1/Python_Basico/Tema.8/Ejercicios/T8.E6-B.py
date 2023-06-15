""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 6 - B

print("Ingrese los datos necesarios")

# Ingreso de Datos

n1 = 1

n2 = 0

while n2 < n1:

    n1 = int(input('Ingrese el menor número: '))

    n2 = int(input('Ingrese el mayor número: '))

for i in range(n1, n2 + 1):

    if i % 2 != 0:

        print(i)

# Operación

# Resultados

print("Muchas Gracias, programa terminado.")