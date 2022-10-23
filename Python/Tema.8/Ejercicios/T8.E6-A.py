#Pida dos números y muestre todos los números impares que van
#desde el primero al segundo. Se debe controlar que los valores
#son correctos.

#solución 1
n1 = 1
n2 = 0
while n2 < n1:
    n1 = int(input('Ingrese el menor número: '))
    n2 = int(input('Ingrese el mayor número: '))
for i in range(n1, n2 + 1):
    if i % 2 != 0:
        print(i)

#solución 2
while True:
    n1 = int(input('Ingrese el menor número: '))
    n2 = int(input('Ingrese el mayor número: '))
    if n1 >= n2:
        print('El primero debe ser menor que el segundo')
    else:
        break
for i in range(n1, n2 + 1):
    if i % 2 != 0:
        print(i)

#solución 3
numero1 = int(input('Ingrese el primer numero: '))
numero2 = int(input('Ingrese el segundo numero: '))    
if numero1 < numero2:
    print(numero2,'es mayor')
    for i in range(numero1, numero2 + 1):
        if i % 2 != 0:
            print(i)    
elif numero2 < numero1:
    print(numero1,'Es mayor')
    for i in range(numero2, numero1 + 1):
        if i % 2 != 0:
            print(i)
else:
    print(numero1)

#solución 4
n1 = int(input('Ingrese un número: '))
n2 = int(input('Ingrese otro número: '))
while n1 >= n2:
    n1 = int(input('Ingrese un número: '))
    n2 = int(input('Ingrese otro diferente y mayor: '))
else:
    for i in range (n1, n2+1):
        if i % 2 != 0:
            print(i)





















    
