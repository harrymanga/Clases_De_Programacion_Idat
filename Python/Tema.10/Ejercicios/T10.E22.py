""

#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 22

print("Ingrese los datos necesarios")

# Funciones


def sueldoBruto(a, b):

    r = a * b

    return r


def bonificación(a, b):

    r = a * b

    return r


def descuento(a):

    if 0 <= a <= 20:

        r = a * 2

    elif 21 <= a <= 50:

        r = a * 6

    elif 51 <= a <= 100:

        r = a * 10

    else:

        r = a * 15

    return r


def salario(a, b, c):

    r = a + b - c

    if r > 0:

        print(f"El salario del empleado es: S/. {r}")

    else:

        print(f"El empleado cuenta con una deuda de : S/. {r * (-1)}")


# Ingreso de Datos

while True:

    while True:

        try:

            tarifaHoraria = input("Ingrese la tarifa de horario laboral : ")

            tarifaHoraria = float(tarifaHoraria)

            if tarifaHoraria > 0:

                break

            else:

                print("Dato invalido, Ingrese la Tarifa de horario laboral")

        except ValueError:

            print("Dato invalido, Ingrese la Tarifa de horario laboral")

    while True:

        try:

            horasTrabajadas = input("Ingrese las Horas trabajadas : ")

            horasTrabajadas = int(horasTrabajadas)

            if horasTrabajadas > 0:

                break

            else:

                print("Dato invalido, Ingrese las Horas trabajadas")

        except ValueError:

            print("Dato invalido, Ingrese las Horas trabajadas")

    while True:

        try:

            horasExtras = input("Ingrese las Horas extras : ")

            horasExtras = int(horasExtras)

            if horasExtras > 0:

                break

            else:

                print("Dato invalido, Ingrese las Horas extras")

        except ValueError:

            print("Dato invalido, Ingrese las Horas extras")

    while True:

        try:

            minutosTardanza = input("Ingrese los minutos de tardanza : ")

            minutosTardanza = int(minutosTardanza)

            if minutosTardanza > 0:

                break

            else:

                print("Dato invalido, Ingrese los minutos de tardanza")

        except ValueError:
            
            print("Dato invalido, Ingrese los minutos de tardanza")

    break


# Operación

s = sueldoBruto(tarifaHoraria, horasTrabajadas)

b = bonificación(tarifaHoraria, horasExtras)

d = descuento(minutosTardanza)

# Resultado

salario(s, b, d)

print("Muchas Gracias, programa terminado.")
