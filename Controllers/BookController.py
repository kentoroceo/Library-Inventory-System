from PyQt5.QtCore import QObject, pyqtSlot
from Controllers.DatabaseController import DatabaseController
#BookController contains the book properties and performs database operations for the book
class BookController(QObject):

    def __init__(self, model):
        super().__init__()
        self._model = model
        self._database_controller = DatabaseController()

    @pyqtSlot(str)
    def change_book_id(self, value):
        self._model.book_id = value

    @pyqtSlot(str)
    def change_title(self, value):
        self._model.title = value

    @pyqtSlot(str)
    def change_author(self, value):
        self._model.author = value

    @pyqtSlot(str)
    def change_publisher(self, value):
        self._model.publisher = value

    @pyqtSlot(str)
    def change_edition(self, value):
        self._model.edition = value

    @pyqtSlot(str)
    def change_category(self, value):
        self._model.category = value

    def change_published_date(self, value):
        self._model.published_date = '{0}/{1}/{2}'.format(value.year(), value.month(), value.day())

    @pyqtSlot(str)
    def change_quantity(self, value):
        self._model.quantity = value

    @pyqtSlot(bool)
    def add(self, value):
        self._model.is_add_click = True if value else False

    @pyqtSlot(bool)
    def clear(self, value):
        self._model.is_clear_click = True if value else False

    def AddBook(self):
        try:
            #print("AddBook")
            mycursor = self._database_controller.Cursor()
            sql = "INSERT INTO book (book_id, title, author, publisher, edition, category, published_date) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            val = (
                self._model.book_id, 
                self._model.title, 
                self._model.author, 
                self._model.publisher, 
                self._model.edition, 
                self._model.category,
                self._model.published_date
            )
            mycursor.execute(sql, val)
            self._database_controller.Commit()
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
        finally:
            self._database_controller.Close()
            return mycursor.rowcount, "record inserted."
    
    def AddInventory(self):
        try:
            mycursor = self._database_controller.Cursor()
            sql = "INSERT INTO inventory (book_id, quantity, stock, outbook) VALUES (%s, %s, %s, %s)"
            val = (
                self._model.book_id, 
                self._model.quantity, 
                self._model.quantity, 
                '0'
            )
            mycursor.execute(sql, val)
            self._database_controller.Commit()
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
        finally:
            self._database_controller.Close()
            return mycursor.rowcount, "record inserted."

    def ReleaseBook(self):
        try:
            self.stock = self.GetBookStock(self._model.book_id)
            self.outbook = self.GetOutbook(self._model.book_id)
            mycursor = self._database_controller.Cursor()
            sql = "UPDATE inventory SET stock = %s, outbook = %s WHERE book_id = %s"
            val = (
                self.stock - 1,
                self.outbook + 1,
                self._model.book_id
            )
            mycursor.execute(sql, val)
            self._database_controller.Commit()
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
        finally:
            self._database_controller.Close()
            return mycursor.rowcount, "record inserted."

    def ReturnBook(self):
        try:
            self.stock = self.GetBookStock(self._model.book_id)
            self.outbook = self.GetOutbook(self._model.book_id)
            mycursor = self._database_controller.Cursor()
            sql = "UPDATE inventory SET stock = %s, outbook = %s WHERE book_id = %s"
            val = (
                self.stock + 1,
                self.outbook - 1,
                self._model.book_id
            )
            mycursor.execute(sql, val)
            self._database_controller.Commit()
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
        finally:
            self._database_controller.Close()
            return mycursor.rowcount, "record inserted."

    def GetBookStock(self, book_id):
        self._book_id = book_id
        try:
            mycursor = self._database_controller.Cursor()
            mycursor.execute("SELECT stock FROM inventory WHERE book_id = " + self._book_id + "")
            myresult = mycursor.fetchall()
            return myresult[0]['stock']
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
        finally:
            self._database_controller.Close()

    def GetOutbook(self, book_id):
        self._book_id = book_id
        try:
            mycursor = self._database_controller.Cursor()
            mycursor.execute("SELECT outbook FROM inventory WHERE book_id = " + self._book_id + "")
            myresult = mycursor.fetchall()
            return myresult[0]['outbook']
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
        finally:
            self._database_controller.Close()

    def Clear(self):
        self._model.book_id = ''
        self._model.title = ''
        self._model.author = ''
        self._model.publisher = ''
        self._model.edition =''
        self._model.category = ''
        self._model.quantity = ''
