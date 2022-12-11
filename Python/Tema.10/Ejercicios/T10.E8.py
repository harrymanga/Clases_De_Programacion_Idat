""

# Ejercicio 8


def tabla(n):

    print("Tabla de multiplicar de ", n, ":")

    for i in range(0, 13):

        p = n * i

        print(n, " x ", i, " = ", p)


# Programa Principal

numero = int(input("Ingrese un número: "))

tabla(numero)

# ****************************


def tablaMulti(n):

    mul = ""

    for i in range(1, 13):

        a = i * n

        mul = mul + str(i) + "x" + str(n) + "=" + str(a) + "\n"

    print(mul)


# Programa Principal

n = int(input("ingrese un numero para generar una tabla de multiplicar: "))

tablaMulti(n)

# ****************************


def tabla(n):

    for i in range(1, 13):

        print(str(i) + ".-", str(n), "x", str(i), ":", n * i)


# Programa Principal

num = int(input("Ingresa un número entero positivo: "))

tabla(num)
