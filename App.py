import sys
from PyQt5.QtWidgets import QApplication
from Model.UserAccountModel import Model
from Controllers.LoginController import LoginController
from Views.MainView import MainView
from Views.LoginView import LoginView
from qt_material import apply_stylesheet

#App Class is the main class of the application
class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        self._model = Model()
        self._mainView = MainView()

        self._loginController = LoginController(self._model) 
        self._loginView = LoginView(self._model, self._loginController)
        
        apply_stylesheet(self._loginView, theme='dark_cyan.xml')

        self._mainView.setScreen(self._loginView)
        self._mainView.show()

        

if __name__ == '__main__':
    app = App(sys.argv)
    sys.exit(app.exec_())

