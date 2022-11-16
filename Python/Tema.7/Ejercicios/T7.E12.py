""

# Ejercicio 12

# Ingreso de Datos


# Operación

from random import randint

c = 1

while True:

    print("JUEGO N", c)

    while True:

        n = int(input("Ingrese un numero del 1 al 6 : "))

        if 1 <= n <= 6:

            break

        else:

            print("Debe ingrese un numero del 1 al 6")

    nr = randint(1, 6)

    print("Numero Generado", nr)

    if n == nr:

        print("GANO")

    else:

        print("PERDIO")

    while True:

        res = input("¿Desea volver a jugar (Si / No): ").capitalize()

        if res in ["Si", "No"]:

            break

        else:

            print("Respuesta incorrecta coloque Si o No")

    if res == "No":

        break

    c += 1


# Resultados

print("Muchas Gracias, programa terminado.")
