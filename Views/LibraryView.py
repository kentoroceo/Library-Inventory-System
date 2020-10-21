from PyQt5.QtWidgets import QWidget, QSizePolicy
from PyQt5.QtCore import pyqtSlot
from Views.LibraryViewUI import Ui_Library

from PyQt5 import QtCore, QtGui, QtWidgets

class LibraryView(QWidget):
    def __init__(self, model, library_controller):
        super().__init__()

        self._model = model
        self._library_controller = library_controller
        self._ui = Ui_Library()
        self._ui.setupUi(self)
        self.InitializeLibrary()
        
    def InitializeLibrary(self):
        self._allBooks = self._library_controller.GetAllBooks()
        self._row = 0
        self._col = 0

        for index, book in enumerate(self._allBooks):
            #print(index, book)
            if(index % 4 == 0):
                self._row = self._row + 1
                self._col = 0

            self._ui.gridLayout.addWidget(book, self._row, self._col)
            self._col = self._col + 1
            print(self._row, self._col)
        

