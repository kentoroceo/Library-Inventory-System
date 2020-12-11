from PyQt5.QtWidgets import QWidget, QSizePolicy
from PyQt5.QtCore import pyqtSlot
from Views.LibraryStudentViewUI import Ui_Library
from Controllers.BookController import BookController
from Model.BookModel import BookModel
from Model.IssuanceModel import IssuanceModel
from Views.BookStudentView import BookStudentView

from PyQt5 import QtCore, QtGui, QtWidgets

#Library View class communicates with UI that connects to a controller to perform backend operations
class LibraryStudentView(QWidget):
    def __init__(self, library_controller, issuance_controller, book_controller):
        super().__init__()

        self._ui = Ui_Library()
        self._ui.setupUi(self)
        self._library_controller = library_controller
        self._issuance_controller = issuance_controller
        self._book_controller = book_controller
        self._bookView = []
        self._ui.SearchLineEdit.hide()
        #self._ui.ComboBox.addItem("book_id") 
        self._ui.ComboBox.addItem("title") 
        self._ui.ComboBox.addItem("author") 
        self._ui.ComboBox.addItem("publisher") 
        self._ui.ComboBox.addItem("edition") 
        self._ui.ComboBox.addItem("category") 
        #self._ui.ComboBox.addItem("published_date") 
        self._ui.ComboBox.currentTextChanged.connect(self.on_combobox_changed)
        self._sortyBy = 'book_id'
    
    def GoToAddBookView(self):
        self.parent().setCurrentIndex(7)
        
    def InitializeLibrary(self):
        self._bookView = []
        self._bookView.clear()
        self.clearLibrary()
        self._allBooks = self._library_controller.GetAllBooks(self._sortyBy)
        self._row = 0
        self._col = 0

        for index, book in enumerate(self._allBooks):
            self._bookModel = BookModel()
            self._bookModel.book_id = str(book['book_id'])
            self._bookModel.title = book['title']
            self._bookModel.author = book['author']
            self._bookModel.publisher = book['publisher']
            self._bookModel.edition = book['edition']
            self._bookModel.category = book['category']
            self._bookModel.published_date = book['published_date'].strftime("%d-%m-%Y")
            self._bookModel.quantity = str(book['stock'])

            self._issuance_model = IssuanceModel()
            self._issuance_controller.change_book_id(str(book['book_id']))
            self._bookView.append(BookStudentView(self._bookModel, self._book_controller, self._issuance_model, self._issuance_controller))

        for index, book in enumerate(self._bookView):
            #print(index, book)
            if(index % 4 == 0):
                self._row = self._row + 1
                self._col = 0

            self._ui.gridLayout.addWidget(book, self._row, self._col)
            self._col = self._col + 1

    def AddBookView(self):
        return self._addBookView
        
    def clearLibrary(self):
        for i in reversed(range(self._ui.gridLayout.count())): 
            self._ui.gridLayout.itemAt(i).widget().setParent(None)

    def on_combobox_changed(self, value):
        self._sortyBy = value
        self.InitializeLibrary()
        #print("combobox changed", value)

