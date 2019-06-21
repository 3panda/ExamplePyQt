# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_ui.ui',
# licensing of 'main_ui.ui' applies.
#
# Created: Fri Jun 21 13:38:48 2019
#      by: pyside2-uic  running on PySide2 5.12.4
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(756, 771)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.imagePath = QtWidgets.QLineEdit(self.centralwidget)
        self.imagePath.setGeometry(QtCore.QRect(40, 60, 491, 41))
        self.imagePath.setObjectName("imagePath")
        self.graphicsViewImage = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsViewImage.setGeometry(QtCore.QRect(40, 140, 651, 441))
        self.graphicsViewImage.setObjectName("graphicsViewImage")
        self.selectButton = QtWidgets.QPushButton(self.centralwidget)
        self.selectButton.setGeometry(QtCore.QRect(560, 60, 131, 51))
        self.selectButton.setObjectName("selectButton")
        self.pushButtonViewStart = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonViewStart.setGeometry(QtCore.QRect(320, 610, 113, 61))
        self.pushButtonViewStart.setObjectName("pushButtonViewStart")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar()
        self.menubar.setGeometry(QtCore.QRect(0, 0, 756, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.selectButton.setText(QtWidgets.QApplication.translate("MainWindow", "selectButton", None, -1))
        self.pushButtonViewStart.setText(QtWidgets.QApplication.translate("MainWindow", "Start", None, -1))

