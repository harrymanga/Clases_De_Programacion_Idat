""

# Ejercicio 4

from random import randint

# ingreso de datos

lista = []

for i in range(50):

    n = randint(1, 10)

    lista.append(n)

# operación

# resultados

print("Numeros generados:", lista)

print("Nº\tRepeticiones")

for i in range(1, 10):

    print(i, " -->   ", lista.count(i))

print("Programa terminado")
