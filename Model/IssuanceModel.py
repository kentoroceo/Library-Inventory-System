from PyQt5.QtCore import QObject, pyqtSignal

#Issuance Model class contains the properties of the issuance
class IssuanceModel(QObject):
    issuance_id_changed = pyqtSignal(str)
    student_id_changed = pyqtSignal(str)
    staff_id_changed = pyqtSignal(str)
    book_id_changed = pyqtSignal(str)
    release_date_changed = pyqtSignal(str)
    due_date_changed = pyqtSignal(str)

    add_button_clicked = pyqtSignal(bool)

    @property
    def issuance_id(self):
        return self._issuance_id

    @issuance_id.setter
    def issuance_id(self, value):
        self._issuance_id = value
        self.issuance_id_changed.emit(value)

    @property
    def student_id(self):
        return self._student_id

    @student_id.setter
    def student_id(self, value):
        self._student_id = value
        self.student_id_changed.emit(value)

    @property
    def staff_id(self):
        return self._staff_id

    @staff_id.setter
    def staff_id(self, value):
        self._staff_id = value
        self.staff_id_changed.emit(value)
    
    @property
    def book_id(self):
        return self._book_id

    @book_id.setter
    def book_id(self, value):
        self._book_id = value
        self.book_id_changed.emit(value)
    
    @property
    def release_date(self):
        return self._release_date

    @release_date.setter
    def release_date(self, value):
        self._release_date = value
        self.release_date_changed.emit(value)

    @property
    def due_date(self):
        return self._due_date

    @due_date.setter
    def due_date(self, value):
        self._due_date = value
        self.due_date_changed.emit(value)

    @property
    def is_add_click(self):
        return self._is_add_click

    @is_add_click.setter
    def is_add_click(self, value):
        self._is_add_click = value
        self.add_button_clicked.emit(value)

    def __init__(self):
        super().__init__()

        self._issuance_id = ''
        self._student_id = ''
        self._staff_id = ''
        self._book_id = ''
        self._release_date = ''
        self._due_date = ''

        self._is_add_click = False


