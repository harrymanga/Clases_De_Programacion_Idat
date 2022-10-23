""" 
#Ejercicio 1
a = int(input("Ingrese el numero a: "));
b = int(input("Ingrese el numero b: "));
n1 = a ** b;
n2 = b ** a;
n3 = b ** (1/a);
n4 = a ** (1/b);
print("La operacion a elevado a la b es: ", n1);
print("La operacion b elevado a la a es: ", n2);
print("La raiz a de b es: ", n3);
print("La raiz b de a es: ", n4);
#Ejercicio 2
a = float(input("Ingrese el precio: "));
b = int(input("Ingrese la cantidad: "));
c = float(input("Ingrese el porcentaje de descuento: "));

n1 = a * b;
n2 = (c/100) * n1;
n3 = n1 - n2;

print("El importe de la compra es: ", n1);
print("El importe del descuento es: ", n2);
print("El importe a pagar es: ", n3);
#Ejercicio 3
a = float(input("Ingrese la medida del Lado A: "));
b = float(input("Ingrese la medida del Lado B: "));
c = float(input("Ingrese la medida del Lado C: "));

p = (a + b + c) / 2;
area = (p*(p-a)*(p-b)*(p-c)) ** (1/2);

print("El area del triangulo es: ", round(area, 5));

#Ejercicio 4
s = float(input("Ingrese el Sueldo: "));
m = float(input("Ingrese los minutos de tardanza: "));
d = float(input("Ingrese los dias de inasistencia: "));
dt = m * 1.5;
dd = d * 34;
pnt = s - (dt + dd);
print("El monto de descuento por minutos de tardanza es: ", dt);
print("El monto de descuento por dia de inasistencia es: ", dd);
print("El pago neto es: ", pnt);"""
#Ejercicio 5
s = float(input("Ingrese el Sueldo: "));
b = s * (15/100);
print("El monto de la bonificacion es: ", b);

