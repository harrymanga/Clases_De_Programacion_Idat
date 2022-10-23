""

# Ejercicio 1


# Ingreso de Datos

mtv = float(input("Ingrese el Monto de la venta: "))
sms = float(input("Ingrese el Monto del sueldo mensual: "))

# Operación

if mtv < 500:

    com = 0

elif mtv < 1000:

    com = mtv * 0.05

else:

    com = mtv * 0.15

mtt = com + sms

# Resultados

print("La comision es de: ", round(mtt, 2))
