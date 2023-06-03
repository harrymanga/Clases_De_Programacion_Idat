""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 6 - E

print("Ingrese los datos necesarios")

# Ingreso de Datos

n1 = int(input('Ingrese un número: '))

n2 = int(input('Ingrese otro número: '))

# Operación

while n1 >= n2:

    n1 = int(input('Ingrese un número: '))

    n2 = int(input('Ingrese otro diferente y mayor: '))

else:

    for i in range(n1, n2+1):

        if i % 2 != 0:

            print(i)

# Resultados

print("Muchas Gracias, programa terminado.")