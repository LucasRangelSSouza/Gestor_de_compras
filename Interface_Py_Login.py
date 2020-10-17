# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
sys.path.append("Imagens")
sys.path.append("Icone")

class Ui_MainWindowLogin(object):
    def setupUi(self, MainWindowLogin):
        MainWindowLogin.setObjectName("MainWindowLogin")
        MainWindowLogin.resize(473, 243)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Imagens/Icone/Icone.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindowLogin.setWindowIcon(icon)
        MainWindowLogin.setWindowOpacity(1.0)
        MainWindowLogin.setStyleSheet("background-color: rgb(83, 83, 83);\n"
"border-radius: 50px;")
        self.centralWidgetGrid = QtWidgets.QWidget(MainWindowLogin)
        self.centralWidgetGrid.setObjectName("centralWidgetGrid")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidgetGrid)
        self.gridLayout.setObjectName("gridLayout")
        self.frameSpace3 = QtWidgets.QFrame(self.centralWidgetGrid)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameSpace3.sizePolicy().hasHeightForWidth())
        self.frameSpace3.setSizePolicy(sizePolicy)
        self.frameSpace3.setMinimumSize(QtCore.QSize(0, 20))
        self.frameSpace3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameSpace3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameSpace3.setObjectName("frameSpace3")
        self.gridLayout.addWidget(self.frameSpace3, 4, 3, 1, 1)
        self.frameSpace4 = QtWidgets.QFrame(self.centralWidgetGrid)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameSpace4.sizePolicy().hasHeightForWidth())
        self.frameSpace4.setSizePolicy(sizePolicy)
        self.frameSpace4.setMinimumSize(QtCore.QSize(0, 20))
        self.frameSpace4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameSpace4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameSpace4.setObjectName("frameSpace4")
        self.gridLayout.addWidget(self.frameSpace4, 6, 3, 1, 1)
        self.frameSpace5 = QtWidgets.QFrame(self.centralWidgetGrid)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameSpace5.sizePolicy().hasHeightForWidth())
        self.frameSpace5.setSizePolicy(sizePolicy)
        self.frameSpace5.setMinimumSize(QtCore.QSize(20, 0))
        self.frameSpace5.setMaximumSize(QtCore.QSize(100, 16777215))
        self.frameSpace5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameSpace5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameSpace5.setObjectName("frameSpace5")
        self.gridLayout.addWidget(self.frameSpace5, 3, 4, 1, 1)
        self.frameSpace2 = QtWidgets.QFrame(self.centralWidgetGrid)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameSpace2.sizePolicy().hasHeightForWidth())
        self.frameSpace2.setSizePolicy(sizePolicy)
        self.frameSpace2.setMinimumSize(QtCore.QSize(30, 20))
        self.frameSpace2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameSpace2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameSpace2.setObjectName("frameSpace2")
        self.gridLayout.addWidget(self.frameSpace2, 2, 3, 1, 1)
        self.lineEditLogin = QtWidgets.QLineEdit(self.centralWidgetGrid)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditLogin.sizePolicy().hasHeightForWidth())
        self.lineEditLogin.setSizePolicy(sizePolicy)
        self.lineEditLogin.setMinimumSize(QtCore.QSize(300, 31))
        self.lineEditLogin.setMaximumSize(QtCore.QSize(16777215, 45))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.lineEditLogin.setFont(font)
        self.lineEditLogin.setStyleSheet("QLineEdit#lineEditLogin {\n"
"    color: rgb(107, 107, 107);\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"}\n"
"")
        self.lineEditLogin.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditLogin.setObjectName("lineEditLogin")
        self.gridLayout.addWidget(self.lineEditLogin, 1, 3, 1, 1)
        self.labelLogin = QtWidgets.QLabel(self.centralWidgetGrid)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelLogin.sizePolicy().hasHeightForWidth())
        self.labelLogin.setSizePolicy(sizePolicy)
        self.labelLogin.setMaximumSize(QtCore.QSize(16777215, 45))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.labelLogin.setFont(font)
        self.labelLogin.setStyleSheet("color: rgb(255, 255, 255);")
        self.labelLogin.setAlignment(QtCore.Qt.AlignCenter)
        self.labelLogin.setObjectName("labelLogin")
        self.gridLayout.addWidget(self.labelLogin, 1, 1, 1, 1)
        self.lineEditSenha = QtWidgets.QLineEdit(self.centralWidgetGrid)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditSenha.sizePolicy().hasHeightForWidth())
        self.lineEditSenha.setSizePolicy(sizePolicy)
        self.lineEditSenha.setMinimumSize(QtCore.QSize(300, 31))
        self.lineEditSenha.setMaximumSize(QtCore.QSize(16777215, 45))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lineEditSenha.setFont(font)
        self.lineEditSenha.setStyleSheet("QLineEdit#lineEditSenha {\n"
"color: rgb(107, 107, 107);\n"
"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"padding-left: 10px;\n"
"padding-right: 10px;\n"
"}")
        self.lineEditSenha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditSenha.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditSenha.setObjectName("lineEditSenha")
        self.gridLayout.addWidget(self.lineEditSenha, 3, 3, 1, 1)
        self.labelSenha = QtWidgets.QLabel(self.centralWidgetGrid)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelSenha.sizePolicy().hasHeightForWidth())
        self.labelSenha.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.labelSenha.setFont(font)
        self.labelSenha.setStyleSheet("color: rgb(255, 255, 255);")
        self.labelSenha.setAlignment(QtCore.Qt.AlignCenter)
        self.labelSenha.setObjectName("labelSenha")
        self.gridLayout.addWidget(self.labelSenha, 3, 1, 1, 1)
        self.frameSpace6 = QtWidgets.QFrame(self.centralWidgetGrid)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameSpace6.sizePolicy().hasHeightForWidth())
        self.frameSpace6.setSizePolicy(sizePolicy)
        self.frameSpace6.setMinimumSize(QtCore.QSize(20, 0))
        self.frameSpace6.setMaximumSize(QtCore.QSize(100, 10))
        self.frameSpace6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameSpace6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameSpace6.setObjectName("frameSpace6")
        self.gridLayout.addWidget(self.frameSpace6, 3, 0, 1, 1)
        self.frameSpace1 = QtWidgets.QFrame(self.centralWidgetGrid)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameSpace1.sizePolicy().hasHeightForWidth())
        self.frameSpace1.setSizePolicy(sizePolicy)
        self.frameSpace1.setMinimumSize(QtCore.QSize(0, 20))
        self.frameSpace1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameSpace1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameSpace1.setObjectName("frameSpace1")
        self.gridLayout.addWidget(self.frameSpace1, 0, 3, 1, 1)
        self.horizontalLayoutBotoes = QtWidgets.QHBoxLayout()
        self.horizontalLayoutBotoes.setObjectName("horizontalLayoutBotoes")
        self.pushButtonLogin = QtWidgets.QPushButton(self.centralWidgetGrid)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonLogin.sizePolicy().hasHeightForWidth())
        self.pushButtonLogin.setSizePolicy(sizePolicy)
        self.pushButtonLogin.setMinimumSize(QtCore.QSize(40, 35))
        self.pushButtonLogin.setMaximumSize(QtCore.QSize(200, 45))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonLogin.setFont(font)
        self.pushButtonLogin.setStyleSheet("QPushButton#pushButtonLogin {\n"
"    background-color: rgb(0, 122, 204);\n"
"    border-radius: 10px;\n"
"    border-color: rgb(11, 183, 235);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton#pushButtonLogin:hover {\n"
"    \n"
"    background-color: rgb(7, 88, 142);\n"
"}")
        self.pushButtonLogin.setObjectName("pushButtonLogin")
        self.horizontalLayoutBotoes.addWidget(self.pushButtonLogin)
        self.pushButtonCancelar = QtWidgets.QPushButton(self.centralWidgetGrid)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonCancelar.sizePolicy().hasHeightForWidth())
        self.pushButtonCancelar.setSizePolicy(sizePolicy)
        self.pushButtonCancelar.setMinimumSize(QtCore.QSize(40, 35))
        self.pushButtonCancelar.setMaximumSize(QtCore.QSize(200, 45))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonCancelar.setFont(font)
        self.pushButtonCancelar.setStyleSheet("QPushButton#pushButtonCancelar {\n"
"    background-color: rgb(0, 122, 204);\n"
"    border-radius: 10px;\n"
"    border-color: rgb(11, 183, 235);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton#pushButtonCancelar:hover {\n"
"    \n"
"    background-color: rgb(7, 88, 142);\n"
"}")
        self.pushButtonCancelar.setObjectName("pushButtonCancelar")
        self.horizontalLayoutBotoes.addWidget(self.pushButtonCancelar)
        self.gridLayout.addLayout(self.horizontalLayoutBotoes, 5, 2, 1, 2)
        self.frameSpace7 = QtWidgets.QFrame(self.centralWidgetGrid)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameSpace7.sizePolicy().hasHeightForWidth())
        self.frameSpace7.setSizePolicy(sizePolicy)
        self.frameSpace7.setMinimumSize(QtCore.QSize(20, 20))
        self.frameSpace7.setMaximumSize(QtCore.QSize(60, 0))
        self.frameSpace7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameSpace7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameSpace7.setObjectName("frameSpace7")
        self.gridLayout.addWidget(self.frameSpace7, 2, 2, 1, 1)
        MainWindowLogin.setCentralWidget(self.centralWidgetGrid)

        self.retranslateUi(MainWindowLogin)
        QtCore.QMetaObject.connectSlotsByName(MainWindowLogin)

    def retranslateUi(self, MainWindowLogin):
        _translate = QtCore.QCoreApplication.translate
        MainWindowLogin.setWindowTitle(_translate("MainWindowLogin", "R-Tech"))
        self.labelLogin.setText(_translate("MainWindowLogin", "Login"))
        self.labelSenha.setText(_translate("MainWindowLogin", "Senha"))
        self.pushButtonLogin.setText(_translate("MainWindowLogin", "Login"))
        self.pushButtonCancelar.setText(_translate("MainWindowLogin", "Cancelar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindowLogin = QtWidgets.QMainWindow()
    ui = Ui_MainWindowLogin()
    ui.setupUi(MainWindowLogin)
    MainWindowLogin.show()
    sys.exit(app.exec_())

