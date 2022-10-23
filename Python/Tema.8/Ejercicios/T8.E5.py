""

# Ejercicio 5


# Ingreso de Datos

while True:

    n1 = int(input("Ingrese el primer número menor del intervalo : "))

    n2 = int(input("Ingrese el segundo número mayor del intervalo : "))

    if n1 >= n2:

        print("Intervalo no admitido")

    else:

        break

# Operación

c = 0

for i in range(n1, n2 + 1):

    c += 1

    print(str(c) + ".-", i)

# Resultados

print("Programa terminado")
