from PyQt5.QtCore import QObject, pyqtSlot


class LoginController(QObject):
    def __init__(self, model):
        super().__init__()
        self._model = model

    @pyqtSlot(bool)
    def login(self, value):
        self._model.is_login_click = True if value else False

    @pyqtSlot(str)
    def change_username(self, value):
        self._model.username = value


    

