""
# !/usr/bin/env python
# -*- coding: utf-8 -*-

# Realizar un programa que tenga 1 función que permita dividir dos números enteros, a su vez deberá pedir dichos números enteros, el programa debe tener manejo de excepciones.

def division():
    
    while True:
        
        try:
            
            num1 = int(input("Ingrese el primer numero para su division : "))
        
        except ValueError:
            
            print("Dato invalido, Ingrese un numero entero")
        
        else:
            
            break
        
    while True:
        
        try:
            
            num2 = int(input("Ingrese el segundo numero para su division : "))
            
        except ValueError:
            
            print("Dato invalido, Ingrese un numero entero")
        
        else:
            
            if num2 == 0:
                
                print("Dato invalido, El segundo numero deve ser diferente de cero")
            
            else:
                
                break
    
    dev = num1 / num2
    
    return dev

print("Programa para devidir 2 numeros enteros\n")

print(f"El resultado de la deivision es : {division()}") 

print("Programa terminado")  
