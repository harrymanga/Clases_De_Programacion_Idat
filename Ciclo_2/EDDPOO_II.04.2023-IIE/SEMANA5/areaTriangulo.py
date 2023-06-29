""
# !/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from PyQt5 import QtWidgets, uic

qtCreatorFile = "SEMANA5/frmAreaTriangulo.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class AreaTriangulo(QtWidgets.QMainWindow):
    
    def __init__(self):
        
        super(AreaTriangulo, self).__init__()
        
        uic.loadUi("SEMANA5/frmAreaTriangulo.ui", self)
        
        
        self.btnCalcular.clicked.connect(self.calcular)

        self.btnLimpiar.clicked.connect(self.limpiar)

        self.btnSalir.clicked.connect(self.salir)

        self.show()
        
    def calcular(selft):
        
        # Entrada de Datos
            
        base = selft.txtBase.text()
                   
        altura = selft.txtAltura.text()
            
        # Proceso de Calculo
        
        try:
             
            area = ( float(base) * float(altura) ) / 2
                       
        # Salida de Resultados
        
            selft.txtS.setText("AREA DEL TRIANGULO : \n")
            
            selft.txtS.append(f"El valor de la base es : {float(base)}")
            
            selft.txtS.append(f"El valor de la altura es : {float(altura)}")
            
            selft.txtS.append(f"El valor del area es : {area}")

        except ValueError:
            
            selft.txtS.append("Dato Invalido, Ingrese solo Números")

    def limpiar(selft):
        
        selft.txtBase.setText("")
        
        selft.txtAltura.setText("")
        
        selft.txtS.setText("")
        
    def salir(selft):
        
        selft.close()

if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    
    window =AreaTriangulo()
    
    app.exec()
        
        


