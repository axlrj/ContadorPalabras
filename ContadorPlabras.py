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
        texto= self.edtCaracteres.text()
        #Separar las palabras
        textoSeparado=texto.split()
        print(textoSeparado)
        #Contar las palabras
        cantidadPalabras= len(textoSeparado)
        print("Palabras: ",cantidadPalabras)
        self.tvPalabras.setText(f"Palabras:{cantidadPalabras}")
        #Contar caracteres
        totalCaracteres = 0 
        for palabra in textoSeparado:
            totalCaracteres+= len (palabra)
        self.tvCaracteres.setText(f"Caracteres:{totalCaracteres}")
        print("Funciona boton")

app=QtWidgets.QApplication(sys.argv)
ventana= ContadorPalabras()
ventana.show()
sys.exit(app.exec())