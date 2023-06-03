def datosDic(n):

    dic = {}

    for i in range(n):

        print('Persona',i+1,'\n**********')

        key = int(input("Ingrese el número de su documento: "))

        name = input("Ingrese su nombre: ")

        dic[key] = name

    return dic

def listado(d):

    print('Personas registradas')

    for c,v in d.items():

        print(c,' --> ',v)

def buscar(d, x):

    for c in d.keys():

        if c == x:

            nom = d[x]
    print(nom)


#programa principal

print("Diccionario #Documento - Nombre")

num = int(input("Ingrese el numero de personas que desea registrar: "))

dic = datosDic(num)

listado(dic)

dni = int(input("Ingrese el número del DNI: "))

buscar(dic, dni)




