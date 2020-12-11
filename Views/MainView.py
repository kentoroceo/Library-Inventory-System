from PyQt5.QtWidgets import QMainWindow, QSizePolicy
from PyQt5.QtCore import pyqtSlot
from Views.MainViewUI import Ui_Main

from PyQt5 import QtCore, QtGui, QtWidgets

#MainView class communicates with UI that connects to a controller to perform backend operations
class MainView(QMainWindow):
    def __init__(self):
        super().__init__()

        self._ui = Ui_Main()
        self._ui.setupUi(self)
        

    def setScreen(self, child):
        self._ui.stackedWidget.addWidget(child)
        self._ui.stackedWidget.setCurrentWidget(child)

