""

# Ejercicio 11

from random import randint

n = int(input("Ingrese la cantidad de notas: "))

lista = []

for i in range(n):

    nota = randint(0, 20)

    lista.append(nota)

print("Las notas generadas son:", lista)

print("La nota promedio es:", round(sum(lista) / len(lista), 2))

print("La nota mayor es:", max(lista))

print("La nota menor es:", min(lista))
