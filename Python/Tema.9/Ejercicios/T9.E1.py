""

# Ejercicio 1

# ingreso de datos

lista = []

for i in range(1, 11):

    while True:

        nota = int(input(str(i) + ".- Ingrese la nota: "))

        if 0 <= nota <= 20:

            lista.append(nota)

            break

        else:

            print("Ingrese una nota entre 0 y 20")

# operación

p = sum(lista) / len(lista)

# resultados

print("Notas Ingresadas:", lista)

print("Promedio de notas:", round(p, 2))

print("Programa terminado")
