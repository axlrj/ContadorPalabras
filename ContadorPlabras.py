import sys
from PyQt6 import QtWidgets,uic

class ContadorPalabras(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        #Cargar nuestra vista
        uic.loadUi("contadorPalabras.ui",self)
        self.btnContar.clicked.connect(self.ContarPalabras)
    def ContarPalabras(self):
        #Recuperar texto
        texto= self.edtCaracteres.Text()
        #Separar las palabras
        textoSeparado=texto.split()
        print(textoSeparado)
        #Contar las palabras
        #Contar caracteres
        print("Funciona boton")
app=QtWidgets.QApplication(sys.argv)
ventana= ContadorPalabras()
ventana.show()
sys.exit(app.exec())