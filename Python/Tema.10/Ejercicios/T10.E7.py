""

# Problema 07
def pagoTotal(a, b):
    pagoTotal = a * b
    if a > 50:
        pagoTotal *= 0.8
    print("El monto total a pagar es:", pagoTotal)


# Programa Principal
a = float(input("ingrese las unidades a comprar: "))
b = float(input("ingrese el costo por unidad: "))
pagoTotal(a, b)

# ***************************************************
# PROBLEMA 7
def operaciones(p, c):
    totalP = p * c
    if c > 50:
        impD = 0.2 * (totalP)
        impC = totalP - impD
    else:
        impD = 0
        impC = totalP
    print("El importe de la compra es: ", totalP)
    print("El importe de descuento es: ", impD)
    print("El importe a pagar es: ", impC)


# programa principal
precio = float(input("Ingrese el precio del producto: "))
cantidad = int(input("Ingrese la cantidad: "))
operaciones(precio, cantidad)

# ********************************


def condicion(a, b):
    t = a * b
    d = t * 0.2
    r = t - (t * 0.2)
    if t > 50:
        print("El total a pagar es sin descuento:", t)
        print("El descuento es:", d)
        print("El total de la compra con descuenta es:", r)
    else:
        print("El total a pagar es:", t)


# PP
cant = int(input("Ingresa la cantidad de productos: "))
costo = float(input("Ingresa el precio del producto: "))
condicion(cant, costo)

# ***********************************
def impC(p, c):
    return p * c


def impD(p, c):
    d = 0
    if c > 50:
        d = 0.2 * impC(p, c)
    return d


def impP(p, c):
    return impC(p, c) - impD(p, c)


# programa principal
precio = float(input("Ingrese el precio del producto: "))
cantidad = int(input("Ingrese la cantidad: "))
print("Importe de la compra:", impC(precio, cantidad))
print("Importe del descuento:", impD(precio, cantidad))
print("Importe a pagar:", impP(precio, cantidad))
