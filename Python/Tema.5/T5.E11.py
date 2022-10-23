"""

# Ejercicio 11

print("Ingrese los datos necesarios")

# Ingreso de datos

lista_usuario = ["Alpha", "Omega"]

lista_clave = ["enero", "diciembre"]

u = input("Ingrese su nombre de usuario: ").capitalize()

c = input("Ingrese su clave de usuario: ").lower()

# Operaciones

if u in lista_usuario and c in lista_clave:

    res = "Bienvenido usuario: " + u

else:

    res = "Nombre de usuario o clave no válido"

# Resultados

print(res)"""


# Ejercicio 11

print("Ingrese los datos necesarios")

# Ingreso de datos

u = input("Ingrese su nombre de usuario: ").capitalize()

c = input("Ingrese su clave de usuario: ").lower()

# Operaciones

if u == "Alpha" and c == "enero":

    res = "Bienvenido usuario: " + u

elif u == "Omega" and c == "diciembre":

    res = "Bienvenido usuario: " + u

else:

    res = "Nombre de usuario o clave no válido"

# Resultados

print(res)
