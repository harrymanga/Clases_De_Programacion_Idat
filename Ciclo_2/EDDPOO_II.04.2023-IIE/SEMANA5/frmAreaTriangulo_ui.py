# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\PC-12\Desktop\EDDPOO_II.04.2023-IIE\SEMANA5\frmAreaTriangulo.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(425, 289)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnCalcular = QtWidgets.QPushButton(self.centralwidget)
        self.btnCalcular.setGeometry(QtCore.QRect(320, 20, 90, 28))
        self.btnCalcular.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 85, 255);\n"
"font: 75 11pt \"Comic Sans MS\";")
        self.btnCalcular.setObjectName("btnCalcular")
        self.btnLimpiar = QtWidgets.QPushButton(self.centralwidget)
        self.btnLimpiar.setGeometry(QtCore.QRect(320, 70, 90, 28))
        self.btnLimpiar.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 85, 255);\n"
"font: 75 11pt \"Comic Sans MS\";")
        self.btnLimpiar.setObjectName("btnLimpiar")
        self.btnSalir = QtWidgets.QPushButton(self.centralwidget)
        self.btnSalir.setGeometry(QtCore.QRect(320, 120, 90, 28))
        self.btnSalir.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 85, 255);\n"
"font: 75 11pt \"Comic Sans MS\";")
        self.btnSalir.setObjectName("btnSalir")
        self.lblBase = QtWidgets.QLabel(self.centralwidget)
        self.lblBase.setGeometry(QtCore.QRect(10, 30, 90, 28))
        self.lblBase.setStyleSheet("font: 11pt \"Gill Sans Ultra Bold\";")
        self.lblBase.setAlignment(QtCore.Qt.AlignCenter)
        self.lblBase.setObjectName("lblBase")
        self.lblAltura = QtWidgets.QLabel(self.centralwidget)
        self.lblAltura.setGeometry(QtCore.QRect(20, 80, 90, 28))
        self.lblAltura.setStyleSheet("font: 11pt \"Gill Sans Ultra Bold\";")
        self.lblAltura.setAlignment(QtCore.Qt.AlignCenter)
        self.lblAltura.setObjectName("lblAltura")
        self.txtBase = QtWidgets.QLineEdit(self.centralwidget)
        self.txtBase.setGeometry(QtCore.QRect(130, 30, 113, 20))
        self.txtBase.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.txtBase.setObjectName("txtBase")
        self.txtAltura = QtWidgets.QLineEdit(self.centralwidget)
        self.txtAltura.setGeometry(QtCore.QRect(130, 80, 113, 20))
        self.txtAltura.setObjectName("txtAltura")
        self.txtS = QtWidgets.QTextEdit(self.centralwidget)
        self.txtS.setGeometry(QtCore.QRect(30, 130, 260, 130))
        self.txtS.setObjectName("txtS")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.txtBase, self.txtAltura)
        MainWindow.setTabOrder(self.txtAltura, self.btnCalcular)
        MainWindow.setTabOrder(self.btnCalcular, self.btnLimpiar)
        MainWindow.setTabOrder(self.btnLimpiar, self.btnSalir)
        MainWindow.setTabOrder(self.btnSalir, self.txtS)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnCalcular.setText(_translate("MainWindow", "CALCULAR"))
        self.btnLimpiar.setText(_translate("MainWindow", "LIMPIAR"))
        self.btnSalir.setText(_translate("MainWindow", "SALIR"))
        self.lblBase.setText(_translate("MainWindow", "BASE :"))
        self.lblAltura.setText(_translate("MainWindow", "ALTURA :"))
