""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 9 - B

print("Ingrese los datos necesarios")

# Ingreso de Datos

n = int(input("Ingrese la cantidad de términos: "))

# Operación

s = 0

for i in range(1, n + 1):

    a = i * 3 - 1

    b = i * 2 + 1

    c = a / b

    s = s + c

    print(str(a) + "/" + str(b))

# Resultados

print("Suma:", round(s, 2))

print("Muchas Gracias, programa terminado.")
