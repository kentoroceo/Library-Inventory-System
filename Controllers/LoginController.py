from PyQt5.QtCore import QObject, pyqtSlot
from Controllers.DatabaseController import DatabaseController

#Login Controller class performs a database operation for loging in the user and to check whether the credential exists or not
class LoginController(QObject):
    def __init__(self, model):
        super().__init__()
        self._model = model
        self._database_controller = DatabaseController()

    @pyqtSlot(bool)
    def login(self, value):
        self._model.is_login_click = True if value else False

    @pyqtSlot(str)
    def change_username(self, value):
        self._model.username = value

    @pyqtSlot(str)
    def change_password(self, value):
        self._model.password = value

    def Login(self):
        try:
            mycursor = self._database_controller.Cursor()
            mycursor.execute("SELECT * FROM user_account WHERE username = '" + self._model.username + "' and pass_word = '" + self._model.password + "' ")
            myresult = mycursor.fetchall()
            return myresult
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
        finally:
            self._database_controller.Close()


    

