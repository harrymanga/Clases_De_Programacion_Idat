""

# Ejercicio 3

# ingreso de datos

vocales = ["a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú", "ü"]

while True:
    nom = input("Ingrese su nombre: ").lower()

    if nom.isalpha():

        break

    else:

        print("Ingrese solo letras")

# operación

cantV = 0

for letra in nom:

    if letra in vocales:

        cantV += 1

cantL = len(nom)

cantC = cantL - cantV

# resultados

print("La cantidad de letras es:", cantL)

print("La cantidad de vocales es:", cantV)

print("La cantidad de consonantes es:", cantC)

print("Programa terminado")
