import sys
from PyQt5.QtWidgets import QApplication
from Model.UserAccountModel import Model
from Model.BookModel import BookModel
from Controllers.LoginController import LoginController
from Controllers.MainController import MainController
from Controllers.NavigationController import NavigationController
from Controllers.LibraryController import LibraryController
from Views.MainView import MainView
from Views.LoginView import LoginView
from Views.NavigationView import NavigationView
from Views.LibraryView import LibraryView



class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        self._model = Model()
        self._mainController = MainController(self._model)
        self._mainView = MainView(self._model, self._mainController)

        self._bookModel = BookModel()
        self._libraryController = LibraryController(self._bookModel)
        self._libraryView = LibraryView(self._bookModel, self._libraryController)
   
        self._navigationController = NavigationController(self._model)
        self._navigationView = NavigationView(self._libraryView, self._model, self._navigationController)

        self._loginController = LoginController(self._model)
        self._loginView = LoginView(self._navigationView, self._model, self._loginController)
        
        self._mainView.setScreen(self._loginView)
        self._mainView.show()

        

if __name__ == '__main__':
    app = App(sys.argv)
    sys.exit(app.exec_())

