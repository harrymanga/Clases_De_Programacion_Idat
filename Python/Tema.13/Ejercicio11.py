def pedirNombre():
    while True:
        n = input('Ingrese el nombre del alumno: ').upper()
        validacion1 = n.isalpha()
        if validacion1 == True:
            break
        else:
            print('Ingresar solo letras')
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
            print('Debe ingresar un valor positivo')
    return n

def registroDatos():
    d = {}
    print('\nRegistro de Empleados')
    cant = int(input('Ingrese la cantidad de empleados: '))
    for i in range(cant):
        nombre = pedirNombre()
        sB = pedirNumero('Ingrese el sueldo básico: ', 2)
        pHE = pedirNumero('Ingrese el pago por horas extras: ', 2)
        hE = pedirNumero('Ingrese las horas extras: ', 2)
        inas = pedirNumero('Ingrese la cantidad de inasistencias: ', 1)
        nH = pedirNumero('Ingrese la cantidad de hijos: ', 1)
        cod = nombre[0] + str(i + 1)
        d[cod] = [nombre, sB, pHE, hE, inas, nH]
        
    for c, v in d.items():
        desc = 0.01 * v[1] * (v[4] // 2)
        boni = 0.005 * v[1] * v[5]
        sN = v[1] + v[2] * v[3] - desc + boni
        v.append(desc)
        v.append(boni)
        v.append(sN)
        d[c] = v

    return d

def reporte(d):
    print('\nEmpleados Registrados')
    print('Código\tNombre\tSueldo Básico\tPago HE\tHE\tInasis\tHijos\tDesct\tBonif\tNeto')
    for c, v in d.items():
        print(c,'\t',v[0],'\t',v[1],'\t',v[2],'\t',v[3],'\t',v[4],'\t',v[5],'\t',v[6],'\t',v[7], '\t',v[8])

#programa principal
dic = {}
while True:
    print('Menú')
    print('1. Registrar datos')
    if len(dic) > 0:
        print('2. Ver reporte')
    opcion = int(input('Elija opción: '))
    if opcion == 1:
        dic = registroDatos()
    elif opcion == 2 and len(dic) > 0:
        reporte(dic)
    else:
        print('Opción no válida')
    resp = input('Desea realizar otra operación?: ')
    if resp != 'si':
        break
