""
# !/usr/bin/env python
# -*- coding: utf-8 -*-

#Elabore un algoritmo que compruebe si una cadena leída por teclado comienza por una subcadena introducida por teclado.

cadena = input("Por favor ingrese una cadena : ").lower()

subcadena = input("Por favor ingrese una subcadena: ").lower()

if cadena.startswith(subcadena):
    
    print("La cadena SI COMIENZA por la subcadena...!!!")

else:
    
    print("La cadena NO COMIENZA por la subcadena...!!!")