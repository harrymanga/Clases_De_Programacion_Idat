""
# !/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from PyQt5 import QtWidgets, uic

qtCreatorFile = "SEMANA4/frmPrueba.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class FormularioPrueba(QtWidgets, QtMainWindow):
    
    def __init__(self):ç
        
        super(FormularioPrueba, self).__init__()
        
        uic.loadUi("SEMANA4/frmPrueba,ui", self)
        
        self.show()

if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    
    window = FormularioPrueba()
    
    app.exec()
        
    
        
        


