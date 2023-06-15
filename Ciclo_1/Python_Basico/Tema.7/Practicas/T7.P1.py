""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 1

print("Ingrese los datos necesarios")

# Ingreso de datos

n = int(input("Ingrese un numero menor a 20: "))

# Operación

while n > 20:

    n = int(
        input("El numero ingresado no es menor que 20, ingrese un numero menor a 20: ")
    )

# Resultados

print("Muchas Gracias, programa terminado.")
