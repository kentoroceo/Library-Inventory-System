# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Book.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Book(object):
    def setupUi(self, Book):
        Book.setObjectName("Book")
        Book.resize(250, 492)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Book.sizePolicy().hasHeightForWidth())
        Book.setSizePolicy(sizePolicy)
        Book.setStyleSheet("")
        self.gridLayout = QtWidgets.QGridLayout(Book)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(Book)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.PhotoContainer = QtWidgets.QFrame(self.frame)
        self.PhotoContainer.setStyleSheet("QFrame{\n"
"    border-style:none;\n"
"}")
        self.PhotoContainer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.PhotoContainer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.PhotoContainer.setObjectName("PhotoContainer")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.PhotoContainer)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.BookPhoto = QtWidgets.QLabel(self.PhotoContainer)
        self.BookPhoto.setText("")
        self.BookPhoto.setPixmap(QtGui.QPixmap("Resources/Images/NoImageAvailable.png"))
        self.BookPhoto.setScaledContents(True)
        self.BookPhoto.setObjectName("BookPhoto")
        self.gridLayout_2.addWidget(self.BookPhoto, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.PhotoContainer)
        self.BookDetails = QtWidgets.QFrame(self.frame)
        self.BookDetails.setStyleSheet("QLabel{\n"
"    color: white;\n"
"}\n"
"QFrame {\n"
"    border-style:none;\n"
"}")
        self.BookDetails.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.BookDetails.setFrameShadow(QtWidgets.QFrame.Raised)
        self.BookDetails.setObjectName("BookDetails")
        self.formLayout = QtWidgets.QFormLayout(self.BookDetails)
        self.formLayout.setObjectName("formLayout")
        self.TitleLabel = QtWidgets.QLabel(self.BookDetails)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.TitleLabel.setFont(font)
        self.TitleLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.TitleLabel.setObjectName("TitleLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.TitleLabel)
        self.BookTitle = QtWidgets.QLabel(self.BookDetails)
        self.BookTitle.setObjectName("BookTitle")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.BookTitle)
        self.AuthorLabell = QtWidgets.QLabel(self.BookDetails)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.AuthorLabell.setFont(font)
        self.AuthorLabell.setObjectName("AuthorLabell")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.AuthorLabell)
        self.BookAuthor = QtWidgets.QLabel(self.BookDetails)
        self.BookAuthor.setObjectName("BookAuthor")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.BookAuthor)
        self.PublisherLabel = QtWidgets.QLabel(self.BookDetails)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.PublisherLabel.setFont(font)
        self.PublisherLabel.setObjectName("PublisherLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.PublisherLabel)
        self.BookPublisher = QtWidgets.QLabel(self.BookDetails)
        self.BookPublisher.setObjectName("BookPublisher")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.BookPublisher)
        self.EditionLabel = QtWidgets.QLabel(self.BookDetails)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.EditionLabel.setFont(font)
        self.EditionLabel.setObjectName("EditionLabel")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.EditionLabel)
        self.BookEdition = QtWidgets.QLabel(self.BookDetails)
        self.BookEdition.setObjectName("BookEdition")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.BookEdition)
        self.CategoryLabel = QtWidgets.QLabel(self.BookDetails)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.CategoryLabel.setFont(font)
        self.CategoryLabel.setObjectName("CategoryLabel")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.CategoryLabel)
        self.BookCategory = QtWidgets.QLabel(self.BookDetails)
        self.BookCategory.setObjectName("BookCategory")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.BookCategory)
        self.PublishedDateLabel = QtWidgets.QLabel(self.BookDetails)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.PublishedDateLabel.setFont(font)
        self.PublishedDateLabel.setObjectName("PublishedDateLabel")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.PublishedDateLabel)
        self.BookPublisherDate = QtWidgets.QLabel(self.BookDetails)
        self.BookPublisherDate.setObjectName("BookPublisherDate")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.BookPublisherDate)
        self.StockLabel = QtWidgets.QLabel(self.BookDetails)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.StockLabel.setFont(font)
        self.StockLabel.setObjectName("StockLabel")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.StockLabel)
        self.BookQuantity = QtWidgets.QLabel(self.BookDetails)
        self.BookQuantity.setObjectName("BookQuantity")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.BookQuantity)
        self.BookId = QtWidgets.QLabel(self.BookDetails)
        self.BookId.setObjectName("BookId")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.BookId)
        self.verticalLayout.addWidget(self.BookDetails)
        self.ButtonContainer = QtWidgets.QFrame(self.frame)
        self.ButtonContainer.setStyleSheet("QFrame{\n"
"    border-style:none;\n"
"}")
        self.ButtonContainer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ButtonContainer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ButtonContainer.setObjectName("ButtonContainer")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.ButtonContainer)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setVerticalSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.BorrowButton = QtWidgets.QPushButton(self.ButtonContainer)
        self.BorrowButton.setStyleSheet("")
        self.BorrowButton.setObjectName("BorrowButton")
        self.gridLayout_3.addWidget(self.BorrowButton, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.ButtonContainer)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi(Book)
        QtCore.QMetaObject.connectSlotsByName(Book)

    def retranslateUi(self, Book):
        _translate = QtCore.QCoreApplication.translate
        Book.setWindowTitle(_translate("Book", "Form"))
        self.TitleLabel.setText(_translate("Book", "Title: "))
        self.BookTitle.setText(_translate("Book", "Title"))
        self.AuthorLabell.setText(_translate("Book", "Author: "))
        self.BookAuthor.setText(_translate("Book", "Author"))
        self.PublisherLabel.setText(_translate("Book", "Publisher: "))
        self.BookPublisher.setText(_translate("Book", "Publisher"))
        self.EditionLabel.setText(_translate("Book", "Edition: "))
        self.BookEdition.setText(_translate("Book", "Edition"))
        self.CategoryLabel.setText(_translate("Book", "Category: "))
        self.BookCategory.setText(_translate("Book", "Category"))
        self.PublishedDateLabel.setText(_translate("Book", "Published Date: "))
        self.BookPublisherDate.setText(_translate("Book", "BookPublishedDate"))
        self.StockLabel.setText(_translate("Book", "Stock: "))
        self.BookQuantity.setText(_translate("Book", "BookQuantity"))
        self.BookId.setText(_translate("Book", "TextLabel"))
        self.BorrowButton.setText(_translate("Book", "Borrow"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Book = QtWidgets.QWidget()
    ui = Ui_Book()
    ui.setupUi(Book)
    Book.show()
    sys.exit(app.exec_())
