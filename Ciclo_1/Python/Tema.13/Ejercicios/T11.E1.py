""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 1

print("Ingrese los datos necesarios")

print("Creacion de diccionario Ingles / Español")

# Funciones


def registroDatos():

    dic = {}

    i = 1

    while True:

        print("Palabra", i, "\n**********")

        pI = input("Ingrese la palabra en inglés: ").lower()

        pC = input("Ingrese la palabra en castellano: ").lower()

        dic[pI] = pC

        i += 1

        r = input("¿Desea continuar?: ")

        if r != "si":

            break

    return dic


def listado(d):

    print("Palabras registradas")

    for c, v in d.items():

        print(c, " --> ", v)


def buscar(d, x):

    pC = "La palabra en inglés introducida no está registrada"

    for c in d.keys():

        if c == x:

            pC = d[x]

    print(pC)


# Ingreso de Datos

# Operación

dic = {}

while True:

    print("Menú")

    print("1. Registrar palabras")

    if len(dic) > 0:

        print("2. Listar palabras")

        print("3. Buscar palabra")

    opcion = int(input("Elija opción: "))

    if opcion == 1:

        print("Diccionario Inglés - Castellano")

        dic = registroDatos()

    elif opcion == 2:

        listado(dic)

    elif opcion == 3:

        pI = input("Ingrese la palabra en inglés: ").lower()

        buscar(dic, pI)

    else:

        print("Opción no válida")

    resp = input("Desea realizar otra operación?: ")

    if resp != "si":

        break

# Resultados

print("Muchas Gracias, programa terminado.")
