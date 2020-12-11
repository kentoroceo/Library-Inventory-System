from PyQt5.QtWidgets import QMainWindow, QWidget, QMessageBox
from PyQt5.QtCore import pyqtSlot
from Views.UsersViewUI import Ui_Users
#from Views.NavigationView import NavigationView

#UserView class communicates with UI that connects to a controller to perform backend operations
class UsersView(QWidget):
    
    def __init__(self, model, users_controller):
        super().__init__()

        self._model = model
        self._users_controller = users_controller
        self._ui = Ui_Users()
        self._ui.setupUi(self)

        # connect widgets to controller
        self._ui.StudentIdLineEdit.textChanged.connect(self._users_controller.change_student_id)
        self._ui.FirstNameLineEdit.textChanged.connect(self._users_controller.change_first_name)
        self._ui.LastNameLineEdit.textChanged.connect(self._users_controller.change_last_name)
        self._ui.MiddleNameLineEdit.textChanged.connect(self._users_controller.change_middle_name)
        self._ui.EmailAddressLineEdit.textChanged.connect(self._users_controller.change_email_address)
        self._ui.ContactNumberLineEdit.textChanged.connect(self._users_controller.change_contact_number)
        self._ui.PasswordLineEdit.textChanged.connect(self._users_controller.change_password)

        self._ui.AddUserButton.clicked.connect(lambda: self._users_controller.add(True))
        self._ui.ClearButton.clicked.connect(lambda: self._users_controller.clear(True))

        # listen for model event signals
        self._model.student_id_changed.connect(self.on_student_id_changed)
        self._model.first_name_changed.connect(self.on_first_name_changed)
        self._model.last_name_changed.connect(self.on_last_name_changed)
        self._model.middle_name_changed.connect(self.on_middle_name_changed)
        self._model.email_address_changed.connect(self.on_email_address_changed)
        self._model.contact_number_changed.connect(self.on_contact_number_changed)
        self._model.password_changed.connect(self.on_password_changed)

        self._model.add_button_clicked.connect(self.on_add_button_clicked)
        self._model.clear_button_clicked.connect(self.on_clear_button_clicked)

        # set a default value
        #self._login_controller.change_username("hello")

    @pyqtSlot(bool)
    def on_add_button_clicked(self, value):
        if self._model.student_id != "" and  self._model.first_name != "" and self._model.last_name != "" and self._model.middle_name != "" and self._model.email_address != "" and self._model.contact_number != "":
            self._users_controller.AddUser()
            self._users_controller.AddUserAccount()
            QMessageBox.information(self,"Information", "User Successfully Added!")
            self._users_controller.Clear()
        else:
            QMessageBox.warning(self,"Warning", "All fields are required!")


    @pyqtSlot(bool)
    def on_clear_button_clicked(self, value):
        self._users_controller.Clear()

    @pyqtSlot(str)
    def on_student_id_changed(self, value):
        self._ui.StudentIdLineEdit.setText(value)   

    @pyqtSlot(str)
    def on_first_name_changed(self, value):
        self._ui.FirstNameLineEdit.setText(value) 

    @pyqtSlot(str)
    def on_last_name_changed(self, value):
        self._ui.LastNameLineEdit.setText(value)   

    @pyqtSlot(str)
    def on_middle_name_changed(self, value):
        self._ui.MiddleNameLineEdit.setText(value) 
    
    @pyqtSlot(str)
    def on_email_address_changed(self, value):
        self._ui.EmailAddressLineEdit.setText(value)   

    @pyqtSlot(str)
    def on_contact_number_changed(self, value):
        self._ui.ContactNumberLineEdit.setText(value) 

    @pyqtSlot(str)
    def on_password_changed(self, value):
        self._ui.PasswordLineEdit.setText(value)
        
