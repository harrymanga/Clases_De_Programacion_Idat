""

# Ejercicio 2

print("Ingreso de datos")

# Ingreso de Datos


def datosDic(n):

    dic = {}

    for i in range(n):

        print("Persona", i + 1, "\n**********")

        key = int(input("Ingrese el número de su documento: "))

        name = input("Ingrese su nombre: ")

        dic[key] = name

    return dic


def listado(d):

    print("Personas registradas")

    for c, v in d.items():

        print(c, " --> ", v)


def buscar(d, x):

    nom = "El número de DNI no esta registrado"

    for c in d.keys():

        if c == x:

            nom = d[x]

    print(nom)


# Operación


# Programa principal

dic = {}

while True:

    print("Menú")

    print("1. Registrar datos")

    if len(dic) > 0:

        print("2. Lista datos")

        print("3. Buscar personas")

    opcion = int(input("Elija una opción: "))

    if opcion == 1:

        print("Diccionario #Documento - Nombre")

        num = int(input("Ingrese el numero de personas que desea registrar: "))

        dic = datosDic(num)

    elif opcion == 2:

        listado(dic)

    elif opcion == 3:

        dni = int(input("Ingrese el número del DNI: "))

        buscar(dic, dni)

    else:

        print("Opcion no valida")

    resp = input("Desea realizar otra operacion: ").lower()

    if resp != "si":

        break

# Resultados
