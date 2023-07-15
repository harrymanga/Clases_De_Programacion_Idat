""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Ejercicio 5

print("Si desea comprar un Smart Tv use el código P001 \nSi desea comprar una Refrigeradora use el código P002 \nSi desea comprar una Lavadora use el código P003")

# Ingreso de Datos

lista_codigo = ["P001", "P002", "P003"]

co = input("Ingrese el código del producto: ").capitalize()

# Operación

if co in lista_codigo:

    un = int(input("Ingrese las cantidad en unidades de producto comprado: "))

    if un > 0:

        if co == "P001":

            pre = 2500.00

        elif co == "P002":

            pre = 2850.00

        else:

            pre = 1520.00

        imv = un * pre

        igv = imv * 0.18

        imt = imv + igv

        print("EL importe de la venta del código", co, "es: S/.", round(imv, 2))

        print("EL importe del IGV es: S/.", round(igv, 2))

        print("EL total a pagar es: S/.", round(imt, 2))

    else:

        print("Ha ingresado un valor no valido para la cantidad")

else:

    print("El Código de producto ingresado no es valido")

# Resultados

print("Muchas Gracias, programa terminado.")
