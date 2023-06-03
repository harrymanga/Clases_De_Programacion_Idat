""
# !/usr/bin/env python
# -*- coding: utf-8 -*-

from operaciones import suma

from operaciones import resta

from operaciones import multiplicacion

from operaciones import division

from operaciones import potencia

print("=============================")

print("CALCULAR LA SUMA DE 2 NUMEROS")

print("=============================\n")

num1 = int(input("Ingrese el primer numero : "))

num2 = int(input("Ingrese el segundo numero : "))

print(f"El valor de la suma es : {suma(num1, num2)}\n")

print("==============================")

print("CALCULAR LA RESTA DE 2 NUMEROS")

print("==============================\n")

num1 = int(input("Ingrese el primer numero : "))

num2 = int(input("Ingrese el segundo numero : "))

print(f"El valor de la resta es : {resta(num1, num2)}\n")

print("======================================")

print("CALCULAR LA MULTIPLICAION DE 2 NUMEROS")

print("======================================\n")

num1 = int(input("Ingrese el primer numero : "))

num2 = int(input("Ingrese el segundo numero : "))

print(f"El valor de la multiplicacion es : {multiplicacion(num1, num2)}\n")

print("=================================")

print("CALCULAR LA DIVISION DE 2 NUMEROS")

print("=================================\n")

num1 = int(input("Ingrese el primer numero : "))

while True:
    
    num2 = int(input("Ingrese el segundo numero : "))
    
    if num2 == 0:
        
        print("Ingrese un numero diferente de cero")
        
    else:
        
        break
    
print(f"El valor de la division es : {division(num1, num2)}\n")

print("====================")

print("CALCULAR LA POTENCIA ")

print("===================\n")

num1 = int(input("Ingrese la base de la potencia: "))

num2 = int(input("Ingrese el exponente de la potencia : "))

print(f"El valor de la potencia es : {potencia(num1, num2)}\n")