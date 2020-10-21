from PyQt5.QtCore import QObject, pyqtSignal

class Model(QObject):
    username_changed = pyqtSignal(str)
    password_changed = pyqtSignal(str)
    login_button_clicked = pyqtSignal(bool)

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        self._username = value
        self.username_changed.emit(value)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value
        self.password_changed.emit(value)

    @property
    def is_login_click(self):
        return self._is_login_click

    @is_login_click.setter
    def is_login_click(self, value):
        self._is_login_click = value
        self.login_button_clicked.emit(value)

    def __init__(self):
        super().__init__()

        self._username = ''
        self._password = ''
        self._is_login_click = False


