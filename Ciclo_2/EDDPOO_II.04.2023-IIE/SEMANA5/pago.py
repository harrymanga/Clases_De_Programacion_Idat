""
# !/usr/bin/env python
# -*- coding: utf-8 -*-

#El cálculo del pago mensual de un empleado de una empresa se efectúa de la siguiente manera: el sueldo básico se calcula en base al número total de horas trabajadas basado en una tarifa horaria; al sueldo básico, se le aplica una bonificación del 20% obteniéndose el sueldo bruto; al sueldo bruto, se le aplica un descuento del 10% obteniéndose el sueldo neto. Escriba un programa que calcule e imprima el sueldo básico, el sueldo bruto y el sueldo neto de un trabajador. 

import sys

from PyQt5 import QtWidgets, uic

qtCreatorFile = "frmPago.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class PagoMensual(QtWidgets.QMainWindow):
    
    def __init__(self):
        
        super(PagoMensual, self).__init__()
        
        uic.loadUi("frmPago.ui", self)
        
        
        self.btnProcesar.clicked.connect(self.procesar)

        self.btnLimpiar.clicked.connect(self.limpiar)

        self.btnSalir.clicked.connect(self.salir)

        self.show()
        
    def procesar(self):
        
        # Entrada de Datos
            
        horas = self.txtHoras.text()
                   
        tarifa = self.txtTarifa.text()
            
        # Proceso de Calculo
         
        try:
             
            sueldoBasico = int(horas) * float(tarifa)
            
            sueldoBruto = sueldoBasico * 1.2
            
            sueldoNeto = sueldoBruto * 0.9
                       
        # Salida de Resultados
        
            self.txtS.setText("PAGO MENSUAL DEL EMPLEADO : \n")
            
            self.txtS.append(f"El Sueldo Básico es : {round(sueldoBasico, 2)}")
            
            self.txtS.append(f"El Sueldo Bruto es : {round(sueldoBruto, 2)}")
            
            self.txtS.append(f"El Sueldo Neto es : {round(sueldoNeto, 2)}")

        except ValueError:
            
            self.txtS.append("Dato Invalido, Ingrese solo horas o tarifas validas.")

    def limpiar(self):
        
        self.txtHoras.setText("")
        
        self.txtTarifa.setText("")
        
        self.txtS.setText("")
        
    def salir(self):
        
        self.close()

if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    
    window = PagoMensual()
    
    app.exec()
        
        


