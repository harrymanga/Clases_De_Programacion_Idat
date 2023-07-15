""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Ejercicio 9

print("Ingrese los datos necesarios")

# Ingreso de Datos

n1 = float(input("Ingrese la nota del primera examen : "))

n2 = float(input("Ingrese la nota del segunda examen : "))

n3 = float(input("Ingrese la nota del tercera examen : "))

# Operaciones

if 0 <= n1 <= 20 and 0 <= n2 <= 20 and 0 <= n3 <= 20:

    if n1 > 14:

        n1 += 2

    if n1 > 20:

        n1 = 20

    if n2 < 13:

        n2 -= 1

    if n2 < 0:

        n2 = 0

    if n3 > 15:

        n3 += 2

    if n3 > 20:

        n3 = 20

    prom = round((n1 + n2 + n3) / 3, 2)

    if prom >= 13:

        res = "EL alumno APROBÓ con: " + str(prom)

    else:

        res = "EL alumno DESAPROBÓ con: " + str(prom)

else:

    res = "Datos Incorrectos"

# Resultado

print(res)

print("Muchas Gracias, programa terminado.")