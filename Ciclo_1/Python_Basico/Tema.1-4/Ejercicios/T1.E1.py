""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

# Cargar el archivo de idiomas

with open("T1.E1.ES.json", "r") as file:
    
    lang = json.load(file)

# Ejercicio 1

print(lang["prompt_initial"])

# Ingreso de Datos

a = int(input(lang["prompt_input_a"]))

b = int(input(lang["prompt_input_b"]))

# Operación

n1 = a ** b

n2 = b ** a

n3 = b ** (1/a)

n4 = a ** (1/b)

# Resultados

print(lang["result_power_ab"], n1)

print(lang["result_power_ba"], n2)

print(lang["result_root_b_of_a"], n3)

print(lang["result_root_a_of_b"], n4)

print(lang["thank_you"])
