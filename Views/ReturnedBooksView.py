from PyQt5.QtWidgets import QWidget, QSizePolicy, QTableWidgetItem, QMessageBox
from PyQt5.QtCore import pyqtSlot
from Views.ReturnedBooksViewUI import Ui_ReturnedBooks
from Controllers.BookController import BookController
from Model.BookModel import BookModel
from Views.BookView import BookView
from datetime import timedelta, date


from PyQt5 import QtCore, QtGui, QtWidgets

#ReturnedBooksView class communicates with UI that connects to a controller to perform backend operations
class ReturnedBooksView(QWidget):
    def __init__(self, return_books_controller):
        super().__init__()

        self._ui = Ui_ReturnedBooks()
        self._ui.setupUi(self)
        self._return_books_controller = return_books_controller
        columns = ['Issuance ID', 'Borrowed by', 'Book Title', 'Book Id', 'Returned Date', 'Librarian', 'Fine']
        self._ui.tableWidget.setHorizontalHeaderLabels(columns)
        self._ui.tableWidget.resizeColumnsToContents()
        self._ui.lineEdit.hide()
        
    def InitializeReturnedBooks(self):
        self._returnedBooks = self._return_books_controller.GetReturnedBooks()
        self._ui.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(self._returnedBooks):
            self._ui.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self._ui.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))



