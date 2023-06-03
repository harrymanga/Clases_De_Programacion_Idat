""
# !/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    
    a = 5

    b = 0

    print(a / b)

except TypeError:
    
    print("Operación no soportada...!!!")
    
except ZeroDivisionError:
    
    print("Division por cero no esta definida...!!!")