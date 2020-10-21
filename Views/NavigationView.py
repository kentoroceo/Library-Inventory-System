from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QWidget
from PyQt5.QtCore import pyqtSlot, QPropertyAnimation 
from Views.NavigationViewUI import Ui_Navigation

class NavigationView(QWidget):
    def __init__(self, library_view, model, navigation_controller):
        super().__init__()

        self._model = model
        self._navigation_controller = navigation_controller
        self._ui = Ui_Navigation()
        self._ui.setupUi(self)
        self._library_view = library_view
        self._ui.stackedWidget.addWidget(self._library_view)

        ## TOGGLE/BURGUER MENU
        ########################################################################
        self._ui.Btn_Toggle.clicked.connect(lambda: self.toggleMenu(250, True))

        ## PAGES
        ########################################################################

        # PAGE 1
        self._ui.btn_page_1.clicked.connect(lambda: self._ui.stackedWidget.setCurrentWidget(self._library_view))

        # PAGE 2
        self._ui.btn_page_2.clicked.connect(lambda: self._ui.stackedWidget.setCurrentWidget(self._ui.page_2))

        # PAGE 3
        self._ui.btn_page_3.clicked.connect(lambda: self._ui.stackedWidget.setCurrentWidget(self._ui.page_3))

    def toggleMenu(self, maxWidth, enable):
        if enable:

            width = self._ui.frame_left_menu.width()
            maxExtend = maxWidth
            standard = 70

            if width == 70:
                widthExtended = maxExtend
            else:
                widthExtended = standard

            self.animation = QPropertyAnimation(self._ui.frame_left_menu, b"minimumWidth")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()