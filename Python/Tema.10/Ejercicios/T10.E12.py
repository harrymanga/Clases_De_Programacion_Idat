""

# Ejercicio 12


def mayor(lista):

    mayor = max(lista)

    return "El numero mayor es: " + str(mayor)


def menor(lista):

    menor = min(lista)

    return "El numero menor es: " + str(menor)


def suma(lista):

    suma = sum(lista)

    return "La suma de los números es: " + str(suma)


def prom(lista):

    pro = round(sum(lista) / len(lista), 2)

    return "El promedio es: " + str(pro)


# Programa Principal

print("Ingrese cuatro numeros")

lista = []

for i in range(4):

    a = int(input("ingrese un numero: "))

    lista.append(a)

# Resultados


print(mayor(lista))

print(menor(lista))

print(suma(lista))

print(prom(lista))
