# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\PC-12\Desktop\EDDPOO_II.04.2023-IIE\SEMANA4\frmPrueba.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(425, 326)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnProcesar = QtWidgets.QPushButton(self.centralwidget)
        self.btnProcesar.setGeometry(QtCore.QRect(20, 110, 90, 28))
        self.btnProcesar.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 85, 255);\n"
"font: 75 11pt \"Comic Sans MS\";")
        self.btnProcesar.setObjectName("btnProcesar")
        self.btnLimpiar = QtWidgets.QPushButton(self.centralwidget)
        self.btnLimpiar.setGeometry(QtCore.QRect(170, 110, 90, 28))
        self.btnLimpiar.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 85, 255);\n"
"font: 75 11pt \"Comic Sans MS\";")
        self.btnLimpiar.setObjectName("btnLimpiar")
        self.btnSalir = QtWidgets.QPushButton(self.centralwidget)
        self.btnSalir.setGeometry(QtCore.QRect(315, 110, 90, 28))
        self.btnSalir.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 85, 255);\n"
"font: 75 11pt \"Comic Sans MS\";")
        self.btnSalir.setObjectName("btnSalir")
        self.lblTexto = QtWidgets.QLabel(self.centralwidget)
        self.lblTexto.setGeometry(QtCore.QRect(80, 40, 261, 30))
        self.lblTexto.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblTexto.setStyleSheet("font: 75 10pt \"Comic Sans MS\";")
        self.lblTexto.setLineWidth(1)
        self.lblTexto.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTexto.setWordWrap(False)
        self.lblTexto.setObjectName("lblTexto")
        self.lblIcon = QtWidgets.QLabel(self.centralwidget)
        self.lblIcon.setGeometry(QtCore.QRect(100, 180, 211, 101))
        self.lblIcon.setText("")
        self.lblIcon.setPixmap(QtGui.QPixmap("c:\\Users\\PC-12\\Desktop\\EDDPOO_II.04.2023-IIE\\SEMANA4\\qtDesigner1.png"))
        self.lblIcon.setScaledContents(True)
        self.lblIcon.setObjectName("lblIcon")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnProcesar.setText(_translate("MainWindow", "PROCESAR"))
        self.btnLimpiar.setText(_translate("MainWindow", "LIMPIAR"))
        self.btnSalir.setText(_translate("MainWindow", "SALIR"))
        self.lblTexto.setText(_translate("MainWindow", "Escriba el texto aqui.."))