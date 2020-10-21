from PyQt5.QtWidgets import QMainWindow, QSizePolicy
from PyQt5.QtCore import pyqtSlot
from Views.MainViewUI import Ui_Main

from PyQt5 import QtCore, QtGui, QtWidgets

class MainView(QMainWindow):
    def __init__(self, model, main_controller):
        super().__init__()

        self._model = model
        self._main_controller = main_controller
        self._ui = Ui_Main()
        self._ui.setupUi(self)
        

    def setScreen(self, child):
        self._ui.stackedWidget.addWidget(child)
        self._ui.stackedWidget.setCurrentWidget(child)

