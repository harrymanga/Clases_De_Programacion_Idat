""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Ejercicio 14

print("Ingrese los datos necesarios")

# Ingreso de datos

ea = int(input("Ingrese los goles anotados por el equipo A : "))

eb = int(input("Ingrese los goles anotados por el equipo B : "))

# Operaciones

if ea == eb:

    res = "Los equipos empataron el partido"

elif ea > eb:

    res = "El equipo A fue el ganador del partido"

else:

    res = "El equipo B fue el ganador del partido"

# Resultados

print(res)

print("Muchas Gracias, programa terminado.")
