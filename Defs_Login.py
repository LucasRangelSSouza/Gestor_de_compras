import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Interface_Py_Login import Ui_MainWindowLogin
import sqlite3
from Licitacoes import Ui_Dialog



class DefsLogin(QtWidgets.QMainWindow):    
    def __init__(self):
        self.testarConexao()
        QtWidgets.QMainWindow.__init__(self) 
        self.ui = Ui_MainWindowLogin()
        self.ui.setupUi(self)


#--------------------------------Construtores-----------------------------
        




#--------------------------------Funçoes---------------------------------
    def LoginOK(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.window)
        DefsLogin.hide()
        self.window.show()

    def testarConexao(self):
        print("Teste de Conexao")



if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    programa = DefsLogin()
    programa.show()

    sys.exit(app.exec_())
