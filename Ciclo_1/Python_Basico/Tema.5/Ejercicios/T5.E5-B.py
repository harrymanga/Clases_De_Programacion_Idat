""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 5 - B

print("Ingrese los números para determinar cuál es el mayor")

# Ingreso de datos

n1 = int(input("Ingrese el primer número: "))

n2 = int(input("Ingrese el segundo número: "))

# Operación

if n1 == n2:

    res = "Los números " + str(n1) + " y " + str(n2) + " son iguales"

elif n1 > n2:

    res = "El número " + str(n1) + " es mayor que " + str(n2)

else:

    res = "El número " + str(n2) + " es mayor que " + str(n1)

# Resultado

print(res)

print("Muchas Gracias, programa terminado.")
