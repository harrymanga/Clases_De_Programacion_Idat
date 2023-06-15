""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 11 - A

print("Ingrese los datos necesarios")

# Ingreso de Datos

día = [
    "Lunes",
    "Martes",
    "Miércoles",
    "Jueves",
    "Viernes",
    "Sábado",
    "Domingo",
]

nu = int(input("ingrese el numero del día de la semana: "))

# Operaciones

if nu <= 7:

    res = día[nu - 1]

else:

    res = "Valor de dado incorrecto"

# Resultado

print(res)

print("Muchas Gracias, programa terminado.")
