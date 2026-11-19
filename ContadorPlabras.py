import sys
from PyQt6 import QtWidgets,uic

class ContadorPalabras(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        #Cargar nuestra vista
        uic.loadUi("contadorPalabras.ui",self)
        self.btnContar.clicked.connect(self.ContarPalabras)
        #configurar el cambio de texto
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
        #cambiar color rojo
        if cantidadPalabras >= 20:
            self.tvPalabras.setStyleSheet("color: red;")
        else:
            self.tvPalabras.setStyleSheet("color: black;")

        if totalCaracteres >= 120:
            self.tvCaracteres.setStyleSheet("color: #ff756b")
        else:
            self.tvCaracteres.setStyleSheet("color: #000000")

app=QtWidgets.QApplication(sys.argv)
ventana= ContadorPalabras()
ventana.show()
sys.exit(app.exec())