from PyQt5.QtWidgets import QWidget, QSizePolicy, QInputDialog, QLineEdit
from PyQt5.QtCore import pyqtSlot
from Views.BookStudentViewUI import Ui_Book
from Controllers.UsersController import UsersController
from Model.UserModel import UserModel
from datetime import timedelta, date

#BookView class communicates with UI that connects to a controller to perform backend operations
from PyQt5 import QtCore, QtGui, QtWidgets

class BookStudentView(QWidget):
    def __init__(self, bookModel, book_controller, issuance_model, issuance_controller):
        super().__init__()

        self._book_model = bookModel
        self._issuance_model = issuance_model
        self._book_controller = book_controller
        self._issuance_controller = issuance_controller
        self._ui = Ui_Book()
        self._ui.setupUi(self)
        self._ui.BookId.setText(self._book_model.book_id)
        self._ui.BookId.hide()
        self._ui.BookTitle.setText(self._book_model.title)
        self._ui.BookAuthor.setText(self._book_model.author)
        self._ui.BookPublisher.setText(self._book_model.publisher)
        self._ui.BookEdition.setText(self._book_model.edition)
        self._ui.BookCategory.setText(self._book_model.category)
        self._ui.BookPublisherDate.setText(self._book_model.published_date)
        self._ui.BookQuantity.setText(self._book_model.quantity)

        self._userModel = UserModel()
        self._usersController = UsersController(self._userModel)
    
    def GetAllStudentID(self):
        items = self._usersController.GetAllStudent()
        item, okPressed = QInputDialog.getItem(self, "Enter Student ID","Student ID:", items, 0, True)
        if okPressed and item:
            today = date.today()
            due_date = today + timedelta(days=7)
            self._issuance_controller.change_student_id(str(item))
            self._issuance_controller.change_release_date(str(today))
            self._issuance_controller.change_due_date(str(due_date))
            self._issuance_controller.change_book_id(str(self._ui.BookId.text()))
            items = self._usersController.GetAllStaff()
            item, okPressed = QInputDialog.getItem(self, "Enter Staff ID","Staff ID:", items, 0, True)
            if okPressed and item:
                self._issuance_controller.change_staff_id(str(item))
                self._issuance_controller.BorrowBook()
                self._book_controller.change_book_id(str(self._ui.BookId.text()))
                self._book_controller.ReleaseBook()

