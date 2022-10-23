""

# Ejercicio 4

# Ingreso de Datos

lista_codigo = ["101", "102", "103"]

co = input("Ingrese el codigo del producto: ")

if co in lista_codigo:

    un = int(input("Ingrese las cantidad en unidades de producto comprado: "))

    # Operación

    if un > 0:

        if co == "101":

            pre = 17.5

        elif co == "102":

            pre = 25

        else:

            pre = 15.5

        if un > 0 and un != -un:

            if un < 11:

                des = 0.05

            elif un < 21:

                des = 0.075

            else:

                des = 0.1
        else:

            des = 0

        imc = un * pre

        imd = imc * des

        imp = imc - imd

        # Resultados

        print("EL importe de la compra del codigo", co, "es: S/.", round(imc, 2))

        print("EL importe del descuento del codigo", co, "es: S/.", round(imd, 2))

        print("EL importe a pagar del codigo", co, "es: S/.", round(imp, 2))

    else:

        print("Ha ingresado un valor no valido para la cantidad")

else:

    print("El Codigo de producto ingresado no es valido")
