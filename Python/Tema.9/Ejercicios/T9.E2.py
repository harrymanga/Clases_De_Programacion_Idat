""

# Ejercicio 2

from random import randint

# ingreso de datos

lista = []

for i in range(50):

    n = randint(10, 100)

    lista.append(n)

# operación

mayor = max(lista)

menor = min(lista)

indMayor = []

indMenor = []

for i in range(50):

    if lista[i] == mayor:

        indMayor.append(i)

    if lista[i] == menor:

        indMenor.append(i)

# resultados

print("Numeros generados:", lista)

print("Numero mayor:", mayor, "\tIndice", indMayor)

print("Numero menor:", menor, "\tIndice", indMenor)

print("Programa terminado")
