import sys

from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QHBoxLayout, QApplication, QFormLayout, QLineEdit, \
    QPushButton, QDialog, QDialogButtonBox, QVBoxLayout
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt

from cliente import Cliente


class Ventana1(QMainWindow):

    # hacer el metodo constructor  en la ventana:
    def __init__(self, parent=None):
        super(Ventana1, self).__init__(parent)

        # Poner el titulo:
        self.setWindowTitle("Formulario de registro")

        # Poner el icono:
        self.setWindowIcon(QtGui.QIcon("imagenes/monkey.png"))

        # Establecemos las propiedades de ancho y alto:
        self.ancho = 1000
        self.alto = 600

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

    #----#

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
        self.nombreCompleto.setFixedWidth(200)

        # Agregamos estos en el formulario:
        self.ladoIzquierdo.addRow("Nombre Completo*", self.nombreCompleto)

        # Hacemos el campo para ingresar el usuario:
        self.usuario = QLineEdit()
        self.usuario.setFixedWidth(200)

        # Agregamos estos en el formulario:
        self.ladoIzquierdo.addRow("Usuario*", self.usuario)

        # Hacemos el campo para ingresar el password:
        self.password = QLineEdit()
        self.password.setFixedWidth(200)
        self.password.setEchoMode(QLineEdit.Password)

        # Agregamos estos en el formulario:
        self.ladoIzquierdo.addRow("Password*", self.password)

        # Hacemos el campo para ingresar el password2:
        self.password2 = QLineEdit()
        self.password2.setFixedWidth(200)
        self.password2.setEchoMode(QLineEdit.Password)

        # Agregamos estos en el formulario:
        self.ladoIzquierdo.addRow("Password*", self.password2)

        # Hacemos el campo para ingresar el documento:
        self.documento = QLineEdit()
        self.documento.setFixedWidth(200)

        # Agregamos el documento en el formulario:
        self.ladoIzquierdo.addRow("Documento*", self.documento)

        # Hacemos el campo para ingresar el correo:
        self.correo = QLineEdit()
        self.correo.setFixedWidth(200)

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
        self.botonLimpiar = QPushButton("Limpiar")

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


        # ----------| LAYOUT DERECHO |---------------#

        # creamos el Layout del lado derecho:
        self.ladoDerecho = QFormLayout()

        # Se asigna la margen solo a la izquierda de 100px:
        self.ladoDerecho.setContentsMargins(50, 0, 0, 0)

        # Hacemos el letrero:
        self.letrero3 = QLabel()

        # Le escribimos el texto:
        self.letrero3.setText("Recuperar contraseña")

        # Le asignamos el tipo de letra:
        self.letrero3.setFont(QFont("Arial black", 20))

        # Le ponemos color de texto:
        self.letrero3.setStyleSheet("color: #000000;")

        # Agregamos el letrero en la primera fila:
        self.ladoDerecho.addRow(self.letrero3)

        # Hacemos el letrero:
        self.letrero4 = QLabel()

        # Establecemos el ancho del label:
        self.letrero4.setFixedWidth(400)

        # Le escribimos el texto:
        self.letrero4.setText("por favor ingrese la información para recuperar"
                              "\nla contraseña. los campos marcados"
                              "\ncon asteriscos obligatorios.")

        # Le asignamos el tipo de letra:
        self.letrero4.setFont(QFont("Arial black", 10))

        # Le ponemos color de texto y margenes:
        self.letrero4.setStyleSheet("color: #000000; margin-bottom: 50px;"
                                    "margin-top: 20px;"
                                    "padding-bottom: 10px;"
                                    "border: 2px solid #000000;"
                                    "border-left: none;"
                                    "border-right: none;"
                                    "border-top: none;")

        # Agregamos el letretero en la fila siguiente:
        self.ladoDerecho.addRow(self.letrero4)

        # ---- 1

        # Hacemos el letrero  de la pregunta 1:
        self.labelPregunta1 = QLabel("Pregunta de verificación 1*")

        # Agregamos el letrero en la fila siguiente:
        self.ladoDerecho.addRow(self.labelPregunta1)

        # Hacemos el campo para ingresar la pregunta 1:
        self.pregunta1 = QLineEdit()
        self.pregunta1.setFixedWidth(200)

        # Agregamos el campo en el formulario:
        self.ladoDerecho.addRow(self.pregunta1)

        # Hacemos el letrero de la respuesta 1:
        self.labelRespuesta1 = QLabel("Respuesta de verificación 1*")

        # Agregamos el letrero en la fila siguiente:
        self.ladoDerecho.addRow(self.labelRespuesta1)

        # Hacemos el campo para ingresar la respuesta 1
        self.respuesta1 = QLineEdit()
        self.respuesta1.setFixedWidth(200)

        # Agregamos el campo en el formulario:
        self.ladoDerecho.addRow(self.respuesta1)

        # ---- 2

        # Hacemos el letrero  de la pregunta 2:
        self.labelPregunta2 = QLabel("Pregunta de verificación 2*")

        # Agregamos el letrero en la fila siguiente:
        self.ladoDerecho.addRow(self.labelPregunta2)

        # Hacemos el campo para ingresar la pregunta 2:
        self.pregunta2 = QLineEdit()
        self.pregunta2.setFixedWidth(200)

        # Agregamos el campo en el formulario:
        self.ladoDerecho.addRow(self.pregunta2)

        # Hacemos el letrero de la respuesta 2:
        self.labelRespuesta2 = QLabel("Respuesta de verificación 2*")

        # Agregamos el letrero en la fila siguiente:
        self.ladoDerecho.addRow(self.labelRespuesta2)

        # Hacemos el campo para ingresar la respuesta 2:
        self.respuesta2 = QLineEdit()
        self.respuesta2.setFixedWidth(200)

        # Agregamos el campo en el formulario:
        self.ladoDerecho.addRow(self.respuesta2)

        # ---- 3

        # Hacemos el letrero  de la pregunta 3:
        self.labelPregunta3 = QLabel("Pregunta de verificación 3*")

        # Agregamos el letrero en la fila siguiente:
        self.ladoDerecho.addRow(self.labelPregunta3)

        # Hacemos el campo para ingresar la pregunta 3:
        self.pregunta3 = QLineEdit()
        self.pregunta3.setFixedWidth(200)

        # Agregamos el campo en el formulario:
        self.ladoDerecho.addRow(self.pregunta3)

        # Hacemos el letrero de la respuesta 2:
        self.labelRespuesta3 = QLabel("Respuesta de verificación 3*")

        # Agregamos el letrero en la fila siguiente:
        self.ladoDerecho.addRow(self.labelRespuesta3)

        # Hacemos el campo para ingresar la respuesta 3:
        self.respuesta3 = QLineEdit()
        self.respuesta3.setFixedWidth(200)

        # Agregamos el campo en el formulario:
        self.ladoDerecho.addRow(self.respuesta3)


        # Hacemos el botón para buscar la preguntas:
        self.botonBuscar = QPushButton("Buscar")

        # Establecemos el ancho del botón:
        self.botonBuscar.setFixedWidth(90)

        # Le ponemos el ancho del botón:
        self.botonBuscar.setStyleSheet("background-color: #E0E0E0;"
                                        "color: #000000;"
                                        "padding: 10px;"
                                        "margin-top: 40px"
                                       )
        # Hacemos que el boton buscar tenga su metodo:
        self.botonBuscar.clicked.connect(self.accion_botonBuscar)


        # Hacemos el botón para recuperar la contraseña:
        self.botonRecuperar = QPushButton("Recuperar")

        # Establecemos el ancho del botón:
        self.botonRecuperar.setFixedWidth(90)

        # Le ponemos el ancho del botón:
        self.botonRecuperar.setStyleSheet("background-color: #E0E0E0;"
                                       "color: #000000;"
                                       "padding: 10px;"
                                       "margin-top: 40px"
                                       )

        self.botonLimpiar.clicked.connect(self.accion_botonLimpiar)

        # Agregamos los dos botones al layout ladoDerecho:
        self.ladoDerecho.addRow(self.botonBuscar, self.botonRecuperar)
        #---#

        # Agregamos en layout ladoDerecho al layout horizontal:
        self.horizontal.addLayout(self.ladoDerecho)


        #----------| IMPORTANTE PONER AL FINAL |---------------#

        # Indicamos que el layout principal del fondo es horizontal:
        self.fondo.setLayout(self.horizontal)

        # Creamos la ventana de dialogo:
        self.ventanaDialogo = QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint)

        # Definimos el tamaño de la ventana:
        self.ventanaDialogo.resize(300, 150)

        # Creamos el botón para aceptar:
        self.botonAceptar = QDialogButtonBox.Ok
        self.opciones = QDialogButtonBox(self.botonAceptar)
        self.opciones.accepted.connect(self.ventanaDialogo.accept)

        # establecemos el titulo de la ventana:
        self.ventanaDialogo.setWindowTitle("Formulario de registro")

        # Configuramos la ventana para que sea modal:
        self.ventanaDialogo.setWindowModality(Qt.ApplicationModal)

        # Creamos un layout vertical:
        self.vertical = QVBoxLayout()

        # Creamos un label para los mensajes:
        self.mensaje = QLabel("")

        # Le ponemos estilos al label mensaje:
        self.mensaje.setStyleSheet("background-color #000000; color #FFFFFF; padding: 10px;")

        # Agregamos el label de mensajes:
        self.vertical.addWidget(self.mensaje)

        # Agregamos las opciones de los botones:
        self.vertical.addWidget(self.opciones)

        # Establecemos el layput para la ventana:
        self.ventanaDialogo.setLayout(self.vertical)

        # Variable para controlar que se han ingresado los datos correctos:
        self.datosCorrectos = True

    # Método del boton limpiar:
    def accion_botonLimpiar(self):
        self.nombreCompleto.setText('')
        self.usuario.setText('')
        self.password.setText('')
        self.password2.setText('')
        self.documento.setText('')
        self.correo.setText('')
        self.pregunta1.setText('')
        self.respuesta1.setText('')
        self.pregunta2.setText('')
        self.respuesta2.setText('')
        self.pregunta3.setText('')
        self.respuesta3.setText('')

    # Método del boton limpiar:
    def accion_botonRegistrar(self):




        # Validamos que los passwords sean iguales
        if(
                self.password.text() != self. password2.text()
        ):
            self.datosCorrectos = False

            # Escribimos el texto explicativo:
            self.mensaje.setText("Los passwords no coinciden")

            # Hacemos que la ventana de dialogo se vea:
            self.ventanaDialogo.exec_()

        # Validamos que se ingresen todos los campos
        if(
                self.nombreCompleto.text() == ''
                or self.usuario.text == ''
                or self.password.text == ''
                or self.password2.text == ''
                or self.documento.text == ''
                or self.correo.text == ''
                or self.pregunta1.text == ''
                or self.respuesta1.text == ''
                or self.pregunta2.text == ''
                or self.respuesta2.text() == ''
                or self.pregunta3.text == ''
                or self.respuesta3.text() == ''

        ):
            self.datosCorrectos = False

            # Escribimos en texto explicativo:
            self.mensaje.setText("Debe ingresar todos los campos")

            # Hacemos que la ventana de dialogo se vea:
            self.ventanaDialogo.exec_()

        # Si lo sdatos estan correctos:
        if self.datosCorrectos:
            # Abrimos el archivo en modo agregar escribiendo datos en binario
            self.file = open('datos/clientes.txt', 'ab')

            # Traer el texto de los QLineEdit y los agrega concatenandolos
            # PAra escribirlos en el archivo en formato binatio utf-8
            self.file.write(bytes(
                self.nombreCompleto.text() + ";"
                + self.usuario.text() + ";"
                + self.password.text() + ";"
                + self.password2.text() + ";"
                + self.documento.text() + ";"
                + self.correo.text() + ";"
                + self.pregunta1.text() + ";"
                + self.respuesta1.text() + ";"
                + self.pregunta2.text() + ";"
                + self.respuesta2.text() + ";"
                + self.pregunta3.text() + ";"
                + self.respuesta3.text() + "\n"
                ,encoding='UTF-8'))

            # Cerramos el archivo:
            self.file.close()

            # Abrimos en modo lectura en fomato bytes.
            self.file = open('datos/clientes.txt', 'rb')
            # Recorrer el archivo linea por linea.
            while self.file:
                linea = self.file.readline().decode('UTF-8')
                print(linea)
                if linea == '': # para cuando encuentre una línea vacía.
                    break
            self.file.close()

    # Metodo del botónBuscar:

    def accion_botonBuscar(self):
        # Establecemos el titulo de la ventana:
        self.ventanaDialogo.setWindowTitle("Buscar preguntas de validación")

        # Validar que se halla ingresado el documento:
        if (
                self.documento.text() == ''
        ):
            self.datosCorrectos = False

            # Escribimos el texto explicativo:
            self.mensaje.setText("Sí va a buscar preguntas"
                                 " para recuperar la contraseña."
                                 "\nDebe primero, Ingresar el documento.")

            # Hacemos que la ventana de dialogo se vea:
            self.ventanaDialogo.exec_()

            # Validar si el documento es númerico:
        if(
            not self.documento.text().isnumeric()
        ):
            self.datosCorrectos = False

            # Escribimos el texto explicativo:
            self.mensaje.setText("El documento debe ser númerico."
                                 "\nNo ingrese letras "
                                 "ni caracterés especiales.")

            # Hacemos que la vantana de dialogo se vea:
            self.ventanaDialogo.exec_()

            # Limpiamos el campo del documento:
            self.documento.setText('')

        if (
            self.datosCorrectos
        ):
            # Abrimos el archivo en modo lectura:
            self.file = open('datos/clientes.txt', 'rb')

            # Lista vacia para guardar todos los usuarios:
            usuarios = []

            while self.file:
                linea = self.file.readline().decode('UTF-8')

                # Obtenemos del string una lista con 11 datos separados por:
                lista = linea.split(";")
                # Se para si ya no hay mas registros en el archivo
                if linea == '':
                    break

                # Creamos un objeto tipo cliente llamado u
                u = Cliente(
                    lista[0],
                    lista[1],
                    lista[2],
                    lista[3],
                    lista[4],
                    lista[5],
                    lista[6],
                    lista[7],
                    lista[8],
                    lista[9],
                    lista[10],
                )

                # Metemos el objeto en la lista de usuarios:
                usuarios.append(u)

            # Cerramos el archivo:
            self.file.close()

            # En este punto tenemos la lista de usuarios con todos los usuarios:

            # Variable para controlar si existe el documento:
            existeDocumento = False

            # Buscamos en la lista usuario si existe la cedula:
            for u in usuarios:

                # comparamos el documento ingresado:
                # Si corresponde el documento, es el usuario correcto:
                if u.documento == self.documento.text():
                    # Mostramos las preguntas en el formulario:
                    self.pregunta1.setText(u.pregunta1)
                    self.pregunta2.setText(u.pregunta2)
                    self.pregunta3.setText(u.pregunta3)

                    # Indicamos que encontramos el documento:
                    existeDocumento = True

                    # Paramos el for:
                    break

                # Si no existe un usuario con este documento:
                if (
                        not existeDocumento
                ):

                    # Escribimos el texto explicativo:
                    self.mensaje.setText("No existe un usuario con este documento:\n"
                                         + self.documento.text())

                    # Hacemos que la ventana de dialogo se vea:
                    self.ventanaDialogo.exec_()



if __name__ == '__main__':

    # Hacer que la aplicación se genere
    app = QApplication(sys.argv)

    # Crear un objeto de tipo Ventana con el nombre de ventana1
    ventana1 = Ventana1()

    # Hacer que el objeto ventana se vea
    ventana1.show()

    sys.exit(app.exec_())