""

# Ejercicio 1


# Ingreso de Datos


# Operación

valores = [25, "Pedro", 9.56, [100, 35, 22], "Juan", 25, 25]

valores.append("Sábado")

valores.append([29, 10, 2022])

valores.extend([29, 10, 2022])

valores.remove(
    "Pedro"
)  # remove() solo elimina el primer elemento de la lista que encuentre

valores.remove(25)

print(valores)

print("Indice de 9.56: ", valores.index(9.56))

# Resultados

print("Programa terminado")
