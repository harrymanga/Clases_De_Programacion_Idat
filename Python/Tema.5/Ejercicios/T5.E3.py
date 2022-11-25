""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 3

print("Ingrese las notas del alumno")

# Ingreso de datos

lista = []

for i in range(3):

    nota = int(input("Ingrese la nota " + str(i + 1) + ": "))

    lista.append(nota)

# Operación

p = round(sum(lista) / len(lista), 2)

if p >= 13:

    r = "El alumno a APROBÓ el curso"

else:

    r = "El alumno a DESAPROBÓ el curso"

# Resultado

print(r)

print("Muchas Gracias, programa terminado.")
