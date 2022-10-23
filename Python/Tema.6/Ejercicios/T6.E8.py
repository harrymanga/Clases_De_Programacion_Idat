""

# Ejercicio 8

print("Ingrese los datos necesarios")

# Ingreso de Datos

ed = int(input("Ingrese la edad del usuario de la entrada: "))

en = int(input("Ingrese la cantidad de entradas: "))

tj = input(
    "Si desea pagar con tarjeta, ingrese el nombre de la tarjeta; de lo contrario pulse ENTER: "
).capitalize()

# Operación

if ed > 0:

    if en > 0:

        if ed >= 60:

            pre = 10

        elif 5 < ed < 60:

            pre = 18.5

        else:

            pre = 12.5

        if tj == "Cgt":

            des = 0.15

        else:

            des = 0

        mtc = pre * en

        mtd = mtc * des

        mtp = mtc - mtd

        # Resultados

        print("EL monto de la compra es: S/.", round(mtc, 2))

        print("EL monto del descuento por usar la tarjeta CGT es: S/.", round(mtd, 2))

        print("EL monto a pagar es: S/.", round(mtp, 2))

    else:

        print("Número de entrdas no valido")

else:

    print("Edad ingresada no valida")
