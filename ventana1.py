import sys

from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QHBoxLayout, QApplication, QFormLayout, QLineEdit, \
    QPushButton
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
        self.ancho = 900
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

        # ----------| LAYOUT IZQUIERDO |---------------#

        # Creamos el layout izquierdo:
        self.ladoIzquierdo = QFormLayout()

        # Hacemos el letrero
        self.letrero1 = QLabel()

        # Le escribimos el texto :
        self.letrero1.setText("Información del Cliente")

        # Le asignamos el tipo de letra:
        self.letrero1.setFont(QFont("Arial black", 20))

        # Le ponemos color de texto:

        self.letrero1.setStyleSheet("color: #000000;")

        # Agregamos el letrero en la primera fila:
        self.ladoIzquierdo.addRow(self.letrero1)

        # hacemos el letrero:
        self.letrero2 = QLabel()

        # Establecemos el ancho del label:
        self.letrero2.setFixedWidth(360)

        # Le escribimos el texto:
        self.letrero2.setText("por favor ingrese la información del cliente"
                              "\nen el formulario de abajo, los campos marcados"
                              "\ncon asteriscos obligatorios.")

        # Le asignamos el tipo de letra:
        self.letrero2.setFont(QFont("Arial black", 10))

        # Le ponemos color de texto y margenes:
        self.letrero2.setStyleSheet("color: #000000; margin-bottom: 50px;"
                                    "margin-top: 20px;"
                                    "padding-bottom: 10px;"
                                    "border: 2px solid #000000;"
                                    "border-left: none;"
                                    "border-right: none;"
                                    "border-top: none;")

        # Agregamos el letretero en la fila siguiente:
        self.ladoIzquierdo.addRow(self.letrero2)

        # Hacemos el campo para ingresar el nombre:
        self.nombreCompleto = QLineEdit()
        self.nombreCompleto.setFixedWidth(150)

        # Agregamos estos en el formulario:
        self.ladoIzquierdo.addRow("Nombre Completo*", self.nombreCompleto)

        # Hacemos el campo para ingresar el usuario:
        self.usuario = QLineEdit()
        self.usuario.setFixedWidth(150)

        # Agregamos estos en el formulario:
        self.ladoIzquierdo.addRow("Usuario*", self.usuario)

        # Hacemos el campo para ingresar el password:
        self.password = QLineEdit()
        self.password.setFixedWidth(150)
        self.password.setEchoMode(QLineEdit.Password)

        # Agregamos estos en el formulario:
        self.ladoIzquierdo.addRow("Password*", self.password)

        # Hacemos el campo para ingresar el password2:
        self.password2 = QLineEdit()
        self.password2.setFixedWidth(150)
        self.password2.setEchoMode(QLineEdit.Password)

        # Agregamos estos en el formulario:
        self.ladoIzquierdo.addRow("Password*", self.password2)

        # Hacemos el campo para ingresar el documento:
        self.documento = QLineEdit()
        self.documento.setFixedWidth(150)

        # Agregamos el documento en el formulario:
        self.ladoIzquierdo.addRow("Documento*", self.documento)

        # Hacemos el campo para ingresar el correo:
        self.correo = QLineEdit()
        self.correo.setFixedWidth(150)

        # Agregamos el correo en el formulario:
        self.ladoIzquierdo.addRow("Correo*", self.correo)

        # Hacemos el botón para registrar los datos:
        self.botonRegistrar = QPushButton("Registrar")

        # Establecemos el ancho del botón:
        self.botonRegistrar.setFixedWidth(90)

        # Le ponemos el ancho del botón:
        self.botonRegistrar.setStyleSheet("background-color: #E0E0E0;"
                                          "color: #000000;"
                                          "padding: 10px;"
                                          "margin-top: 40px")

        self.botonRegistrar.clicked.connect(self.accion_botonRegistrar)

        # Hacemos el botón para limpiar los datos:
        self.botonLimpiar =  QPushButton("Limpiar")

        # Establecemos el ancho del botón:
        self.botonLimpiar.setFixedWidth(90)

        # Le ponemos el ancho del botón:
        self.botonLimpiar.setStyleSheet("background-color: #E0E0E0;"
                                          "color: #000000;"
                                          "padding: 10px;"
                                          "margin-top: 40px")

        self.botonLimpiar.clicked.connect(self.accion_botonLimpiar)

        # Agregamos los dos botones al layout ladoIzquierdo:
        self.ladoIzquierdo.addRow(self.botonRegistrar, self.botonLimpiar)




        # Agregamos en layout ladoIzquierdo al layout horizontal
        self.horizontal.addLayout(self.ladoIzquierdo)




        #----------| IMPORTANTE PONER AL FINAL |---------------#

        # Indicamos que el layout principal del fondo es horizontal:
        self.fondo.setLayout(self.horizontal)

    # Método del boton limpiar:
    def accion_botonLimpiar(self):
        pass

    # Método del boton limpiar:
    def accion_botonRegistrar(self):
        pass








if __name__ == '__main__':

    # Hacer que la aplicación se genere
    app = QApplication(sys.argv)

    # Crear un objeto de tipo Ventana con el nombre de ventana1
    ventana1 = Ventana1()

    # Hacer que el objeto ventana se vea
    ventana1.show()

    sys.exit(app.exec_())








