""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Ejercicio 15

print("Ingrese los datos necesarios")

# Ingreso de datos

e1 = int(input("Ingrese la primera edad : "))

e2 = int(input("Ingrese la segunda edad : "))

e3 = int(input("Ingrese la tercera edad : "))

# Operaciones

if e1 == e2 == e3:

    res = "Las 3 edades son iguales"

elif e1 <= e2 and e1 <= e3:

    res = str(e1) + " Es el menor de las 3 edades"

elif e2 <= e1 and e2 <= e3:

    res = str(e2) + " Es el menor de las 3 edades"

else:

    res = str(e3) + " Es el menor de las 3 edades"

# Resultados

print(res)

print("Muchas Gracias, programa terminado.")
