from PyQt5.QtCore import QObject, pyqtSlot
from Controllers.DatabaseController import DatabaseController

#User controller contains all the properties of the user/student and perform database operations for the user such as add the user to the database
class UsersController(QObject):
    def __init__(self, model):
        super().__init__()
        self._model = model
        self._database_controller = DatabaseController()

    @pyqtSlot(str)
    def change_password(self, value):
        self._model.password = value

    @pyqtSlot(str)
    def change_student_id(self, value):
        self._model.student_id = value

    @pyqtSlot(str)
    def change_first_name(self, value):
        self._model.first_name = value

    @pyqtSlot(str)
    def change_last_name(self, value):
        self._model.last_name = value

    @pyqtSlot(str)
    def change_middle_name(self, value):
        self._model.middle_name = value

    @pyqtSlot(str)
    def change_email_address(self, value):
        self._model.email_address = value

    @pyqtSlot(str)
    def change_contact_number(self, value):
        self._model.contact_number = value

    @pyqtSlot(bool)
    def add(self, value):
        self._model.is_add_click = True if value else False

    @pyqtSlot(bool)
    def clear(self, value):
        self._model.is_clear_click = True if value else False

    
    def AddUser(self):
        try:
            mycursor = self._database_controller.Cursor()
            sql = "INSERT INTO student (student_id, first_name, last_name, middle_name, email_address, contact_number) VALUES (%s, %s, %s, %s, %s, %s)"
            val = (
                self._model.student_id, 
                self._model.first_name, 
                self._model.last_name, 
                self._model.middle_name, 
                self._model.email_address, 
                self._model.contact_number
            )
            mycursor.execute(sql, val)
            self._database_controller.Commit()
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
        finally:
            return mycursor.rowcount, "record inserted."

    def AddUserAccount(self):
        try:
            mycursor = self._database_controller.Cursor()
            sql = "INSERT INTO user_account (username, student_id, pass_word, role_id) VALUES (%s, %s, %s, %s)"
            val = (
                self._model.student_id, 
                self._model.student_id,
                self._model.password, 
                '1'
            )
            mycursor.execute(sql, val)
            self._database_controller.Commit() 
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
        finally:
            self._database_controller.Close()
            return mycursor.rowcount, "record inserted."

    def Clear(self):
        self._model.student_id = ''
        self._model.first_name = ''
        self._model.last_name = ''
        self._model.middle_name = ''
        self._model.email_address =''
        self._model.contact_number = ''
        self._model.password = ''

    def GetAllStudent(self):
        try:
            mycursor = self._database_controller.CursorTuple()
            mycursor.execute("SELECT student_id FROM user_account WHERE role_id = 1")
            myresult = mycursor.fetchall()
            studentIDs = ()
            for index, studentId in enumerate(myresult):
                studentIDs += (str(studentId[0]),)
                
            return studentIDs
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
        finally:
            self._database_controller.Close()

    def GetAllStaff(self):
        try:
            mycursor = self._database_controller.CursorTuple()
            mycursor.execute("SELECT staff_id FROM user_account WHERE role_id = 0")
            myresult = mycursor.fetchall()
            studentIDs = ()
            for index, studentId in enumerate(myresult):
                studentIDs += (str(studentId[0]),)
                
            return studentIDs
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
        finally:
            self._database_controller.Close()
        

        

