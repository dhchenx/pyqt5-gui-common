# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app_main_show_matplotlib.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(624, 422)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_show_matplotlib = QtWidgets.QPushButton(self.centralwidget)
        self.btn_show_matplotlib.setGeometry(QtCore.QRect(200, 290, 191, 23))
        self.btn_show_matplotlib.setObjectName("btn_show_matplotlib")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(110, 30, 421, 241))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.layout_matplotlib = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.layout_matplotlib.setContentsMargins(0, 0, 0, 0)
        self.layout_matplotlib.setObjectName("layout_matplotlib")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 624, 22))
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
        self.btn_show_matplotlib.setText(_translate("MainWindow", "Show matplotlib"))
