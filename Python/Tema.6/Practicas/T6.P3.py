""

# Ejercicio


# Ingreso de Datos

edad = int(input("Ingrese su edad: "))
# operación
if edad < 0:
    m = "Error: no existe una edad negativa"
elif edad < 15:
    m = "eres bastante joven"
elif edad < 30:
    m = "eres muy joven"
elif edad < 50:
    m = "eres joven"
elif edad < 80:
    m = "eres casi un joven"
else:
    m = "igual ya te vas haciendo mayor"
# resultados
print(m)
