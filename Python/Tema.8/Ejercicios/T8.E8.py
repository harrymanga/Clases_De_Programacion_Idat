""

# Ejercicio 8


# Ingreso de Datos

n = int(input("Ingrese el número de terminos : "))

# Operación

c = 0

s = 0

for i in range(1, n + 1):

    c += 1

    i *= 2

    s += i

    print(str(c) + ".-", i)

print("La suma es:", s)

# Resultados

print("Programa terminado")
