""

# Ejercicio 5

# Ingreso de Datos


# Operación

cTer = 150

c = 1

t = 3

s = 0

while c <= cTer:

    print(str(c) + ".-", t)

    s += t

    t += c

    c += 1


# Resultados

print("La suma de los números es: ", s)

print("El promedio de los números es: ", round(s / cTer, 2))

print("Muchas Gracias, programa terminado.")
