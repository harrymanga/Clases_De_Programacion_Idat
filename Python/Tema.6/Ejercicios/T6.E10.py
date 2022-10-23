"""

# Ejercicio 10

print("Ingrese los datos necesarios")

# Ingreso de Datos

pre = [
    "Caramelo de limón",
    "Chupetín",
    "Chocolate",
    "Gaseosa personal",
    "Gaseosa de 1 litro",
    "Gaseosa de 2 litros",
]

nu = int(input("ingrese el resultado obtenido en el dado: "))

# Operaciones

if nu <= 6:

    res = pre[nu - 1]

else:

    res = "Valor de dado incorrecto"

# Resultado

print(res)"""


# Ejercicio 10

print("Ingrese los datos necesarios")

# Ingreso de Datos

nu = int(input("ingrese el resultado obtenido en el dado: "))

# Operaciones

if nu <= 6:

    if nu == 1:

        res = "Su premio es un Caramelo de limón."

    elif nu == 2:

        res = "Su premio es un Chupetín."

    elif nu == 3:

        res = "Su premio es un Chocolate."

    elif nu == 4:

        res = "Su premio es una Gaseosa personal."

    elif nu == 5:

        res = "Su premio es una Gaseosa de 1 litro."

    else:

        res = "Su premio es una Gaseosa de 2 litros."

else:

    res = "Valor de dado incorrecto"

# Resultado

print(res)
