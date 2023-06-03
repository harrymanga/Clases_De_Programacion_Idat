""
# !/usr/bin/env python
# -*- coding: utf-8 -*-

from areaCuadrado import areaCuadrado

from areaRectangulo import areaRectangulo

from areaTrapecio import areaTrapecio

print("=================")

print("ÁREA DEL CUADRADO")

print("=================\n")

lado = int(input("Ingrese el lado del cuadrado : "))

print(f"El area del cuadrado es : {areaCuadrado(lado)}\n")

print("===================")

print("ÁREA DEL RECTANGULO")

print("===================\n")

lado = int(input("Ingrese el lado del rectangulo : "))

altura = int(input("Ingrese la altura del rectangulo : "))

print(f"El area del cuadrado es : {areaRectangulo(lado,altura)}\n")

print("=================")

print("ÁREA DEL TRAPECIO")

print("=================\n")

baseMenor = int(input("Ingrese la base menor del trapecio : "))

baseMayor = int(input("Ingrese la base mayor del trapecio : "))

altura = int(input("Ingrese la altura del rectangulo : "))

print(f"El area del cuadrado es : {areaTrapecio(baseMenor,baseMayor,altura)}\n")