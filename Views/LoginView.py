from PyQt5.QtWidgets import QMainWindow, QWidget
from PyQt5.QtCore import pyqtSlot
from Views.LoginViewUI import Ui_Login


class LoginView(QWidget):
    def __init__(self, navigation_view, model, login_controller):
        super().__init__()

        self._model = model
        self._login_controller = login_controller
        self._ui = Ui_Login()
        self._ui.setupUi(self)
        self._navigation_view = navigation_view

        # connect widgets to controller
        self._ui.UsernameLineEdit.textChanged.connect(self._login_controller.change_username)
        self._ui.LoginButton.clicked.connect(lambda: self._login_controller.login(True))

        # listen for model event signals
        self._model.login_button_clicked.connect(self.on_login_button_clicked)
        self._model.username_changed.connect(self.on_username_changed)
        self._model.password_changed.connect(self.on_password_changed)

        # set a default value
        #self._login_controller.change_username("hello")


    #@pyqtSlot(int)
    #def on_login_button_clicked(self, value):
    #    self._ui.spinBox_amount.setValue(value)

    #@pyqtSlot(str)
    #def on_even_odd_changed(self, value):
    #    self._ui.label_even_odd.setText(value)

    @pyqtSlot(bool)
    def on_login_button_clicked(self, value):
        self.parent().parent().parent().setScreen(self._navigation_view)

    @pyqtSlot(str)
    def on_username_changed(self, value):
        self._ui.UsernameLineEdit.setText(value)   

    @pyqtSlot(str)
    def on_password_changed(self, value):
        self._ui.PasswordLineEdit.setText(value) 

