""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Ejercicio 9

print("Ingrese los datos necesarios")

# Ingreso de datos

print("Ingrese M o F según su sexo")

n = input("Ingrese su respuesta según su sexo: ").upper()

# Operaciones

if n != str("M") and n != str("F"):

    res = "Usted ha ingresado una respuesta inválida"

elif n == str("M"):

    res = "Bienvenido Caballero"

else:

    res = "Bienvenida Señorita"

# Resultados

print(res)

print("Muchas Gracias, programa terminado.")
