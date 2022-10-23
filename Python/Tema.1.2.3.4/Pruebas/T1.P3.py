"""
#Ejercicio 1
#Ingreso de datos

x = float(input("Ingrese el perimetro del octagono: "))

y = float(input("ingrese el apotema del octagono: "))

#Operación

z = (x*y) / 2

#Resultados
print("El resultado es: ", z)


#Ejercicio 2

#Ingreso de datos

d1= float(input("Ingrese la diagonal mayor: "))

d2= float(input("ingrese la diagonal menor: "))

#Operación

a = ( d1 * d2) / 2

#Resultados

print("El Area del Rombo es: ", a)

#Ejercicio 3

#Ingreso de datos

import math;
r=float(input("Ingrese el Radio : "));

#Operación

a = 4 * math.pi * ( r**2 );

v = ( 4 * math.pi * ( r**3 ) ) / 3;

#Resultados

print("El Area de la Esfera es : ", round( a, 2 ));
print("El Volumen de la Esfera es : ", round( v, 2 ));

#Ejercicio 4

#Ingreso de datos

import math;

l=float(input("Ingrese la medida del Lado del prisma : "));
h=float(input("Ingrese la medida de La altura del prisma: "));

#Operación

v = ( (3**(1/2)) * ( l**2 ) * h) / 12;

#Resultados

print("El Volumen del prisma es : ", round( v, 2 ));

#Ejercicio 5

#Ingreso de datos

import math;

a = float(input("Ingrese la medida de la arista del icosaedro : "));

#Operación

a1 = 5 * (math.sqrt(3)) * (a**2);
v =  (5 * (3 + math.sqrt(5)) * (a**3))/ 12;

#Resultados

print("El Area del icosaedro es : ", round( a1, 2 ));
print("El Volumen del icosaedro es : ", round( v, 2 ));"""

#Ejercicio 6

#Ingreso de datos

import math;

r1 = float(input("Ingrese la medida del Radio mayor : "));
r2 = float(input("Ingrese la medida del Radio menor : "));

#Operación

a = 4 * math.pi * r1 * r2;


#Resultados

print("El Area del Toroide es : ", round( a, 2 ));
