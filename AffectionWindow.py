# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'affectation.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(745, 468)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.spinBoxCol = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBoxCol.setFrame(True)
        self.spinBoxCol.setObjectName("spinBoxCol")
        self.horizontalLayout_3.addWidget(self.spinBoxCol)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.spinBoxRow = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBoxRow.setObjectName("spinBoxRow")
        self.horizontalLayout_3.addWidget(self.spinBoxRow)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.pushButtonGenMatrix = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonGenMatrix.setObjectName("pushButtonGenMatrix")
        self.verticalLayout.addWidget(self.pushButtonGenMatrix)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.verticalLayoutMatrix = QtWidgets.QVBoxLayout()
        self.verticalLayoutMatrix.setObjectName("verticalLayoutMatrix")
        self.verticalLayout.addLayout(self.verticalLayoutMatrix)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.labelResult = QtWidgets.QLabel(self.centralwidget)
        self.labelResult.setStyleSheet("color: rgb(114, 159, 207);\n"
"font: 20pt \"Ubuntu\";\n"
"text-align: center;")
        self.labelResult.setText("")
        self.labelResult.setObjectName("labelResult")
        self.horizontalLayout_2.addWidget(self.labelResult)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 745, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Problème d\'affectation"))
        self.label.setText(_translate("MainWindow", "Entrez la taille de la matrice à genérer : "))
        self.label_2.setText(_translate("MainWindow", "X"))
        self.pushButtonGenMatrix.setText(_translate("MainWindow", "Generer la matrice"))

