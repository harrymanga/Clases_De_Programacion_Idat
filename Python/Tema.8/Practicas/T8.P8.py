"""

# Ejercicio 8 - A


# Ingreso de Datos

n = int(input("Ingrese el total de números naturales pares: "))

# Operación

s = 0

for i in range(1, n + 1):

    npar = i * 2

    print("Numero ", i, ":", npar)

    s = s + npar

print("La suma de  los", n, "números pares es: ", s)

# Resultados

print("Programa terminado")"""


# Ejercicio 8 - B


# Ingreso de Datos

n = int(input("Ingrese el total de números naturales pares: "))

# Operación

s = 0

for i in range(2, 2 * n + 1, 2):

    print(i)

    s += i

print("La suma de  los", n, "números pares es: ", s)

# Resultados

print("Programa terminado")
