""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 6

print("Ingrese los datos necesarios")

# Ingreso de datos

# Operación

cTer = 50

c = 1

t = 7

s = 0

while c <= cTer:

    print(str(c) + ".-", t)

    s += t

    t += c

    c += 1


# Resultados

print("La suma de los números es: ", s)

print("El promedio de los números es: ", round(s / cTer, 2))

print("Muchas Gracias, programa terminado.")
