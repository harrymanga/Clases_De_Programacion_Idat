def numPromedio(numeros):

    return sum(numeros) / len(numeros)


def pedirNumero(msg):

    usuarioNum = input(msg)

    continuar = False

    while continuar == False:

        try:

            usuarioNum = int(usuarioNum)

            continuar = True

        except:

            usuarioNum = input("Numero no valido\nIngrese nuevamente ")

    return usuarioNum


def pedirNumeroFloat(msg):

    usuarioNum = input(msg)

    continuar = False

    while continuar == False:

        try:

            usuarioNum = float(usuarioNum)

            continuar = True

        except:

            usuarioNum = input("No valido\nIngrese nuevamente ")

    return usuarioNum


ventas = []

cantidadVentas = pedirNumero("Cantidad de ventas a registar:")

for x in range(1, cantidadVentas + 1):

    ventas.append(pedirNumeroFloat("Precio de la venta #" + str(x) + ": "))

    print(ventas)

print("El promedio de las ventas es: ", round(numPromedio(ventas), 2))
