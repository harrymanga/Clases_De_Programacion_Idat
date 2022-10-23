""

# Ejercicio 9


# Ingreso de Datos

n = int(input("Ingrese el valor de N: "))

# Operación

f = 1

if n < 0:

    print("No existe factorial de números negativos")

else:

    for i in range(1, n + 1):

        f *= i

    print("El factorial de ", n, "=", f)

# Resultados

print("Programa terminado")
