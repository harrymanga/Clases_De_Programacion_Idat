""

# Ejercicio 3

# Ingreso de Datos

n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el segundo numero: "))

# Operación

if n1 % n2 == 0:

    res = str(n1) + " es múltiplo de " + str(n2)

elif n2 % n1 == 0:

    res = str(n2) + " es múltiplo de " + str(n1)

else:

    res = "Los números no son múltiplos entre si"

# Resultados

print(res)
