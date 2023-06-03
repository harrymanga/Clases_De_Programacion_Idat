""
# !/usr/bin/env python
# -*- coding: utf-8 -*-

# Realizar un programa que simule tirar dos dados y luego muestre los valores que aparecieron. Si la suma de dichos números es igual a 9 mostrar un mensaje de “Has ganado” sino mostrar “Has perdido”.

from random import randint

print("Empieza el juego de dados!!!")

while True:
    
    dado1 = randint(1, 6)

    dado2 = randint(1, 6)

    suma = dado1 + dado2

    if suma == 9:
    
        mensaje = "HAS GANADO ...!!!"
    
    else:
    
        mensaje = "HAS PERDIDO ...!!!"
    
    print(f"El primer dado es : {dado1}")
    
    print(f"El segundo dado es : {dado2}")

    print(f"La suma de dados es : {suma}")

    print(mensaje)
    
    rep = input("¿Desea realizar otra tirada? Escriba si o no : ").capitalize()
    
    if rep == "No":
        
        print("Gracias por jugar")
        
        break  