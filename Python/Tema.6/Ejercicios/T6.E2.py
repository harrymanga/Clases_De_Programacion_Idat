""

# Ejercicio 2

# Ingreso de Datos

mtc = float(input("Ingrese el Monto de la compra: "))

# Operación

if mtc >= 500:

    des = mtc * 0.3

elif mtc >= 200:

    des = mtc * 0.2

elif mtc >= 100:

    des = mtc * 0.1
else:

    des = 0

mtp = mtc - des

# Resultados

print("La comision es de: ", round(mtp, 2))
