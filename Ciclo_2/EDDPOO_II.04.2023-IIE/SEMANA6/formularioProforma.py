""
# !/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from PyQt5 import QtWidgets, uic

qtCreatorFile = "SEMANA6/frmProforma.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class Proforma(QtWidgets.QMainWindow):
    
    def __init__(self):
        
        super(Proforma, self).__init__()
        
        uic.loadUi("SEMANA6/frmProforma.ui", self)
        
        
        self.rbInteres1.setChecked(True)
        
        self.rbMayorista.setChecked(True)        
        
        self.btnCalcular.clicked.connect(self.calcular)

        self.btnLimpiar.clicked.connect(self.limpiar)

        self.btnSalir.clicked.connect(self.salir)
        
        self.show()
        
        
    def calcular(self):
        
        # Entrada de Datos
        
        codigoCliente = self.txtCodigoCliente.text()
        
        nombreCliente = self.txtNombreCliente.text()
        
        producto = self.txtProducto.text()
                   
        precio = self.txtPrecio.text()
                   
        cantidad = self.spbCantidad.value()
            
        # Proceso de Calculo
        
        try:
             
            importe = float(precio) * int(cantidad)
            
            porcentajeDescuento = 0
            
            if self.rbMayorista.isChecked() == True:
                
                porcentajeDescuento = 4.5 / 100
                
            if self.rbMinorista.isChecked() == True:
                
                porcentajeDescuento = 1.9 / 100   
                
            descuento = importe * porcentajeDescuento 
            
            porcentajeInteres = 0
            
            if self.rbInteres1.isChecked() == True:
                
                porcentajeInteres = 0
                
            if self.rbInteres2.isChecked() == True:
                
                porcentajeInteres = 8.5 / 100   

            if self.rbInteres3.isChecked() == True:
                
                porcentajeInteres = 12.5 / 100 
                                  
            interes = importe * porcentajeInteres
            
            total = importe - descuento + interes
            
                  
        # Salida de Resultados en las lineas de texto
        
            self.txtImporte.setText("S/."+ str("{:.2f}".format(importe)))
        
            self.txtDescuento.setText("S/."+ str("{:.2f}".format(descuento)))
            
            self.txtInteres.setText("S/."+ str("{:.2f}".format(interes)))
            
            self.txtTotal.setText("S/."+ str("{:.2f}".format(total)))
            
            
        # Salida de Resultados en la caja de texto
        
            self.txtS.setText("============= ".center(80))
            
            self.txtS.append("| PROFORMA | ".center(91))
            
            self.txtS.append("============= \n".center(81))
            
            self.txtS.append(f"CÓDIGO DEL CLIENTE\t: {codigoCliente}")
            
            self.txtS.append(f"NOMBRE DEL CLIENTE\t: {nombreCliente}\n")           
            
            self.txtS.append(f"PRODUCTO\t\t: {producto}")
            
            self.txtS.append("PRECIO\t\t: S/." + str("{:.2f}".format(float(precio))))
            
            self.txtS.append(f"CANTIDAD\t\t: {cantidad}")
            
            self.txtS.append("El importe de la compra es\t: S/." + str("{:.2f}".format(importe)))
            
            self.txtS.append("El descuento de la compra es\t: S/." + str("{:.2f}".format(descuento)))
            
            self.txtS.append("El interés de la compra es\t: S/." + str("{:.2f}".format(interes)))
            
            self.txtS.append("El total a pagar es\t: S/." + str("{:.2f}".format(total)))
        
        except ValueError:
            
            self.txtS.append("Dato Invalido, Ingrese solo precios validos.") 


    def limpiar(self):
        
        self.txtCodigoCliente.setText("")
        
        self.txtNombreCliente.setText("")
        
        self.txtProducto.setText("")
        
        self.txtPrecio.setText("")
        
        self.txtImporte.setText("")
        
        self.txtDescuento.setText("")
        
        self.txtInteres.setText("")
        
        self.txtTotal.setText("")
        
        self.txtS.setText("")
        
        self.rbInteres1.setChecked(True)
        
        self.rbMayorista.setChecked(True)
        
        self.spbCantidad.setValue(0)  
        
    def salir(self):
        
        self.close()        
           

if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    
    window = Proforma()
    
    app.exec()
        
        


