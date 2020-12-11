from PyQt5.QtCore import QObject, pyqtSignal

#Book Model class contains properties of the book such as book id, author, etc
class BookModel(QObject):

    book_id_changed = pyqtSignal(str)
    title_changed = pyqtSignal(str)
    author_changed = pyqtSignal(str)
    publisher_changed = pyqtSignal(str)
    edition_changed = pyqtSignal(str)
    category_changed = pyqtSignal(str)
    published_date_changed = pyqtSignal(str)
    inventory_id_changed = pyqtSignal(str)
    quantity_changed = pyqtSignal(str)
    stock_changed = pyqtSignal(str)
    outbook_changed = pyqtSignal(str)
    add_button_clicked = pyqtSignal(bool)
    clear_button_clicked = pyqtSignal(bool)


    @property
    def book_id(self):
        return self._book_id

    @book_id.setter
    def book_id(self, value):
        self._book_id = value
        self.book_id_changed.emit(value)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
        self.title_changed.emit(value)

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        self._author = value
        self.author_changed.emit(value)

    @property
    def publisher(self):
        return self._publisher

    @publisher.setter
    def publisher(self, value):
        self._publisher = value
        self.publisher_changed.emit(value)

    @property
    def edition(self):
        return self._edition

    @edition.setter
    def edition(self, value):
        self._edition = value
        self.edition_changed.emit(value)

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        self._category = value
        self.category_changed.emit(value)

    @property
    def published_date(self):
        return self._published_date

    @published_date.setter
    def published_date(self, value):
        self._published_date = value
        self.published_date_changed.emit(value)

    @property
    def inventory_id(self):
        return self._inventory_id

    @inventory_id.setter
    def inventory_id(self, value):
        self._inventory_id = value
        self.inventory_id_changed.emit(value)

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value
        self.quantity_changed.emit(value)

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, value):
        self._stock = value
        self.stock_changed.emit(value)

    @property
    def outbook(self):
        return self._stock

    @outbook.setter
    def outbook(self, value):
        self._outbook = value
        self.outbook_changed.emit(value)

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

        self._book_id = ''
        self._title = ''
        self._author = ''
        self._publisher = ''
        self._edition = ''
        self._category = ''
        self._published_date = ''
        self._stock = ''
        self._quantity = ''
        self._outbook = ''
        self._inventory_id = ''


