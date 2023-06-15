""
# !/usr/bin/env python
# -*- coding: utf-8 -*-

# Elabore un programa que pida una cadena y un carácter por teclado (valida que sea un carácter) y muestra cuantas veces aparece el carácter en la cadena.


cadena = input("Por favor ingrese una cadena : ").lower()

# FORMA 1

while True:
    
    caracter = input("Ingrese un caracter : ").lower()
    
    if len(caracter) == 1: break
    
# FORMA 2

#caracter = input("Ingrese un caracter : ").lower()

#while len(caracter) != 1:
    
    caracter = input("Ingrese un caracter : ").lower()
    
contar = cadena.count(caracter)

print(f"CONTEO : {contar}")
    
    