""

# Ejercicio 10


# Ingreso de Datos

n = int(input("Ingrese el total de tablas: "))

# Operación

for j in range(1, n + 1):

    print("\nTabal de multiplicar del", j)

    print("**************************")

    for i in range(1, 13):

        print(i, "*", j, "=", i * j)


# Resultados

print("Programa terminado")
