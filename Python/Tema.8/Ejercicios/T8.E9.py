""

# Ejercicio 9


# Ingreso de Datos

n = int(input("Ingrese el número de términos : "))

# Operación

c = 0

s1 = 0

s2 = 0

for i in range(2, n + 1, 3):

    c += 1

    s1 += i


for j in range(3, n + 1, 2):

    s2 += j

    print(str(c) + ".-", i, "/", j)

print("La suma es:", s1)

# Resultados

print("Programa terminado")
