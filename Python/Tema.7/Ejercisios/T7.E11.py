"""

# Ejercicio 11 - A

# Ingreso de Datos


# Operación

c = 1

s = 0

n = -1

while n != 0:

    n = int(input(str(c) + ".- Ingrese un numero: "))

    if n % 2 == 0:

        s += n

    c += 1


# Resultados

print("La suma de las estaturas es: ", s)

print("Muchas Gracias, programa terminado.")


# Ejercicio 11 - B

# Ingreso de Datos


# Operación

c = 1

s = 0

n = int(input(str(c) + ".- Ingrese un numero: "))

while n != 0:

    if n % 2 == 0:

        s += n

    c += 1

    n = int(input(str(c) + ".- Ingrese un numero: "))

# Resultados

print("La suma de las estaturas es: ", s)

print("Muchas Gracias, programa terminado.")"""


# Ejercicio 11 - C

# Ingreso de Datos


# Operación

c = 1

s = 0

while True:

    n = int(input(str(c) + ".- Ingrese un numero: "))

    if n % 2 == 0:

        s += n

    if n == 0:

        break

    c += 1


# Resultados

print("La suma de las estaturas es: ", s)

print("Muchas Gracias, programa terminado.")
