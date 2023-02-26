""


def pedirNombre():

    while True:

        n = input("Ingrese el nombre del Producto :").upper()

        validacion1 = n.isalpha()

        if validacion1 == True:

            break

        else:

            print("Ingresar solo letras")

    return n


def registroDatos():

    d = {}

    print("\nRegistro de Productos")

    for i in range(5):

        nombre = pedirNombre()

        precio = float(input("Ingrese el precio: "))

        stock = int(input("Ingrese el stock: "))

        cod = nombre[0] + str(i + 1)

        d[cod] = [nombre, precio, stock]

    return d


def listado(d):

    print("\nProductos Registrados")

    print("Nombre\tCosto de inventario")

    for v in d.values():

        print(v[0], "\t", v[1] * v[2])


def mayorP(d):

    mayor = 0

    for valor in d.values():

        if valor[1] > mayor:

            p = valor

            mayor = valor[1]

    print("Producto con mayor precio: ", p)


# programa principal

dic = {}

while True:

    print("Menú")

    print("1. Registrar datos")

    if len(dic) > 0:

        print("2. Listar datos")

        print("3. Producto con mayor precio")

    opcion = int(input("Elija opción: "))

    if opcion == 1:

        dic = registroDatos()

    elif opcion == 2:

        listado(dic)

    elif opcion == 3:

        mayorP(dic)

    else:

        print("Opción no válida")

    resp = input("Desea realizar otra operación?: ").lower()

    if resp != "si":

        break
