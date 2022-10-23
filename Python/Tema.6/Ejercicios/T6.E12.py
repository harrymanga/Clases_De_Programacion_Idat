"""

# Ejercicio 11

print("Ingrese los datos necesarios")

# Ingreso de Datos

día = [
    "Lunes",
    "Martes",
    "Miércoles",
    "Jueves",
    "Viernes",
    "Sábado",
    "Domingo",
]

nu = int(input("ingrese el numero del día de la semana: "))

# Operaciones

if nu <= 7:

    res = día[nu - 1]

else:

    res = "Valor de dado incorrecto"

# Resultado

print(res)

"""


# Ejercicio 12

print("Ingrese los datos necesarios")

# Ingreso de Datos

a = float(input("ingrese la medida del lado A: "))

b = float(input("ingrese la medida del lado B: "))

c = float(input("ingrese la medida del lado C: "))

# Operaciones

if a < (b + c) and a > (b - c):

    pass

if a == b and a == c:

    res = "El triangulo es equilátero"

elif a == b and a != c:

    res = "El triangulo es isósceles"

else:

    res = 3

# Resultado

print(res)
