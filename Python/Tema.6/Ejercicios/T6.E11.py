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


# Ejercicio 11

print("Ingrese los datos necesarios")

# Ingreso de Datos

nu = int(input("ingrese el numero del día de la semana: "))

# Operaciones

if nu <= 7:

    if nu == 1:

        res = "El día de la semana es Lunes."

    elif nu == 2:

        res = "El día de la semana es Martes."

    elif nu == 3:

        res = "El día de la semana es Miércoles."

    elif nu == 4:

        res = "El día de la semana es Jueves."

    elif nu == 5:

        res = "El día de la semana es Viernes."

    elif nu == 6:

        res = "El día de la semana es Sábado."

    else:

        res = "El día de la semana es Domingo."
else:

    res = "Valor de dado incorrecto"

# Resultado

print(res)
