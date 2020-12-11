from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QWidget
from PyQt5.QtCore import pyqtSlot, QPropertyAnimation 
from Views.NavigationStudentViewUI import Ui_Navigation
from Controllers.LibraryController import LibraryController
from Controllers.UsersController import UsersController
from Controllers.IssuanceController import IssuanceController
from Views.IssuedBooksStudentView import IssuedBooksStudentView
from Views.LibraryStudentView import LibraryStudentView
from Views.UsersView import UsersView
from Model.UserModel import UserModel
from Model.IssuanceModel import IssuanceModel
from Views.AddBookViewUI import Ui_AddBook
from Model.BookModel import BookModel
from Controllers.BookController import BookController
from Views.AddBookView import AddBookView
from Model.ReturnedModel import ReturnedModel
from Controllers.ReturnController import ReturnController
from Views.ReturnedBooksView import ReturnedBooksView
#NavigationView class communicates with UI that connects to a controller to perform backend operations
class NavigationStudentView(QWidget):
    def __init__(self):
        super().__init__()

        self._ui = Ui_Navigation()
        self._ui.setupUi(self)
        
        self._userModel = UserModel()
        self._usersController = UsersController(self._userModel)
        self._usersView = UsersView(self._userModel, self._usersController)
        self._ui.stackedWidget.addWidget(self._usersView)

        self._returnedModel = ReturnedModel()
        self._returned_controller = ReturnController(self._returnedModel)
        self._returnedBooksView = ReturnedBooksView(self._returned_controller)
        self._ui.stackedWidget.addWidget(self._returnedBooksView)

        self._issuanceModel = IssuanceModel()
        self._issuanceController = IssuanceController(self._issuanceModel)
        self._issuanceView = IssuedBooksStudentView(self._issuanceController, self._returned_controller)
        self._ui.stackedWidget.addWidget(self._issuanceView)

        self._bookModel = BookModel()
        self._bookController = BookController(self._bookModel)
        self._addBookView = AddBookView(self._bookModel, self._bookController)
        self._ui.stackedWidget.addWidget(self._addBookView)

        self._libraryController = LibraryController()
        self._libraryView = LibraryStudentView(self._libraryController, self._issuanceController, self._bookController)
        self._ui.stackedWidget.addWidget(self._libraryView)
        self._ui.stackedWidget.setCurrentWidget(self._libraryView)
        self._libraryView.InitializeLibrary()
        
    
        ## TOGGLE/BURGUER MENU
        self._ui.Btn_Toggle.clicked.connect(lambda: self.toggleMenu(70, True))

        ## PAGES
        self._ui.library_page.clicked.connect(lambda: self._ui.stackedWidget.setCurrentWidget(self._libraryView))
        self._ui.library_page.clicked.connect(self._libraryView.InitializeLibrary)

        self._ui.issued_books_page.clicked.connect(lambda: self._ui.stackedWidget.setCurrentWidget(self._issuanceView))
        self._ui.issued_books_page.clicked.connect(self._issuanceView.InitializeIssuedBooks)


    def toggleMenu(self, minWidth, enable):
        if enable:

            width = self._ui.frame_left_menu.width()
            minExtend = minWidth
            standard = 250

            if width == 250:
                widthExtended = minExtend
                self._ui.library_page.setText("")
                self._ui.issued_books_page.setText("")
            else:
                widthExtended = standard
                self._ui.library_page.setText("       Library          ")
                self._ui.issued_books_page.setText("       Issued Books")

            self.animation = QPropertyAnimation(self._ui.frame_left_menu, b"minimumWidth")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()
            

        