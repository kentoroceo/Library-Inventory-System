from PyQt5.QtWidgets import QMainWindow, QWidget
from PyQt5.QtCore import pyqtSlot
from Views.LoginViewUI import Ui_Login
from Views.NavigationView import NavigationView
from Views.NavigationStudentView import NavigationStudentView
from qt_material import apply_stylesheet

#LoginView class communicates with UI that connects to a controller to perform backend operations
class LoginView(QWidget):
    def __init__(self, model, login_controller):
        super().__init__()

        self._model = model
        self._login_controller = login_controller
        self._ui = Ui_Login()
        self._ui.setupUi(self)

        self._navigationView = NavigationView()
        apply_stylesheet(self._navigationView, theme='dark_cyan.xml')

        self._navigationStudentView = NavigationStudentView()
        apply_stylesheet(self._navigationStudentView, theme='dark_cyan.xml')

        # connect widgets to controller
        self._ui.UsernameLineEdit.textChanged.connect(self._login_controller.change_username)
        self._ui.PasswordLineEdit.textChanged.connect(self._login_controller.change_password)
        self._ui.LoginButton.clicked.connect(lambda: self._login_controller.login(True))
        self._ui.label.hide()

        # listen for model event signals
        self._model.login_button_clicked.connect(self.on_login_button_clicked)
        self._model.username_changed.connect(self.on_username_changed)
        self._model.password_changed.connect(self.on_password_changed)

    @pyqtSlot(bool)
    def on_login_button_clicked(self, value):
        self.userInfo = self._login_controller.Login()
        if(len(self.userInfo) == 1):
            if(self.userInfo[0]['role_id'] == 0):
                self.parent().parent().parent().setScreen(self._navigationView)
            else:
                self.parent().parent().parent().setScreen(self._navigationStudentView)
        else:
            self._ui.label.show()

    @pyqtSlot(str)
    def on_username_changed(self, value):
        self._ui.UsernameLineEdit.setText(value)   
        self._ui.label.hide()

    @pyqtSlot(str)
    def on_password_changed(self, value):
        self._ui.PasswordLineEdit.setText(value) 
        self._ui.label.hide()

