""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Ejercicio 1

print("Ingrese los datos necesarios")

# Ingreso de Datos

a = int(input("Ingrese el número a: "))

b = int(input("Ingrese el número b: "))

# Operación

n1 = a ** b

n2 = b ** a

n3 = b ** (1/a)

n4 = a ** (1/b)

# Resultados

print("La operación a elevado a la b es: ", n1)

print("La operación b elevado a la a es: ", n2)

print("La raíz a de b es: ", n3)

print("La raíz b de a es: ", n4)

print("Muchas Gracias, programa terminado.")
