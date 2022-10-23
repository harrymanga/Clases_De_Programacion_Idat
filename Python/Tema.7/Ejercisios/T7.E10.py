""

# Ejercicio 10

# Ingreso de Datos


# Operación

cTer = 5

c = 1

s = 0

while c <= cTer:

    es = float(input(str(c) + ".- Ingrese la estatura: "))

    s += es

    c += 1


# Resultados

print("La suma de las estaturas es: ", s)

print("El promedio de las estaturas es: ", round(s / cTer, 2))

print("Muchas Gracias, programa terminado.")
