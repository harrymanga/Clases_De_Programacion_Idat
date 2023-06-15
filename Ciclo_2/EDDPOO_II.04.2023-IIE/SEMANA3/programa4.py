""
# !/usr/bin/env python
# -*- coding: utf-8 -*-

#  Elabore un programa que pida una cadena por teclado que representa una frase (palabras separadas por espacios), finalmente que cuente cuantas palabras tiene.

cadena = input("Por favor ingrese una frase : ")

palabras = cadena.split()

print(f"La Frase Cuenta con {len(palabras)} Palabras")

    