from PyQt5.QtWidgets import QWidget, QSizePolicy
from PyQt5.QtCore import pyqtSlot
from Views.BookViewUI import Ui_Book

from PyQt5 import QtCore, QtGui, QtWidgets

class BookView(QWidget):
    def __init__(self, model, book_controller):
        super().__init__()

        self._model = model
        self._book_controller = book_controller
        self._ui = Ui_Book()
        self._ui.setupUi(self)
        

