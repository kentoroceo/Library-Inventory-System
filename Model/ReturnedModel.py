from PyQt5.QtCore import QObject, pyqtSignal

#Return Model class contains the properties of the returned books
class ReturnedModel(QObject):
    return_id_changed = pyqtSignal(str)
    issuance_id_changed = pyqtSignal(str)
    student_id_changed = pyqtSignal(str)
    staff_id_changed = pyqtSignal(str)
    book_id_changed = pyqtSignal(str)
    return_date_changed = pyqtSignal(str)
    fine_changed = pyqtSignal(str)

    add_button_clicked = pyqtSignal(bool)

    @property
    def return_id(self):
        return self._return_id

    @return_id.setter
    def return_id(self, value):
        self._return_id = value
        self.return_id_changed.emit(value)

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
    def return_date(self):
        return self._return_date

    @return_date.setter
    def return_date(self, value):
        self._return_date = value
        self.return_date_changed.emit(value)

    @property
    def fine(self):
        return self._fine

    @fine.setter
    def fine(self, value):
        self._fine = value
        self.fine_changed.emit(value)

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
        self._return_date = ''
        self._fine = ''

        self._is_add_click = False


