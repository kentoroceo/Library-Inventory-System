from PyQt5.QtCore import QObject, pyqtSlot
from Controllers.BookController import BookController
from Model.BookModel import BookModel
from Controllers.DatabaseController import DatabaseController

#Issuance Controller class contains the issuance properties and performs database operations for the issuance
class IssuanceController(QObject):

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
    def change_release_date(self, value):
        self._model.release_date = value

    @pyqtSlot(str)
    def change_due_date(self, value):
        self._model.due_date = value

    @pyqtSlot(bool)
    def add(self, value):
        self._model.is_add_click = True if value else False

    def GetIssuedBooks(self):
        try:
            mycursor = self._database_controller.CursorTuple()
            mycursor.execute(mycursor.execute("SELECT issuance_id, CONCAT(student.first_name, ' ', student.middle_name, ' ', student.last_name) AS full_name, student.student_id, book.title, issuance.book_id, issuance.release_date, issuance.due_date, CONCAT(staff.first_name, ' ', staff.middle_name, ' ', staff.last_name) AS staff_name FROM issuance LEFT JOIN book ON book.book_id = issuance.book_id LEFT JOIN student ON student.student_id = issuance.student_id LEFT JOIN staff ON staff.staff_id = issuance.staff_id WHERE issuance.is_returned = 0"))
            books = mycursor.fetchall()
            return books
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
        finally:
            self._database_controller.Close()

    def BorrowBook(self):
        try:
            mycursor = self._database_controller.Cursor()
            sql = "INSERT INTO issuance (student_id, staff_id, book_id, release_date, due_date, is_returned) VALUES (%s, %s, %s, %s, %s, %s)"
            val = (
                self._model.student_id, 
                self._model.staff_id, 
                self._model.book_id, 
                self._model.release_date, 
                self._model.due_date,
                '0', 
            )
            mycursor.execute(sql, val)
            self._database_controller.Commit()
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
        finally:
            self._database_controller.Close()
            return mycursor.rowcount, "record inserted."

    def UpdateIssuance(self):
        try:
            mycursor = self._database_controller.Cursor()
            sql = "UPDATE issuance SET is_returned = 1 WHERE issuance_id = %s"
            val = (
                self._model.issuance_id,
            )
            mycursor.execute(sql, val)
            self._database_controller.Commit()
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
        finally:
            self._database_controller.Close()
            return mycursor.rowcount, "record inserted."
