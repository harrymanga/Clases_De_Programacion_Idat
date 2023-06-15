""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 1

print("Ingrese los datos necesarios")

# Ingreso de datos

edad = int(input("Ingrese su edad: "))

# Operación

if edad < 0:

    m = "Error: no existe una edad negativa"

elif edad < 18:

    m = "es menor de edad"

else:

    m = "es mayor de edad"

# Resultados

print(m)

print("Muchas Gracias, programa terminado.")
