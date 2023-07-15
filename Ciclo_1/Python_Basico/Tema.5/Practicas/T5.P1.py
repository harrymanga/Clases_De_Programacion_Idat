""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Ejercicio 1

print("Ingrese los datos necesarios")

# Ingreso de datos

nota1 = int(input("Ingrese la nota 1: "))

nota2 = int(input("Ingrese la nota 2: "))

nota3 = int(input("Ingrese la nota 3: "))

# Operación

if nota3 >= 10 and nota3 < 20:

    nota3 += 2

p = round((nota1 + nota2 + nota3) / 3, 2)

# Resultado

print("Nota 3:", nota3)

print("Promedio:", p)
