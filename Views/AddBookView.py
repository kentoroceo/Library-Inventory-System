from PyQt5.QtWidgets import QWidget, QSizePolicy, QMessageBox
from PyQt5.QtCore import pyqtSlot
from Views.AddBookViewUI import Ui_AddBook

from PyQt5 import QtCore, QtGui, QtWidgets

#AddBookView class communicates with UI that connects to a controller to perform backend operations
class AddBookView(QWidget):
    def __init__(self, model, book_controller):
        super().__init__()

        self._model = model
        self._book_controller = book_controller
        self._ui = Ui_AddBook()
        self._ui.setupUi(self)

        # connect widgets to controller
        self._ui.BookIdLineEdit.textChanged.connect(self._book_controller.change_book_id)
        self._ui.BookTitleLineEdit.textChanged.connect(self._book_controller.change_title)
        self._ui.BookAuthorLineEdit.textChanged.connect(self._book_controller.change_author)
        self._ui.BookPublisherLineEdit.textChanged.connect(self._book_controller.change_publisher)
        self._ui.BookEditionLineEdit.textChanged.connect(self._book_controller.change_edition)
        self._ui.BookCategoryLineEdit.textChanged.connect(self._book_controller.change_category)
        self._ui.BookPublishedDate.dateChanged.connect(self._book_controller.change_published_date)
        self._ui.BookQuantityLineEdit.textChanged.connect(self._book_controller.change_quantity)

        self._ui.AddUserButton.clicked.connect(lambda: self._book_controller.add(True))
        self._ui.ClearButton.clicked.connect(lambda: self._book_controller.clear(True))

        # listen for model event signals
        self._model.book_id_changed.connect(self.on_book_id_changed)
        self._model.title_changed.connect(self.on_title_changed)
        self._model.author_changed.connect(self.on_author_changed)
        self._model.publisher_changed.connect(self.on_publisher_changed)
        self._model.edition_changed.connect(self.on_edition_changed)
        self._model.category_changed.connect(self.on_category_changed)
        self._model.quantity_changed.connect(self.on_quantity_changed)

        self._model.add_button_clicked.connect(self.on_add_button_clicked)
        self._model.clear_button_clicked.connect(self.on_clear_button_clicked)

        # set a default value
        #self._login_controller.change_username("hello")

    @pyqtSlot(bool)
    def on_add_button_clicked(self, value):
        if self._model.book_id != "" and  self._model.title != "" and self._model.author != "" and self._model.publisher != "" and self._model.edition != "" and self._model.category != "" and self._model.published_date != "" and self._model.quantity != "":
            self._book_controller.AddBook()
            self._book_controller.AddInventory()
            QMessageBox.information(self,"Information", "Book Successfully Added!")
            self._book_controller.Clear()
        else:
            QMessageBox.warning(self,"Warning", "All fields are required!")


    @pyqtSlot(bool)
    def on_clear_button_clicked(self, value):
        self._book_controller.Clear()

    @pyqtSlot(str)
    def on_book_id_changed(self, value):
        self._ui.BookIdLineEdit.setText(value)   

    @pyqtSlot(str)
    def on_title_changed(self, value):
        self._ui.BookTitleLineEdit.setText(value) 

    @pyqtSlot(str)
    def on_author_changed(self, value):
        self._ui.BookAuthorLineEdit.setText(value)   

    @pyqtSlot(str)
    def on_publisher_changed(self, value):
        self._ui.BookPublisherLineEdit.setText(value) 
    
    @pyqtSlot(str)
    def on_edition_changed(self, value):
        self._ui.BookEditionLineEdit.setText(value)   

    @pyqtSlot(str)
    def on_category_changed(self, value):
        self._ui.BookCategoryLineEdit.setText(value) 

    @pyqtSlot(str)
    def on_quantity_changed(self, value):
        self._ui.BookQuantityLineEdit.setText(value) 

    #def on_published_date_changed(self, value):
        #self._ui.BookPublishedDate.setText(value)

