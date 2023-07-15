""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Ejercicio 6

print("Ingrese los datos para determinar los importes")

# Ingreso de datos

pr = float(input("Ingrese el precio de los productos por unidades: "))

un = int(input("Ingrese las unidades de producto comprado: "))

# Operación

imc = pr * un

if un >= 100:

    imd = imc * 0.20


else:

    imd = imc * 0.15

imp = imc - imd

# Resultado

print("El importe de la compra es : S/.", imc)

print("El importe del descuento es : S/.", imd)

print("El importe a pagar es : S/.", imp)

print("Muchas Gracias, programa terminado.")
