#PROBLEMA 5
def condicion(n):
    if n > 0 and n < 18:
        r = 'Usted es menor de edad'
    elif n >= 18:
        r = 'Usted es mayor de edad'
    else:
        r = 'Valor de edad no válido'
    print(r)

#programa principal
edad = int(input('Ingrese su edad: '))
condicion(edad)

#*************

def edad(e):
    if e < 0:
        return "Error edad no válida"
    elif 0 <= e < 18:
        return "Es menor de edad"
    else:
        return "Es mayor de edad"
# Ingreso de Datos
ed = int(input("Ingrese su edad: "))
# Operación

# Resultados
print(edad(ed))
print("Programa terminado")

#***************

def edad(n):
    if n > 18:
        print('Mayor de edad')
    elif n > 0:
        print('Menor de edad')
    else:
        print('Dato no correcto')
numero = int(input('1.-Ingrese la edad:'))
edad(numero)






