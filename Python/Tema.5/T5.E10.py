""

# Ejercicio 10

print("Ingrese los datos necesarios")

# Ingreso de datos

lista = ["Juan", "Pedro", "Pablo", "Antonio"]

n = input("Ingrese su nombre de usuario: ").capitalize()

# Operaciones

if n in lista:

    res = "Bienvenido usuario: " + n

else:

    res = "Nombre de usuario no válido"

# Resultados

print(res)
