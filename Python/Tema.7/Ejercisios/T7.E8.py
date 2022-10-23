""

# Ejercicio 8

# Ingreso de Datos


# Operación

cTer = 10

c = 1

s = 0

while c <= cTer:

    t = c * 13

    print(str(c) + ".-", t)

    s += t

    c += 1


# Resultados

print("La suma de los números es: ", s)

print("El promedio de los números es: ", round(s / cTer, 2))

print("Muchas Gracias, programa terminado.")
