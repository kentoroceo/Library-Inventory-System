from PyQt5.QtCore import QObject, pyqtSlot
from Views.BookView import BookView
from Controllers.BookController import BookController

class LibraryController(QObject):

    def __init__(self, model):
        super().__init__()
        self._model = model
        self._bookView = []
        self._bookController = []

    def GetAllBooks(self):
        self.books = [
            {
            "title": "Game of Thrones Season 1",
            "author": "ewan",
            },
            {
            "title": "Game of Thrones Season 2",
            "author": "ewan",
            },
            {
            "title": "Game of Thrones Season 2",
            "author": "ewan",
            },
            {
            "title": "Game of Thrones Season 2",
            "author": "ewan",
            },
            {
            "title": "Game of Thrones Season 2",
            "author": "ewan",
            },
            {
            "title": "Game of Thrones Season 1",
            "author": "ewan",
            },
            {
            "title": "Game of Thrones Season 2",
            "author": "ewan",
            },
            {
            "title": "Game of Thrones Season 2",
            "author": "ewan",
            },
            {
            "title": "Game of Thrones Season 2",
            "author": "ewan",
            },
            {
            "title": "Game of Thrones Season 2",
            "author": "ewan",
            },
        ]

        for index, book in enumerate(self.books):
            #print(index, book)
            self._bookController.append(BookController(self._model))
            self._bookView.append(BookView(self._model, self._bookController))

        return self._bookView
    
