""

# Ejercicio 10

from random import randint


def numeros(a, b):

    if a == b:

        r = "GANÓ! Los números " + str(a) + " y " + str(b) + " son iguales"

    else:

        r = "PERDIÓ! Los números " + str(a) + " y " + str(b) + " no son iguales"

    return r


while True:

    n1 = int(input("Ingrese un número de 1 a 6: "))

    if n1 >= 1 and n1 <= 6:

        break

n2 = randint(1, 6)

print(numeros(n1, n2))
