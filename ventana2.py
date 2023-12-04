import math
import sys

from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QVBoxLayout, QScrollArea, QWidget, QGridLayout, \
    QPushButton, QApplication, QButtonGroup
from PyQt5 import QtGui

from cliente import Cliente
from ventana3 import Ventana3


class Ventana2(QMainWindow):

    # Metodo constructor de la ventana
    def __init__(self, anterior):
        super(Ventana2, self).__init__(anterior)

        # Creamos un atributo que guarde la ventana anterior
        self.ventanaAnterior = anterior

        # poner el titulo
        self.setWindowTitle("Usuarios Registrados")

        # Ponemos el icono
        self.setWindowIcon(QtGui.QIcon('imagenes/cliente.jpg'))

        # Establecemos las propiedades de ancho por alto
        self.ancho = 900
        self.alto = 600

        # Establecemos el tamaño de la venata
        self.resize(self.ancho, self.alto)

        # Centrar la ventana en la pantalla
        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        # Fijar el tamaño de la ventana para evitar cambiarlo
        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        # Establecemos el fondo principal
        self.fondo = QLabel(self)

        # Definimos la imagen de fondo
        self.imagenFondo = QPixmap('imagenes/empresa.jpg')

        # Definimos la iamgen de fondo
        self.fondo.setPixmap(self.imagenFondo)

        # Establecemos el modo para escalar la imagen
        self.fondo.setScaledContents(True)

        # Hacemos que se adapte al tamaño de la imagen
        self.resize(self.imagenFondo.width(), self.imagenFondo.height())

        # Establecemos la ventana de fondo como ventana central
        self.setCentralWidget(self.fondo)



        # Establecemos la distribucion de los elementos en layout vertical
        self.vertical = QVBoxLayout()



        # Hacemos el letrero
        self.letrero1 = QLabel()

        # Le escribimos el texto
        self.letrero1.setText("Usuarios Registrados")

        # Le asignamos el tipo de letra
        self.letrero1.setFont(QFont("Andale Mono", 20))

        # Le asignamos color de texto
        self.letrero1.setStyleSheet("color: #000080;")

        # Agregamos el letrero en la primera fila
        self.vertical.addWidget(self.letrero1)


        # Ponemos un espacio despues
        self.vertical.addStretch()


        # Creamos un scroll
        self.scrollArea = QScrollArea()

        # Le ponemos transparente el fondo del scroll
        self.scrollArea.setStyleSheet("background-color: transparent;")

        # Hacemos que el scroll se adapte a diferentes tamaños
        self.scrollArea.setWidgetResizable(True)

        # Creamos una ventana contenedora para cada celda
        self.contenedora = QWidget()

        # Vamos a crear un Layout de grid para poner una cuadricula de elemento:
        self.cuadricula = QGridLayout(self.contenedora)

        # Metenos la ventana contenedora en el scroll:
        self.scrollArea.setWidget(self.contenedora)

        # Metemos en el Layout vertical el scroll:
        self.vertical.addWidget(self.scrollArea)

        # Abrimos el archivo en modo de lectura
        self.file = open('datos/clientes.txt', 'rb')

        # Lista vacia para guardar los usuarios
        self.usuarios = []

        # Recorremos el archivo, linea por linea
        while self.file:
            linea = self.file.readline().decode('UTF-8')
            # Obtenemos del string una lista con 11 datos separados por :
            lista = linea.split(";")
            # Se para si ya no hay msa registros en el archivo
            if linea == '':
                break
            # Creamos un objeto de tipo cliente llamado u
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
            # Metemos el objeto en la lista de usuario:
            self.usuarios.append(u)

            # Cerramos el archivo
        self.file.close()

        # En este punto tenemos la lista usuarios con los usuarios

        # Obtenemos el numero de usuarios registrados
        # Consultamos el tamaño de la lista usuarios
        self.numeroUsuarios = len(self.usuarios)

        # Contador de elementos para controlar a los usuarios en la lista usuario
        self.contador = 1

        # Definimos la cantidad de elementos a mostrar por fila con columna
        self.elementosPorColumna = 3

        # Calculamos el numero de filas
        # Redondemos al entero superior + 1, dividimos por elementosPorColumna:
        self.numeroFilas = math.ceil(self.numeroUsuarios / self.elementosPorColumna) + 1

        # Controlamos todos los botones por una variable
        self.botones = QButtonGroup()

        # Definimos que el controlador de los botones
        # debe agrupar a todos los botones internos
        self.botones.setExclusive(False)

        for fila in range(1, self.numeroFilas):
            for columna in range(1, self.elementosPorColumna+1):

                # Validamos que se estan ingresando la cantidad de usuarios correctos
                if self.contador < self.numeroUsuarios:

                    # En cada celda de la cuadricula va una ventana
                    self.ventanaAuxiliar = QWidget()

                    # Se determina su alto y su ancho
                    self.ventanaAuxiliar.setFixedHeight(100)
                    self.ventanaAuxiliar.setFixedWidth(200)

                    # Creamos un layout vertical para cada elemento de la cuadricula
                    self.verticalCuadricula = QVBoxLayout()

                    # Creamos un boton para cada usuario mostrar su cedula
                    self.botonAccion = QPushButton(self.usuarios[self.contador].documento)

                    # Establecemos el ancho del boton
                    self.botonAccion.setFixedWidth(150)

                    # Le ponemos los estilos
                    self.botonAccion.setStyleSheet("background-color: #008845;"
                                                      "color: #FFFFFF;"
                                                      "padding: 10px;"
                                                      )


                    # Metemos el boton en el layout vertical para que se vea
                    self.verticalCuadricula.addWidget(self.botonAccion)

                    # Agregamos el boton al grupo, con su cedula como id
                    self.botones.addButton(self.botonAccion, int(self.usuarios[self.contador].documento))

                    # Agregamos un espacio en blanco
                    self.verticalCuadricula.addStretch()

                    # A la ventana le asignamos el layout vertical
                    self.ventanaAuxiliar.setLayout(self.verticalCuadricula)

                    # A la cuadricula le agregamos la ventana en la fila y columana actual
                    self.cuadricula.addWidget(self.ventanaAuxiliar, fila, columna)

                    # Aumentamos el contador
                    self.contador += 1


        # Establecemos el metodo para que funcionen todos los botones
        self.botones.idClicked.connect(self.metodo_accionBotones)


        # BOTON FORMA TABULAR
        # Hacemos el boton para navegar a la ventana de la tabla de usuarios
        self.botonFormaTabular = QPushButton("Forma Tabular")

        # Establecemos el ancho del boton
        self.botonFormaTabular.setFixedWidth(100)

        # Le ponemos los estilos
        self.botonFormaTabular.setStyleSheet("background-color: #008845;"
                                          "color: #FFFFFF;"
                                          "padding: 10px;"
                                          "margin-top: 10px;")

        self.botonFormaTabular.clicked.connect(self.metodo_botonFormaTabular)

        # Agregamos el boton botonContnuar al layout ladoDerecho
        self.vertical.addWidget(self.botonFormaTabular)



        # BOTON VOLVER
        # Hacemos el boton para devolver a la ventana anterior
        self.botonVolver = QPushButton("Volver")

        # Establecemos el ancho del boton
        self.botonVolver.setFixedWidth(90)

        # Le ponemos los estilos
        self.botonVolver.setStyleSheet("background-color: #008845;"
                                             "color: #FFFFFF;"
                                             "padding: 10px;"
                                             "margin-top: 10px;")

        self.botonVolver.clicked.connect(self.metodo_botonVolver)

        # Agregamos el boton botonContnuar al layout ladoDerecho
        self.vertical.addWidget(self.botonVolver)


        # --- OJO IMPORTANTE PONER AL FINAL ---

        # indicamos que el layout principal del fondo es horizontal
        self.fondo.setLayout(self.vertical)

    def metodo_accionBotones(self, cedulaUsuario):
        print(cedulaUsuario)

    def metodo_botonVolver(self):
        self.hide()
        self.ventanaAnterior.show()

    def metodo_botonFormaTabular(self):
        self.hide()
        self.ventana3 = Ventana3(self)
        self.ventana3.show()


if __name__ == "__main__":
    # Hacemos que la aplicacion de genere
    app = QApplication(sys.argv)

    # Crear un objeto de tipo Ventana1 con el nombre ventana1
    ventana2 = Ventana2()

    # Hacemos que el objeto ventana 1 se vea
    ventana2.show()

    # codigo para terminar la aplicación
    sys.exit(app.exec_())








































