""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 21

print("Ingrese los datos necesarios")

# Funciones

meses = {
    1: "Enero",
    2: "Febrero",
    3: "Marzo",
    4: "Abril",
    5: "Mayo",
    6: "Junio",
    7: "Julio",
    8: "Agosto",
    9: "Septiembre",
    10: "Octubre",
    11: "Noviembre",
    12: "Diciembre",
}


def nombreMes(a):

    print(f"El mes seleccionado es : {meses[a]}")


# Ingreso de Datos


while True:

    try:

        numMes = input("Ingrese el numero de mes que desea saber: ")

        numMes = int(numMes)

        if 13 > numMes > 0:

            break

        else:

            print("Dato invalido, Ingrese el numero del mes")

    except ValueError:
        
        print("Dato invalido, Ingrese el numero del mes")


# Operación

# Resultado

nombreMes(numMes)

print("Muchas Gracias, programa terminado.")
