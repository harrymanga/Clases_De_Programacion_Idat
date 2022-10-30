""

# Ejercicio 5

from random import randint

# ingreso de datos

lista = []

for i in range(100):

    n = randint(30, 100)

    lista.append(n)

# operación

par = 0

for n in lista:

    if n % 2 == 0:

        par += 1

impar = len(lista) - par

# resultados

print("Números generados:", lista)

print("La cantidad de números pares es: ", par)

print("La cantidad de números impares es: ", impar)

print("Programa terminado")
