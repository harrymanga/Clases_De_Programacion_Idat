""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Ejercicio 10 - A

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

    res = "Su premio es " + pre[nu - 1]

else:

    res = "Valor de dado incorrecto"

# Resultado

print(res)

print("Muchas Gracias, programa terminado.")