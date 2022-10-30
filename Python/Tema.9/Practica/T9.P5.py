""


# Ejercicio 5


# Ingreso de Datos

lista = []

c = 0

while True:

    n = int(input(str(c + 1) + ".- Ingrese un numero: "))

    if n == 0:

        break

    if n % 5 == 0:

        lista.append(n)

    c += 1

print("Números Ingresados:", lista)

# Operación


# Resultados

print("Programa terminado")
