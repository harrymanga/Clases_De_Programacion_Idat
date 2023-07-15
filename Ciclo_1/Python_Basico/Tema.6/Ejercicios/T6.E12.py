""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Ejercicio 12

print("Ingrese los datos necesarios")

# Ingreso de datos

a = float(input("ingrese la medida del lado A: "))

b = float(input("ingrese la medida del lado B: "))

c = float(input("ingrese la medida del lado C: "))

# Operaciones

if a < (b + c) and a > (b - c):

    pass

if a == b and a == c:

    res = "El triangulo es equilátero"

elif a == b and a != c:

    res = "El triangulo es isósceles"

else:

    res = 3

# Resultado

print(res)

print("Muchas Gracias, programa terminado.")