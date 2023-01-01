import PyQt5
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from app_main_open_office import Ui_MainWindow
import sys
import os
import ctypes
from PyQt5.QAxContainer import QAxWidget
from axwidget import AxWidget
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import pandas as pd
import seaborn as sns

# To solve the display issue of high-resolution screen
from image_viewer import ImageViewer

myAppId = 'pyqt5-gui-common'  # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myAppId)
if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

class MyMainForm(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        # add click event
        self.btn_open_office.clicked.connect(self.open_office)
        self.axWidget = None

    def openOffice(self, path, app):
        self.axWidget.clear()
        if not self.axWidget.setControl(app):
            return QMessageBox.critical(self, 'Errir', 'Not installed  %s' % app)
        self.axWidget.dynamicCall(
            'SetVisible (bool Visible)', 'false')  # 不显示窗体
        self.axWidget.setProperty('DisplayAlerts', False)
        self.axWidget.setControl(path)

    def closeEvent(self, event):
        try:
            if self.axWidget!=None:
                self.axWidget.close()
                self.axWidget.clear()
                self.layout().removeWidget(self.axWidget)
                del self.axWidget
                super(AxWidget, self).closeEvent(event)
        except Exception as err:
            print(err)

    def open_office(self):
        self.axWidget = QAxWidget(self)
        self.layout_office.addWidget(self.axWidget)
        # self.onOpenFile()
        self.openOffice(path=r"docs/test.docx", app='Word.Application')

    def onOpenFile(self):
        path, _ = QFileDialog.getOpenFileName(
            self, '请选择文件', '', 'excel(*.xlsx *.xls);;word(*.docx *.doc);;pdf(*.pdf)')
        if not path:
            return
        if _.find('*.doc'):
            return self.openOffice(path, 'Word.Application')
        if _.find('*.xls'):
            return self.openOffice(path, 'Excel.Application')
        if _.find('*.pdf'):
            return self.openPdf(path)

if __name__ == "__main__":
    # obtain the current directory for data loading
    current_path = os.path.dirname(__file__)
    print("current path = ", current_path)
    # init the main GUI
    app = QApplication(sys.argv)
    myWin = MyMainForm()
    myWin.show()
    # run the app
    try:
        r = app.exec_()
    except Exception as err:
        print("Error:",err)
