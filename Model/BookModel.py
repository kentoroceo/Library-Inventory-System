from PyQt5.QtCore import QObject, pyqtSignal

class BookModel(QObject):

    title_changed = pyqtSignal(str)
    author_changed = pyqtSignal(str)
    login_button_clicked = pyqtSignal(bool)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
        self.title_changed.emit(value)

    @property
    def author(self):
        return self._author

    @author.setter
    def password(self, value):
        self._author = value
        self.author_changed.emit(value)

    def __init__(self):
        super().__init__()

        self._title = ''
        self._author = ''


