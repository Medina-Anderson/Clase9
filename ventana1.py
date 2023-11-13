import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QHBoxLayout, QApplication
from PyQt5 import QtGui


class Ventana1(QMainWindow):

    # hacer el metodo constructor  en la ventana:
    def __init__(self, parent=None):
        super(Ventana1, self).__init__(parent)

        # Poner el titulo:
        self.setWindowTitle("Formulario de registro")

        # Poner el icono:
        self.setWindowIcon(QtGui.QIcon("imagenes/monkey.png"))

        # Establecemos las propiedades de ancho y alto:
        self.ancho = 800
        self.alto = 500

        # Establecemos el tamaño de la ventana:
        self.resize(self.ancho, self.alto)

        # Estas lineas hacen que la ventana se vea en el centro:
        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        # Para fijar que la ventana no se pueda cambiar de tamaño
        # Se fija el ancho y el alto
        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        # Establecemos el fondo principal:
        self.fondo = QLabel(self)

        # Definimos la imagen de fondo:
        self.imagenFondo = QPixmap("imagenes/desert.jpg")

        # Definimos la imagen de fondo:
        self.fondo.setPixmap(self.imagenFondo)

        # Definimo la imagen de fondo:
        self.fondo.setScaledContents(True)

        # Hacemos que se adapte el tamaño de la imagen:
        self.resize(self.imagenFondo.width(), self.imagenFondo.height())

        # Establecemos la ventana de fondo como la ventana central:
        self.setCentralWidget(self.fondo)

        # Establecemos la distribución de los elementos en forma horizontal:
        self.horizontal = QHBoxLayout()

        # Ponemos las margenes:
        self.horizontal.setContentsMargins(30, 30, 30, 30)



        #----------| IMPORTANTE PONER AL FINAL |---------------#

        # Indicamos que el layout principal del fondo es horizontal:
        self.fondo.setLayout(self.horizontal)


if __name__ == '__main__':

    # Hacer que la aplicación se genere
    app = QApplication(sys.argv)

    # Crear un objeto de tipo Ventana con el nombre de ventana1
    ventana1 = Ventana1()

    # Hacer que el objeto ventana se vea
    ventana1.show()

    sys.exit(app.exec_())








