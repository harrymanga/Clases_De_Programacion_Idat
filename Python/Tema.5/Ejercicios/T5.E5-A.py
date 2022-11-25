""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 5 - A

print("Ingrese los números para determinar cuál es el mayor")

# Ingreso de datos

n1 = int(input("Ingrese el primer número: "))

n2 = int(input("Ingrese el segundo número: "))

# Operación

if n1 == n2:

    print("Los números", n1, "y", n2, "son iguales")

elif n1 > n2:

    r1 = n1

    r2 = n2

else:

    r1 = n2

    r2 = n1

# Resultado

print("El número", r1, "es el mayor")

print("El número", r2, "es el menor")

print("Muchas Gracias, programa terminado.")
