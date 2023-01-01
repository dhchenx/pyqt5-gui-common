import PyQt5
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from app_main import Ui_MainWindow
import sys
import os
import ctypes

# To solve the display issue of high-resolution screen
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
        self.btn_test.clicked.connect(self.click_me)

    def click_me(self):
        QMessageBox.information(self,"Tips","Clicked")

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
