""
# !/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    
    print("Bloque try")
    
    x = int(input("Ingresa un número: "))
    
    y = int(input("Ingresa otro número: "))
    
    z = x / y
    
except ValueError:
    
    print("Bloque except ValueError")
    
    print("Solo se aceptan numeros enteros")
    
except ZeroDivisionError:
    
    print("Bloque except ZeroDivisionError")
    
    print("División por cero no aceptada.")
        
else:
    
    print("Bloque else")
    
    print("División = ", z)
    
finally:
    
    print("Bloque finally")
