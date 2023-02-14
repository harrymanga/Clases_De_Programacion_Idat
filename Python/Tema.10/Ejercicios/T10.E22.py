"""


22. Crear una aplicación que permita calcular el salario de un empleado. 

El salario será igual a la suma de sueldo bruto + bonificación – descuento. ​

El sueldo bruto se calculará como tarifa horaria * horas trabajadas.​

La bonificación se calculará como tarifa horaria * horas extras.​

El descuento se aplicará según el siguiente criterio :​

Si los minutos de tardanza se encuentran de cero a 20, entonces se descontará S/2 por minuto.​

Si los minutos de tardanza se encuentran de 21 a 50, entonces se descontará S/6 por minuto.​

Si los minutos de tardanza se encuentran de 51 a 100, entonces se descontará S/10 por minuto.​

Si los minutos de tardanza son más de 100, entonces se descontará S/15 por minuto.​

​

Utilice funciones para el cálculo de salario, sueldo bruto, bonificación y descuento.
"""

#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 22

print("Ingrese los datos necesarios")

# Funciones


def sueldoBruto(a, b):

    r = a * b

    return r

# Ingreso de Datos

# Operación

# Resultado

print("Muchas Gracias, programa terminado.")
