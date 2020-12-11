from PyQt5.QtWidgets import QWidget, QSizePolicy, QTableWidgetItem, QMessageBox, QInputDialog
from PyQt5.QtCore import pyqtSlot
from Views.IssuedBooksStudentViewUI import Ui_IssuedBooks
from Controllers.BookController import BookController
from Controllers.UsersController import UsersController
from Model.UserModel import UserModel
from Model.BookModel import BookModel
from Views.BookView import BookView
from datetime import timedelta, date

from PyQt5 import QtCore, QtGui, QtWidgets

#IssuedBooksView class communicates with UI that connects to a controller to perform backend operations
class IssuedBooksStudentView(QWidget):
    def __init__(self, issuance_controller, returned_controller):
        super().__init__()

        self._ui = Ui_IssuedBooks()
        self._ui.setupUi(self)
        self._issuance_controller = issuance_controller
        self._returned_controller = returned_controller
        self._ui.lineEdit.hide()
        #self._ui.tableWidget.itemSelectionChanged.connect(self.GetSelectedIssuanceID)

        columns = ['Issuance ID', 'Borrowed by', 'Student ID', 'Book Title', 'Book Id', 'Release Date', 'Due Date', 'Librarian', 'Fine']
        self._ui.tableWidget.setHorizontalHeaderLabels(columns)
        self._ui.tableWidget.resizeColumnsToContents()

        self._userModel = UserModel()
        self._usersController = UsersController(self._userModel)

        self._bookModel = BookModel()
        self._bookController = BookController(self._bookModel)
        
        
    def InitializeIssuedBooks(self):
        self._issuedBooks = self._issuance_controller.GetIssuedBooks()
        if len(self._issuedBooks) == 0:
            self._ui.ReturnButton.setEnabled(False) 
            
        self._ui.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(self._issuedBooks):
            self._fine = self.ComputeFine(row_data[6])
            self._row_data_with_fine = list(row_data)
            self._row_data_with_fine.append(self._fine)
            self._row_data_with_fine = tuple(self._row_data_with_fine)
            self._ui.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(self._row_data_with_fine):
                self._ui.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
 
    def GetSelectedIssuanceID(self):
        self.items = self._ui.tableWidget.selectedItems()
        if len(self.items) > 0: 
            self._ui.ReturnButton.setEnabled(True) 
            self._issuance_id = str(self.items[0].text())
            self._student_id = str(self.items[2].text())
            self._book_title = str(self.items[3].text())
            self._book_id = str(self.items[4].text())
            self._fine= str(self.items[8].text())
        else:
            self._ui.ReturnButton.setEnabled(False) 

    def ReturnBook(self):
        buttonReply = QMessageBox.question(self, 'Confirmation', "Are you sure you want to return the book " + self._book_title + " with the Issuance ID of " + self._issuance_id + "?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            items = self._usersController.GetAllStaff()
            item, okPressed = QInputDialog.getItem(self, "Enter Staff ID","Staff ID:", items, 0, True)
            if okPressed and item:
                self._returned_controller.change_issuance_id(str(self._issuance_id))
                self._returned_controller.change_staff_id(str(item))
                self._returned_controller.change_book_id(str(self._book_id))
                self._returned_controller.change_student_id(str(self._student_id))
                self._returned_controller.change_return_date(str(date.today()))
                self._returned_controller.change_fine(str(self._fine))

                self._issuance_controller.UpdateIssuance()
               
                self._returned_controller.ReturnBook()
                self._bookController.change_book_id(str(self._book_id))
                self._bookController.ReturnBook()
                
            

    def ComputeFine(self, due_date):
        today = date.today()
        daysPastDueDate = today - due_date
        if(daysPastDueDate.days > 0):
            return daysPastDueDate.days * 10
        else:
            return 0
        



