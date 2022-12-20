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

            salario = input("Ingrese el monto del salario básico del empleado : ")

            if salario.isalpha() or 0 < float(salario) or salario != "":

                salario = float(salario)

                break

            else:

                print("Dato invalido, Ingrese el salario del empleado")

        while True:

            bonificación = input("Ingrese el monto de la bonificación del empleado : ")

            if bonificación.isalpha() or 0 < float(bonificación):

                bonificación = float(bonificación)

                break

            else:

                print("Dato invalido, Ingrese la bonificación del empleado")

        while True:

            descuento = input("Ingrese el monto del descuento del empleado : ")

            if descuento.isalpha() or 0 < float(descuento):

                descuento = float(descuento)

                break

            else:

                print("Dato invalido, Ingrese el descuento del empleado")

        empleado[nombre] = salario, bonificación, descuento

        break

def salarioNeto(a):
	
	for c,v in a.items():
		
		neto = v[0] + v[1] - v[2]
		
		print("El sueldo neto a pagar es : S/." ,neto)

# Ingreso de Datos

while True:
	
	numEmpleados = input("Ingrese el numero de empleados a registrar : ")

	if numEmpleados.isdigit() or 0 < int(numEmpleados) or numEmpleados != str(""):
		
		numEmpleados = int(numEmpleados)
		
		break
		
	else:
		
		print("Dato invalido, Ingrese la bonificación del empleado")


# Operación

# Resultados

registrarDatos()

print(empleado)

salarioNeto(empleado)

print("Muchas Gracias, programa terminado.")
