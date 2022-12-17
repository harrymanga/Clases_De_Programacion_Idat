""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 8 - B

print("Ingrese los datos necesarios")

# Funciones


def tablaMulti(n):

    mul = ""

    for i in range(1, 13):

        a = i * n

        mul = mul + str(i) + "x" + str(n) + "=" + str(a) + "\n"

    print(mul)


# Ingreso de Datos

n = int(input("ingrese un numero para generar una tabla de multiplicar: "))

# Operación

# Resultados

tablaMulti(n)

print("Muchas Gracias, programa terminado.")
