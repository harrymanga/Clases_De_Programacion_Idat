""

# Problema 04
# Datos
print("**************************************")
print("Selecciones el codigo de su producto: ")
print("Producto 1 codigo:(101)....costo(17.5)")
print("Producto 2 codigo:(102)....costo(25.0)")
print("Producto 3 codigo:(103)....costo(15.5)")
print("**************************************")
cod = float(input("Ingrese el codigo de su producto: "))
uni = float(input("Ingrese las unidades a comprar: "))
# Condiciones y Operaciones
if 10 >= uni >= 1:
    des = 0.05
elif 20 >= uni > 10:
    des = 0.075
else:
    des = 0.1

if cod == 101:
    pag = uni * (1 - des) * 17.5
    i = 1
elif cod == 102:
    pag = uni * (1 - des) * 25
    i = 1
elif cod == 103:
    pag = uni * (1 - des) * 15.5
    i = 1
else:
    i = 0
# Resultados
if i == 1:
    print("**************************************")
    desT = des * 100
    print(
        "Ud tiene un descuento del:",
        round(desT, 2),
        "%",
        "\ny un importe total de:",
        round(pag, 2),
    )
else:
    print("Codigo inexistente")
