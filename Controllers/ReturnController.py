from PyQt5.QtCore import QObject, pyqtSlot
from Controllers.BookController import BookController
from Model.BookModel import BookModel
from Controllers.DatabaseController import DatabaseController

#Issuance Controller class contains the issuance properties and performs database operations for the issuance
class ReturnController(QObject):

    def __init__(self, model):
        super().__init__()
        self._database_controller = DatabaseController()
        self._model = model

    @pyqtSlot(str)
    def change_issuance_id(self, value):
        self._model.issuance_id = value

    @pyqtSlot(str)
    def change_student_id(self, value):
        self._model.student_id = value

    @pyqtSlot(str)
    def change_staff_id(self, value):
        self._model.staff_id = value

    @pyqtSlot(str)
    def change_book_id(self, value):
        self._model.book_id = value

    @pyqtSlot(str)
    def change_fine(self, value):
        self._model.fine = value

    @pyqtSlot(str)
    def change_return_date(self, value):
        self._model.return_date = value

    @pyqtSlot(bool)
    def add(self, value):
        self._model.is_add_click = True if value else False

    def GetReturnedBooks(self):
        try:
            mycursor = self._database_controller.CursorTuple()
            mycursor.execute(mycursor.execute("SELECT issuance_id, CONCAT(student.first_name, ' ', student.middle_name, ' ', student.last_name) AS full_name, book.title, return_book.book_id, return_book.return_date, CONCAT(staff.first_name, ' ', staff.middle_name, ' ', staff.last_name) AS staff_name, return_book.fine FROM return_book LEFT JOIN book ON book.book_id = return_book.book_id LEFT JOIN student ON student.student_id = return_book.student_id LEFT JOIN staff ON staff.staff_id = return_book.staff_id"))
            books = mycursor.fetchall()
            return books
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
        finally:
            self._database_controller.Close()

    def ReturnBook(self):
        try:
            mycursor = self._database_controller.Cursor()
            sql = "INSERT INTO return_book (issuance_id, staff_id, book_id, student_id, return_date, fine) VALUES (%s, %s, %s, %s, %s, %s);"
            val = (
                self._model.issuance_id,
                self._model.staff_id, 
                self._model.book_id, 
                self._model.student_id, 
                self._model.return_date, 
                self._model.fine, 
            )
            mycursor.execute(sql, val)
            self._database_controller.Commit()
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
        finally:
            self._database_controller.Close()
            return mycursor.rowcount, "record inserted."


