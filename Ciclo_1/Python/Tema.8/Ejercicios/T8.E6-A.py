""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 6 - A

print("Ingrese los datos necesarios")

# Ingreso de Datos

while True:

    n1 = int(input("Ingrese el número menor del intervalo : "))

    n2 = int(input("Ingrese el número mayor del intervalo : "))

    if n1 >= n2:

        print("Intervalo no admitido")

    else:

        break

# Operación

c = 0

for i in range(n1, n2 + 1):

    if i % 2 != 0:

        c += 1

        print(str(c) + ".-", i)

# Resultados

print("Muchas Gracias, programa terminado.")