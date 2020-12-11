# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(811, 576)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Login.sizePolicy().hasHeightForWidth())
        Login.setSizePolicy(sizePolicy)
        Login.setStyleSheet("QWidget{\n"
"    border-style:none;\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(Login)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.LoginContainer = QtWidgets.QFrame(Login)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LoginContainer.sizePolicy().hasHeightForWidth())
        self.LoginContainer.setSizePolicy(sizePolicy)
        self.LoginContainer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LoginContainer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LoginContainer.setObjectName("LoginContainer")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.LoginContainer)
        self.gridLayout_6.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.ColumnFrame = QtWidgets.QFrame(self.LoginContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ColumnFrame.sizePolicy().hasHeightForWidth())
        self.ColumnFrame.setSizePolicy(sizePolicy)
        self.ColumnFrame.setStyleSheet("")
        self.ColumnFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ColumnFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ColumnFrame.setObjectName("ColumnFrame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.ColumnFrame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.LogoFrame = QtWidgets.QFrame(self.ColumnFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LogoFrame.sizePolicy().hasHeightForWidth())
        self.LogoFrame.setSizePolicy(sizePolicy)
        self.LogoFrame.setStyleSheet("background-color: rgb(53, 57, 68);")
        self.LogoFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LogoFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LogoFrame.setObjectName("LogoFrame")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.LogoFrame)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.Logo = QtWidgets.QFrame(self.LogoFrame)
        self.Logo.setStyleSheet("QLabel{\n"
"    color: white;\n"
"    font: 25pt \"MS PGothic\";\n"
"}\n"
"QFrame{\n"
"    border-style:none;\n"
"}\n"
"")
        self.Logo.setLineWidth(0)
        self.Logo.setObjectName("Logo")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.Logo)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Icon = QtWidgets.QLabel(self.Logo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Icon.sizePolicy().hasHeightForWidth())
        self.Icon.setSizePolicy(sizePolicy)
        self.Icon.setText("")
        self.Icon.setPixmap(QtGui.QPixmap("Resources/Images/Library Inventory System.png"))
        self.Icon.setObjectName("Icon")
        self.verticalLayout.addWidget(self.Icon, 0, QtCore.Qt.AlignHCenter)
        self.Label = QtWidgets.QLabel(self.Logo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Label.sizePolicy().hasHeightForWidth())
        self.Label.setSizePolicy(sizePolicy)
        self.Label.setObjectName("Label")
        self.verticalLayout.addWidget(self.Label, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout_4.addWidget(self.Logo, 0, 0, 1, 1, QtCore.Qt.AlignVCenter)
        self.horizontalLayout_2.addWidget(self.LogoFrame)
        self.LoginFrame = QtWidgets.QFrame(self.ColumnFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LoginFrame.sizePolicy().hasHeightForWidth())
        self.LoginFrame.setSizePolicy(sizePolicy)
        self.LoginFrame.setStyleSheet("QFrame{\n"
"    border-style:none;\n"
"}\n"
"QLineEdit {\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.LoginFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.LoginFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.LoginFrame.setLineWidth(0)
        self.LoginFrame.setObjectName("LoginFrame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.LoginFrame)
        self.verticalLayout_2.setContentsMargins(50, 0, 50, 0)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.UsernameLineEdit = QtWidgets.QLineEdit(self.LoginFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.UsernameLineEdit.sizePolicy().hasHeightForWidth())
        self.UsernameLineEdit.setSizePolicy(sizePolicy)
        self.UsernameLineEdit.setStyleSheet("")
        self.UsernameLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.UsernameLineEdit.setObjectName("UsernameLineEdit")
        self.verticalLayout_2.addWidget(self.UsernameLineEdit)
        self.PasswordLineEdit = QtWidgets.QLineEdit(self.LoginFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PasswordLineEdit.sizePolicy().hasHeightForWidth())
        self.PasswordLineEdit.setSizePolicy(sizePolicy)
        self.PasswordLineEdit.setStyleSheet("")
        self.PasswordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.PasswordLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.PasswordLineEdit.setObjectName("PasswordLineEdit")
        self.verticalLayout_2.addWidget(self.PasswordLineEdit)
        self.LoginButton = QtWidgets.QPushButton(self.LoginFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LoginButton.sizePolicy().hasHeightForWidth())
        self.LoginButton.setSizePolicy(sizePolicy)
        self.LoginButton.setStyleSheet("")
        self.LoginButton.setDefault(False)
        self.LoginButton.setFlat(False)
        self.LoginButton.setObjectName("LoginButton")
        self.verticalLayout_2.addWidget(self.LoginButton, 0, QtCore.Qt.AlignVCenter)
        self.label = QtWidgets.QLabel(self.LoginFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet("color: red;\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.horizontalLayout_2.addWidget(self.LoginFrame, 0, QtCore.Qt.AlignVCenter)
        self.gridLayout_6.addWidget(self.ColumnFrame, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.LoginContainer, 0, 0, 1, 1)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Form"))
        self.Label.setText(_translate("Login", "Library Inventory System"))
        self.UsernameLineEdit.setPlaceholderText(_translate("Login", "username"))
        self.PasswordLineEdit.setPlaceholderText(_translate("Login", "password"))
        self.LoginButton.setText(_translate("Login", "Login"))
        self.label.setText(_translate("Login", "Invalid Username or Password"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QWidget()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())
