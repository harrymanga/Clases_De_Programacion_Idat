""
# !/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from PyQt5 import QtWidgets, uic

qtCreatorFile = "frmAreaTriangulo.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class AreaTriangulo(QtWidgets.QMainWindow):
    
    def __init__(self):
        
        super(AreaTriangulo, self).__init__()
        
        uic.loadUi("frmAreaTriangulo.ui", self)
        
        
        self.btnCalcular.clicked.connect(self.calcular)

        self.btnLimpiar.clicked.connect(self.limpiar)

        self.btnSalir.clicked.connect(self.salir)

        self.show()
        
    def calcular(self):
        
        # Entrada de Datos
            
        base = self.txtBase.text()
                   
        altura = self.txtAltura.text()
            
        # Proceso de Calculo
        
        try:
             
            area = ( float(base) * float(altura) ) / 2
                       
        # Salida de Resultados
        
            self.txtS.setText("AREA DEL TRIANGULO : \n")
            
            self.txtS.append(f"El valor de la base es : {float(base)}")
            
            self.txtS.append(f"El valor de la altura es : {float(altura)}")
            
            self.txtS.append(f"El valor del area es : {area}")

        except ValueError:
            
            self.txtS.append("Dato Invalido, Ingrese solo Números")

    def limpiar(self):
        
        self.txtBase.setText("")
        
        self.txtAltura.setText("")
        
        self.txtS.setText("")
        
    def salir(self):
        
        self.close()

if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    
    window =AreaTriangulo()
    
    app.exec()
        
        


