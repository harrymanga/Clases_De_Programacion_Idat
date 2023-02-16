""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 1

print("Ingrese los datos necesarios")

# Funciones

# Ingreso de Datos

dicc1 = {"101": "Juan", "102": "Pedro", "103": "Pablo"}

dicc2 = {

    "101": ["Juan", 2500, "SMP"],
    "102": ["Pedro", 3500, "LOL"],
    "103": ["Pablo", 3000, "VES"],
}

# Operación

print(dicc1)

print(dicc2)

print(dicc1["102"])

print(dicc2["102"])

print(dicc2.keys())

for clave in dicc2.keys():

    print(clave, "--->", dicc2[clave])

print(dicc2.items())

for clave, valor in dicc2.items():

    print(clave, "--->", valor)

print(dicc2.values())

for valor in dicc2.values():

    print(valor)

print(dicc1)

dicc1["101"] = "Juan Perez"

print(dicc1)

dicc1["104"] = "Maria Barriga Grande"

print(dicc1)

# Resultados

print("Muchas Gracias, programa terminado.")