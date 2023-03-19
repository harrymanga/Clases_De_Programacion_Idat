
def pedirNombre():

    while True:

        n = input('Ingrese el nombre del alumno: ').upper()

        validacion1 = n.isalpha()

        if validacion1 == True:

            break

        else:

            print('Ingresar solo letras')

    return n

def pedirNota(m):

    while True:

        n = int(input(m))

        if 0 <= n <= 20:

            break

        else:

            print('La nota ingresada no se encuentra en el rango de [0-20]')

    return n

def registroDatos():

    d = {}

    print('\nRegistro de Alumnos')

    cant = int(input('Ingrese la cantidad de alumnos: '))

    for i in range(cant):

        nombre = pedirNombre()

        n1 = pedirNota('Ingrese la nota 1: ')

        n2 = pedirNota('Ingrese la nota 2: ')

        n3 = pedirNota('Ingrese la nota 3: ')

        n4 = pedirNota('Ingrese la nota 4: ')

        n5 = pedirNota('Ingrese la nota 5: ')

        cod = nombre[0] + str(i + 1)

        d[cod] = [nombre, n1, n2, n3, n4, n5]

    for c, v in d.items():

        p = (v[1] + v[2] + v[3] + v[4] + v[5]) / 5

        cond = 'Desaprobado'

        if p >= 13:

            cond = 'Aprobado'

        v.append(p)

        v.append(cond)

        d[c] = v
        
    return d

def listado(d):
    print('\nAlumnos Registrados')
    print('Código\tNombre\tNotas\t\t\tPromedio\tCondición')
    for c, v in d.items():
        print(c,'\t',v[0],'\t',v[1:6],'\t',v[6],'\t',v[7])

def buscar(d):
    x = input('Ingrese el código del alumno: ')
    alumno = 'El código ingresado no existe'
    for c in d.keys():
        if c == x:
            alumno = d[x]
    print(alumno)

def verEstadisticas(d):
    c = 0
    for v in d.values():
        if v[6] >= 13:
            c += 1
    print('Cantidad de aprobados:', c)
    print('Cantidad de desaprobados:', len(d) - c)

#programa principal
dic = {}
while True:
    print('Menú')
    print('1. Registrar datos')
    if len(dic) > 0:
        print('2. Listar datos')
        print('3. Buscar alumno')
        print('4. Ver estadísticas')
    opcion = int(input('Elija opción: '))
    if opcion == 1:
        dic = registroDatos()
    elif opcion == 2:
        listado(dic)
    elif opcion == 3:
        buscar(dic)
    elif opcion == 4:
        verEstadisticas(dic)
    else:
        print('Opción no válida')
    resp = input('Desea realizar otra operación?: ')
    if resp != 'si':
        break
