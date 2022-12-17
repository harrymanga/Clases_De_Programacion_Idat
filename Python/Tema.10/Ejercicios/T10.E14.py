""


def numeroInt(msg):

    msg1 = input(msg)

    while True:

        try:

            msg1 = int(msg1)

            break

        except:

            msg1 = input("Dato no valido, Ingrese nuevamente el numero de ventas : ")

    return msg1


ventas = numeroInt("Ingrese el numero de ventas a registrar : ")

print(ventas)
