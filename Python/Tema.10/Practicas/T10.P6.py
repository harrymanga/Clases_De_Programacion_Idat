#Ejercicio 6 - b
def opeTriangulo(a,b,c):
   p = (a + b + c)/2
   area = (p*(p-a)*(p-b)*(p-c))**0.5
   print("el área es:",round(area,2),"\nel perímetro es",2*p)
   
#Programa Principal
a = float(input("ingrese lado 1: "))
b = float(input("ingrese lado 2: "))
c = float(input("ingrese lado 3: "))
opeTriangulo(a,b,c)
print("Programa terminado")

#************************
#PROBLEMA 6
def operaciones(a,b):
    print('El área del rectángulo es: ', a * b)
    print('El perímetro del rectángulo es: ', 2 * (a + b))
#Programa Principal 
L1 = float(input('Ingrese el primer lado: '))
L2 = float(input('Ingrese el segundo lado: '))
operaciones(L1,L2)

#*****************
def perimetro(a, b):
    return 2 * (a + b)

def area(a, b):
    return a * b

#Programa Principal 
base = float(input('Ingrese la medida de la base: '))
altura = float(input('Ingrese la medida de la altura: '))
print('Perímetro:', perimetro(base, altura))
print('Área:', area(base, altura))



