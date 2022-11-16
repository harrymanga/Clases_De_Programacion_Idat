""

# Ejercicio 10


def contV(n):

    v = ["a", "e", "i", "o", "u"]

    contV = 0

    lista = list(n)

    for i in v:

        a = lista.count(i)

        contV += a

    return contV


# Programa Principal

nombre = input("Ingrese su nombre: ").lower()

print("El número de vocales es: ", contV(nombre))

# ********************


def vocalCont(nom):

    cont = 0

    lista = list(nom)

    for i in "aeiou":

        a = lista.count(i)

        cont += a

    print('"' + nom + '"' + " tiene " + str(cont) + " vocales.")


# Programa Principal

nom = input("ingrese una palabra o frase: ").lower()

vocalCont(nom)
