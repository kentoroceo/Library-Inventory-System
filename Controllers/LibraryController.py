from PyQt5.QtCore import QObject, pyqtSlot
from Controllers.BookController import BookController
from Model.BookModel import BookModel
from Controllers.DatabaseController import DatabaseController

#Library Controller class performs a database operation for getting all the books in the library
class LibraryController(QObject):

    def __init__(self):
        super().__init__()
        self._database_controller = DatabaseController()

    def GetAllBooks(self, sortBy):
        try:
            mycursor = self._database_controller.Cursor()
            mycursor.execute("SELECT book.book_id, book.title, book.author, book.publisher, book.edition, book.category, book.published_date, inventory.book_id, inventory.stock FROM book INNER JOIN inventory ON book.book_id = inventory.book_id WHERE inventory.stock != 0 ORDER BY book." + sortBy + "")
            books = mycursor.fetchall()
            return books
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
        finally:
            self._database_controller.Close()

            
    
