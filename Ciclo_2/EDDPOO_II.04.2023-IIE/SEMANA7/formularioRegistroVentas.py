""
# !/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from PyQt5 import QtWidgets, uic

qtCreatorFile = "frmRegistroVentas.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class FormularioVentas(QtWidgets.QMainWindow):
    def __init__(self):
        
        super(FormularioVentas, self).__init__()

        uic.loadUi("frmRegistroVentas.ui", self)

        self.btnRegistrar.clicked.connect(self.registrar)

        self.btnNuevo.clicked.connect(self.nuevo)

        self.btnSalir.clicked.connect(self.salir)

        self.show()

    def registrar(self):
        
        # Entrada de Datos

        producto = self.cboProducto.currentText()

        tipoPago = self.cboPago.currentText()

        cantidad = self.txtCantidad.text()

        # Precio del producto

        precio = 0

        if producto == "Colección Escolar":
            precio = 240

        elif producto == "Colección PreUniversitaria":
            precio = 150

        elif producto == "Colección Profesional":
            precio = 350

        self.lblPrecio.set.Text("S/. " + str(precio))

        # Proceso de Calculo

        # try:

        # Salida de Resultados en las lineas de texto

        # Salida de Resultados en la caja de texto

        # except ValueError:

        # self.txtS.append("Dato Invalido, Ingrese solo precios validos.")

    def nuevo(self):
        
        pass

    def salir(self):
        
        self.close()

if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)

    window = FormularioVentas()

    app.exec()
