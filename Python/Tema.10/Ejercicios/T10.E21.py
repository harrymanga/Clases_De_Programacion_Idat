""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 20

print("Ingrese los datos necesarios")

# Funciones


def aprobados(a):

    aprobado = 0

    desaprobado = 0

    for i in a:

        if 13 <= i:

            aprobado += 1

        else:

            desaprobado += 1

    print(f"Hay {aprobado} alumnos APROBADOS")

    print(f"Hay {desaprobado} alumnos DESAPROBADOS")


def becas(b):

    sinExamen = 0

    mediaBeca = 0

    becaCompleta = 0

    for i in b:

        if i < 6:

            sinExamen += 1

        elif 17 <= i <= 19:

            mediaBeca += 1

        elif i == 20:

            becaCompleta += 1

    print(f"Hay {sinExamen} alumnos sin derecho a dar examen de recuperación")

    print(f"Hay {mediaBeca} alumnos que ganaron media Beca")

    print(f"Hay {becaCompleta} alumnos que ganaron Beca Completa")


# Ingreso de Datos

# Operación

from random import randint

notas = []

for i in range(50):

    nota = randint(0, 20)

    notas.append(nota)

# Resultado

aprobados(notas)

becas(notas)

print("Muchas Gracias, programa terminado.")
