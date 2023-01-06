""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 19

print("Ingrese los datos necesarios")

# Funciones

empleado = {}


def registrarDatos():

    while True:

        while True:

            nombre = input("Ingresar el nombre del empleado : ").capitalize()

            if nombre.isalpha():

                break

            else:

                print("Dato invalido, Ingrese el nombre del empleado")

        while True:

            try:

                salario = input("Ingrese el monto del salario básico del empleado : ")

                salario = float(salario)

                if salario > 0:

                    break

                else:

                    print("Dato invalido, Ingrese el salario del empleado")

            except ValueError:

                print("Dato invalido, Ingrese el salario del empleado")

        while True:

            try:

                bonificación = input(
                    "Ingrese el monto de la bonificación del empleado : "
                )

                bonificación = float(bonificación)

                if bonificación > 0:

                    break

                else:

                    print("Dato invalido, Ingrese la bonificación del empleado")

            except ValueError:

                print("Dato invalido, Ingrese la bonificación del empleado")

        while True:

            try:

                descuento = input("Ingrese el monto del descuento del empleado : ")

                descuento = float(descuento)

                if descuento > 0:

                    break

                else:

                    print("Dato invalido, Ingrese el descuento del empleado")

            except ValueError:

                print("Dato invalido, Ingrese el descuento del empleado")

        empleado[nombre] = salario, bonificación, descuento

        break


# Ingreso de Datos

while True:

    try:

        numEmpleados = input("Ingrese el numero de empleados a registrar : ")

        numEmpleados = int(numEmpleados)

        if numEmpleados > 0:

            break

        else:

            print("Dato invalido, Ingrese el numero de empleados a registrar")

    except ValueError:

        print("Dato invalido, Ingrese el numero de empleados a registrar")

# Operación

for i in range(numEmpleados):

    print(f"Ingrese los datos del empleado N° {i+1}")

    registrarDatos()

sueldosNetos = {}


def salarioNeto(a):

    print("Sueldos a Pagar")

    for c1, v1 in a.items():

        neto = v1[0] + v1[1] - v1[2]

        print(f"El sueldo neto a pagar del empleado {c1} es : S/. {neto}")

        sueldosNetos[c1] = neto


def empleadoMayorSueldo(b):

    mayor = 0

    for c2, v2 in b.items():

        if mayor < v2:

            mayor = v2

    for c2, v2 in b.items():

        if mayor == v2:

            print(f"EL empleado con mayor sueldo neto es : {c2}")


# Resultado

salarioNeto(empleado)

empleadoMayorSueldo(sueldosNetos)

print("Muchas Gracias, programa terminado.")
