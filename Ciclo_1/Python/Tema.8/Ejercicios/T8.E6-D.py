""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 6 - D

print("Ingrese los datos necesarios")

# Ingreso de Datos

numero1 = int(input('Ingrese el primer numero: '))

numero2 = int(input('Ingrese el segundo numero: '))

# Operación

if numero1 < numero2:

    print(numero2,'es mayor')

    for i in range(numero1, numero2 + 1):

        if i % 2 != 0:

            print(i)

elif numero2 < numero1:

    print(numero1,'Es mayor')

    for i in range(numero2, numero1 + 1):

        if i % 2 != 0:

            print(i)

else:

    print(numero1)

# Resultados

print("Muchas Gracias, programa terminado.")