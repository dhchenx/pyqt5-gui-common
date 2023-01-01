import PyQt5
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from app_main_show_matplotlib import Ui_MainWindow
import sys
import os
import ctypes
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import pandas as pd
import seaborn as sns

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
        self.btn_show_matplotlib.clicked.connect(self.show_matplotlib)

    def show_matplotlib(self):
        # init canvas
        figure = plt.figure(facecolor='#FFFFFF')
        canvas = FigureCanvas(figure)
        self.layout_matplotlib.addWidget(canvas)
        # create dataset
        list_x = [0,1,2,3,4,5]
        list_y = [44,22,34,88,55,66]
        dd = {"Time": list_x, "Count": list_y}
        df = pd.DataFrame(dd)
        # plot
        ax = sns.lineplot(x="Time", y="Count", data=df)
        # ax.axes.xaxis.set_ticklabels([])
        # ax.set_xticklabels(['7-1','7-2','7-3','7-4','7-5','7-6','7-7','7-8'])
        # plt.xticks(rotation=15)
        # plt.margins(1)
        plt.subplots_adjust(bottom=0.2)
        # plt.xticks([])
        canvas.draw()

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
