""

# Ejercicio 6

lista = []

# ingreso de datos

cantidad = int(input("Ingrese la cantidad de estaturas: "))

for i in range(1, cantidad + 1):

    while True:

        est = float(input(str(i) + ".- Ingrese la estatura: "))

        if 0.50 <= est <= 2.50:

            lista.append(est)

            break

        else:

            print("Ingrese una estatura en el rango de [0.50 a 2.50] metros")

# operación

prom = sum(lista) / len(lista)

lista2 = []

for est in lista:

    if est > prom:

        lista2.append(est)

# resultados

print("Estaturas ingresadas:", lista)

print("Estatura promedio:", round(prom, 2))

print("Las estaturas mayores al promedio son:", lista2)

print("Cantidad de estaturas mayores al promedio:", len(lista2))

print("Programa terminado")
