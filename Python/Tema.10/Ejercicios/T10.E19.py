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


def salarioNeto(a):

    for c, v in a.items():

        neto = v[0] + v[1] - v[2]

        print("El sueldo neto a pagar es : S/.", neto)


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

    print("Ingrese los datos del empleado N°", i + 1)

    registrarDatos()


# Resultados


print(empleado)

salarioNeto(empleado)

print("Muchas Gracias, programa terminado.")
