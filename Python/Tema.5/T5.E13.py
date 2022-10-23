""
# Ejercicio 13

print("Ingrese los datos necesarios")

# Ingreso de datos

n1 = float(input("Ingrese la primera nota : "))

n2 = float(input("Ingrese la segunda nota : "))

n3 = float(input("Ingrese la tercera nota : "))

# Operaciones

if 0 <= n1 <= 20 and 0 <= n2 <= 20 and 0 <= n3 <= 20:

    if n3 >= 10:

        n3 += 2

    if n3 > 20:

        n3 = 20

    prom = round((n1 + n2 + n3) / 3, 2)

    # Resultados

    print("El promedio final del alumno es: ", prom)

else:

    print("Datos Incorrectos")
