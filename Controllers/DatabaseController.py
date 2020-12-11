import mysql.connector

#Database Controller the initializes the database connector to perform database operations
class DatabaseController():

    def __init__(self):
        super().__init__()
        
    def Cursor(self):
        self.dblibrary = mysql.connector.connect(
          host="localhost",
          user="root",
          password="",
          database="dblibrary"
        )
        mycursor = self.dblibrary.cursor(dictionary=True)
        return mycursor

    def CursorTuple(self):
        self.dblibrary = mysql.connector.connect(
          host="localhost",
          user="root",
          password="",
          database="dblibrary"
        )
        mycursor = self.dblibrary.cursor()
        return mycursor

    def Commit(self):
        self.dblibrary.commit()

    def Close(self):
        self.dblibrary.close()

    

   