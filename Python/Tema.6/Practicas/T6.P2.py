""

# Ejercicio


# Ingreso de Datos

edad = int(input("Ingrese su edad: "))

# Operación

if edad < 0:

    m = "Error: no existe una edad negativa"

elif edad < 18:

    m = "es menor de edad"

else:

    m = "es mayor de edad"

# Resultados

print(m)
