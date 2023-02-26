""


def pedirNombre():

    while True:

        n = input("Ingrese el nombre del inquilino: ").upper()

        validacion1 = n.isalpha()

        if validacion1 == True:

            break

        else:

            print("Ingresar solo letras")
            
    return n


def pedirNumero(m, opcion):
    while True:
        if opcion == 1:
            n = int(input(m))
        else:
            n = float(input(m))
        if n >= 0:
            break
        else:
            print("Debe ingresar un valor positivo")
    return n


def registroDatos():
    d = {}
    print("\nRegistro de Inquilinos")
    cant = int(input("Ingrese la cantidad de inquilinos: "))
    for i in range(cant):
        nombre = pedirNombre()
        mAlq = pedirNumero("Ingrese el monto del alquiler: ", 2)
        cAgu = pedirNumero("Ingrese el monto por consumo de agua: ", 2)
        cElec = pedirNumero("Ingrese el por consumo de electricidad: ", 2)
        cGas = pedirNumero("Ingrese el monto por consumo de gas: ", 2)
        cod = nombre[0] + str(i + 1)
        d[cod] = [nombre, mAlq, cAgu, cElec, cGas]

    for c, v in d.items():
        toPagar = v[1] + v[2] + v[3] + v[4]
        v.append(toPagar)
        d[c] = v
    return d


def reporte(d):
    print("\nInquilinos Registrados")
    print(
        "Código\tNombre\tSueldo Básico\tPago HE\tHE\tInasis\tHijos\tDesct\tBonif\tNeto"
    )
    for c, v in d.items():
        print(
            c,
            "\t",
            v[0],
            "\t",
            v[1],
            "\t",
            v[2],
            "\t",
            v[3],
            "\t",
            v[4],
            "\t",
            v[5],
            "\t",
        )


# programa principal
dic = {}
while True:
    print("Menú")
    print("1. Registrar Inquilino")
    if len(dic) > 0:
        print("2. Ver reporte")
    opcion = int(input("Elija opción: "))
    if opcion == 1:
        dic = registroDatos()
    elif opcion == 2 and len(dic) > 0:
        reporte(dic)
    else:
        print("Opción no válida")
    resp = input("Desea realizar otra operación?: ")
    if resp != "si":
        break
