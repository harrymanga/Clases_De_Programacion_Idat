""
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ejercicio 14

print("Ingrese los datos necesarios")

# Ingreso de datos

from random import randint

c = 1

s = 0

while True:

    print("JUEGO N°:", c)

    c += 1

    nr = randint(1, 6)

    print("Numero Generado", nr)

    if nr == 1 or nr == 6:

        print("Usted gano S/.5")

        s += 5

    else:

        print("Usted perdió S/.2")

        s -= 2

    while True:

        men = input(
            "¿Desea registrar otro producto? , para continuar ingrese Si, si desea terminar ingrese No: "
        ).lower()

        if men.isdigit() or men == "":

            print("Error ingrese Si o No")

        else:

            break

    if men != "si":

        break

# Operación

if s < 0:

    s = s * -1

    res = "Usted Perdió el juego, debe pagar S/." + str(s)

else:

    res = "Usted Gano el juego, su monto acumulado es S/." + str(s)

# Resultados

print(res)

print("Muchas Gracias, programa terminado.")
