""

# Ejercicio 13


def vocales(n):

    v = ["a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú", "ü"]
    contV = 0

    lista = n

    list(lista)

    for i in v:

        a = lista.count(i)

        contV += a

    return contV


def consonantes(n):

    return len(n) - vocales(n)


def pedirDatos():

    lista = []

    for i in range(1, 6):

        n = input(str(i) + ".- Ingrese un nombre: ").lower()

        lista.append(n)

    return lista


def mayorCV(x):

    lista = []

    listaMCV = []

    for valor in x:

        cV = vocales(valor)

        lista.append(cV)

    for i in range(len(lista)):

        if lista[i] == max(lista):

            listaMCV.append(x[i])

    return listaMCV


def mayorCC(x):

    lista = []

    listaMCC = []

    for valor in x:

        cV = consonantes(valor)

        lista.append(cV)

    for i in range(len(lista)):

        if lista[i] == max(lista):

            listaMCC.append(x[i])

    return listaMCC


# programa principal

listaN = pedirDatos()

listaNMCV = mayorCV(listaN)

listaNMCC = mayorCC(listaN)

print("El nombre con más vocales es: ", listaNMCV)

print("El nombre con más consonantes es: ", listaNMCC)

# Resultados
