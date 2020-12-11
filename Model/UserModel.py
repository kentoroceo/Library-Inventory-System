from PyQt5.QtCore import QObject, pyqtSignal

#UserMOdel class contains all the properties of the student
class UserModel(QObject):
    student_id_changed = pyqtSignal(str)
    first_name_changed = pyqtSignal(str)
    last_name_changed = pyqtSignal(str)
    middle_name_changed = pyqtSignal(str)
    email_address_changed = pyqtSignal(str)
    contact_number_changed = pyqtSignal(str)
    password_changed = pyqtSignal(str)
    add_button_clicked = pyqtSignal(bool)
    clear_button_clicked = pyqtSignal(bool)

    @property
    def student_id(self):
        return self._student_id

    @student_id.setter
    def student_id(self, value):
        self._student_id = value
        self.student_id_changed.emit(value)

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value
        self.first_name_changed.emit(value)

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value
        self.last_name_changed.emit(value)
    
    @property
    def middle_name(self):
        return self._middle_name

    @middle_name.setter
    def middle_name(self, value):
        self._middle_name = value
        self.middle_name_changed.emit(value)
    
    @property
    def email_address(self):
        return self._email_address

    @email_address.setter
    def email_address(self, value):
        self._email_address = value
        self.email_address_changed.emit(value)

    @property
    def contact_number(self):
        return self._contact_number

    @contact_number.setter
    def contact_number(self, value):
        self._contact_number = value
        self.contact_number_changed.emit(value)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value
        self.password_changed.emit(value)

    @property
    def is_add_click(self):
        return self._is_add_click

    @is_add_click.setter
    def is_add_click(self, value):
        self._is_add_click = value
        self.add_button_clicked.emit(value)

    @property
    def is_clear_click(self):
        return self._is_clear_click

    @is_clear_click.setter
    def is_clear_click(self, value):
        self._is_clear_click = value
        self.clear_button_clicked.emit(value)

    def __init__(self):
        super().__init__()

        self._student_id = ''
        self._first_name = ''
        self._last_name = ''
        self._middle_name = ''
        self._email_address = ''
        self._contact_number = ''
        self._password = ''
        self._is_add_click = False
        self._is_clear_click = False


