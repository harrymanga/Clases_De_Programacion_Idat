""
# !/usr/bin/env python
# -*- coding: utf-8 -*-


# Definiendo funciones 

def suma(a ,b):

    return a + b

def resta(a ,b):

    return a - b
    
def multiplicacion(a ,b):

    return a * b    

def division(a ,b):

    try:
        
        a / b
    
    except ZeroDivisionError:
        
        print("No se puede dividir entre 0...!!!")
        
        return "Operacion erronea...!!!"
    
# Pedimos los valores

while True:
    
    try:
        
        num1 = int(input("Ingrese el primer numero : "))
        
        num2 = int(input("Ingrese el segundo numero : ")) 
        
        break

    except ValueError:
        
        print("Los valores ingresados son incorrectos...!!!")
        
        print("Intentelo nuevamente...!!!")        

# Efectuando las opéraciones

operacion = input("Ingrese la operacion a realizar : \n- SUMA\n- RESTA\n- MULTIPLICACION\n- DIVISION\n\n").upper()

if operacion == "SUMA":
    
    print(f"SUMA: {suma(num1, num2)}")
 
elif operacion == "RESTA":
    
    print(f"RESTA: {resta(num1, num2)}")
 
elif operacion == "MULTIPLICACIÓN":
    
    print(f"MULTIPLICACIÓN: {multiplicacion(num1, num2)}")
   
elif operacion == "DIVISIÓN":
    
    print(f"DIVISIÓN: {division(num1, num2)}")
 
else:
    
    print("Operación no contemplada...!!!")
 
print("Gracias por usar el programa...!!!")
