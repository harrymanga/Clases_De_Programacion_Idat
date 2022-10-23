
#solución 1
n = int(input("Ingrese la cantidad de términos: "))
s = 0
for i in range(1, n+1):
    a = (i * 3 - 2)
    b = (i * 2)
    c = a / b
    s = s + c
    print(str(a)+"/"+str(b))
print('Suma:', round(s,2))

#solución 2
from fractions import Fraction
i = 1
suma = 0
for j in range(2, 201, 2):
    k = Fraction(i, j)
    print(k)
    suma += k
    i += 3
print('Suma:', Fraction(suma))

#solución 3
n = int(input("Ingrese la cantidad de términos: "))
suma = 0
a = 1
b = 2
for i in range(1, n+1):
    print(str(a)+"/"+str(b))
    suma += a / b
    a += 3
    b += 2
print('Suma:', round(suma,2))








