"""
#Ejercicio 1

print ("Por favor ingrese los datos para calcular el Área de un triangulo");

#Ingreso de datos

b = float(input("Ingrese la medida de la base del triangulo: "));
h = float(input("Ingrese la medida de la altura del triangulo: "));

#Operación

a = (b * h) / 2;

#Resultados

print("El Área del triangulo es: ", round(a, 2));

#Ejercicio 2

print ("Por favor ingrese los datos para calcular el Área de un trapecio");

#Ingreso de datos

B = float(input("Ingrese la medida de la base mayor del trapecio: "));
b = float(input("Ingrese la medida de la base menor del trapecio: "));
h = float(input("Ingrese la medida de la altura del trapecio: "));

#Operación

a = ( (B + b) * h )/ 2;

#Resultados

print("El Área del trapecio es: ", round(a, 2));

#Ejercicio 3

print ("Por favor ingrese los datos del producto para calcular el total a pagar");

#Ingreso de datos

c = float(input("Ingrese el costo unitario del producto: "));
u = int(input("Ingrese la cantidad en unidades del producto: "));

#Operación

t = c * u;

#Resultados

print("El costo total a pagar es: ", round(t, 2));

#Ejercicio 4

print ("Por favor ingrese los numeros enteros para realizar el promedio");

#Ingreso de datos

n1 = int(input("Ingrese el primer numero entero: "));
n2 = int(input("Ingrese el segundo numero entero: "));
n3 = int(input("Ingrese el tercer numero entero: "));

#Operación

p = (n1 + n2 + n3) / 3;

#Resultados

print("El promedio es: ", round(p, 2));


#Ejercicio 5

print ("Por favor ingrese los datos para hallar la hipotenusa del triangulo rectangulo");

#Ingreso de datos

import math;

a = float(input("Ingrese la medida del cateto a: "));
b = float(input("Ingrese la medida del cateto b: "));

#Operación

h = math.sqrt((a**2) + (b**2));

#Resultados

print("La hipotenusa es: ", round(h, 2));


#Ejercicio 6

print ("Por favor ingrese los datos para calcular el pago mensual");

#Ingreso de datos

t = float(input("Ingrese la tarifa por hora trabajada: "));
h = float(input("Ingrese las horas trabajadas: "));

#Operación

s1 = t * h;
s2 = s1 + (s1 * 0.2);
s3 = s2 - (s2 * 0.1); 

#Resultados

print("El Sueldo Basico es: ", round(s1, 2));
print("El Sueldo Bruto es: ", round(s2, 2));
print("El Sueldo Neto es: ", round(s3, 2));


#Ejercicio 7

print ("Por favor ingrese los datos para calcular el monto por persona");

#Ingreso de datos

mt = float(input("Ingrese el monto total a repartir: "));
e1 = int(input("Ingrese la edad de la primera persona: "));
e2 = int(input("Ingrese la edad de la segunda persona: "));
e3 = int(input("Ingrese la edad de la tercera persona: "));

#Operación

m1 = (e1 * mt) / (e1 + e2 + e3);
m2 = (e2 * mt) / (e1 + e2 + e3);
m3 = (e3 * mt) / (e1 + e2 + e3);

#Resultados

print("El Monto que recive la primera persona es: ", round(m1, 2));
print("El Monto que recive la segunda persona es: ", round(m2, 2));
print("El Monto que recive la tercera persona es: ", round(m3, 2)); 


#Ejercicio 8

print ("Por favor ingrese los datos para calcular los importes");

#Ingreso de datos

c = float(input("Ingrese el costo unitario del producto: "));
u = int(input("Ingrese la cantidad en unidades del producto: "));

#Operación

ic = c * u;
id = ic * 0.11;
ip = ic - id;

#Resultados

print("El importe de la compra es: ", round(ic, 2));
print("El importe del descuento es: ", round(id, 2));
print("El importe a pagar es: ", round(ip, 2));


#Ejercicio 9

print ("Por favor ingrese los datos para calcular los importes");

#Ingreso de datos

u = int(input("Ingrese la cantidad en unidades del producto: "));

#Operación

ic = u * 17.5;
id = ic * 0.11;
ip = ic - id;
os = int(u / 12) * 5;

#Resultados

print("El importe de la compra es: ", round(ic, 2));
print("El importe del descuento es: ", round(id, 2));
print("El importe a pagar es: ", round(ip, 2));
print("El obsequio correspondiente es: ", os);


#Ejercicio 10

print ("Por favor ingrese los datos para calcular los importes");

#Ingreso de datos

mtv = float(input("Ingrese el monto total vendido: "));

#Operación

cm = mtv * 0.09
sb = 300 + cm;
dc = sb * 0.11;
sn = sb - dc;

#Resultados

print("El importe de la comision es: ", round(cm, 2));
print("El importe del sueldo bruto es: ", round(sb, 2));
print("El importe del descuento es: ", round(dc, 2));
print("El importe del sueldo neto es: ", round(sn, 2));


#Ejercicio 11

print ("Por favor ingrese los datos para calcular el precio de venta de la pieza");

#Ingreso de datos

pc = float(input("Ingrese el precio de compra de la pieza: "));
pr = float(input("Ingrese el porcentaje de ganancia: "));

#Operación

pg = pc * (pr / 100);
pv = pc + pg;

#Resultados

print("El precio de venta es: ", round(pv, 2));


#Ejercicio 12

print ("Por favor ingrese los datos para calcular los precios de los productos");

#Ingreso de datos

p = float(input("Ingrese el costo de la compra de los polos: "));
g = float(input("Ingrese el costo de la compra de las gorras: "));

#Operación

ic = p + g;
dp = p * 0.15;
dg = g * 0.05;
id = dp + dg;
ip = ic - id;

#Resultados

print("El importe de la compra es: ", round(ic, 2));
print("El importe del descuento es: ", round(id, 2));
print("El importe a pagar es: ", round(ip, 2));


#Ejercicio 13

print ("Por favor ingrese los datos para calcular el sueldo del trabajador");

#Ingreso de datos

h = float(input("Ingrese las horas trabajadas: "));
p = float(input("Ingrese el pago por hora trabajada: "));

#Operación

sb = h * p;
dpe = sb * 0.09;
dpa = sb * 0.125;
dt = dpe + dpa;
sn = sb - dt;

#Resultados

print("El sueldo bruto es: ", round(sb, 2));
print("El descuento por ESSALUD es: ", round(dpe, 2));
print("El descuento por AFP es: ", round(dpa, 2));
print("El sueldo neto es: ", round(sn, 2));
"""

#Ejercicio 14

print ("Por favor ingrese los datos para calcular el porcentaje de estudiantes varones y mujeres");

#Ingreso de datos

e = int(input("Ingrese el numero total de estudiantes: "));
v = int(input("Ingrese el numero de estudiantes varones: "));


#Operación

pv = (v / e) * 100;
pm = ((e - v) / e) * 100;


#Resultados

print("El porcentaje de varones es: ", pv);
print("El porcentaje de mujeres es: ", pm);
