""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 9

print("Ingrese los datos necesarios")

# Ingreso de datos

n = int(input("Ingrese la cantidad de términos: "))

m = int(input("Ingrese el valor de la multiplicidad: "))


# Operación

cTer = n

c = 1

s = 0

while c <= cTer:

    t = c * m

    print(str(c) + ".-", t)

    s += t

    c += 1


# Resultados

print("La suma de los números es: ", s)

print("El promedio de los números es: ", round(s / cTer, 2))

print("Muchas Gracias, programa terminado.")
