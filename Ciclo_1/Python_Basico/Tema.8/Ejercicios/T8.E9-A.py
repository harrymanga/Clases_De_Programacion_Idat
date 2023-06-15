""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 9 - A

print("Ingrese los datos necesarios")

# Ingreso de Datos

# Operación

j = 2

k = 3

s1 = 0

for i in range(1, 101):

    s1 += (j / k)

    print(str(i) + ".-", j, "/", k)

    j += 3

    k += 2

# Resultados

print("La suma es:", round(s1 , 2))

print("Muchas Gracias, programa terminado.")