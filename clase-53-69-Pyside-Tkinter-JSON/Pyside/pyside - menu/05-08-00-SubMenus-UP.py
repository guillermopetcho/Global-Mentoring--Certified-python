from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QAction, QIcon, QKeySequence
from PySide6.QtWidgets import QMainWindow, QApplication, QLabel, QToolBar, QStatusBar, QCheckBox


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Barra de Herramientas')
        # publicamos una etiqueta
        etiqueta = QLabel('Hola')
        etiqueta.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(etiqueta)

        # Creamos la barra de herramientas
        barra = QToolBar('Mi barra de herramientas')
        barra.setIconSize(QSize(16,16))
        # Configuracion para mostrar la barra de herramientas
        # barra.setToolButtonStyle(Qt.ToolButtonFollowStyle)
        # barra.setToolButtonStyle(Qt.ToolButtonTextOnly)
        # barra.setToolButtonStyle(Qt.ToolButtonIconOnly)
        # barra.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        # barra.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.addToolBar(barra)

        # Agregamos un elemento a nuestra barra de herramientas
        boton_nuevo = QAction(QIcon('nuevo.png'), 'Nuevo', self)
        # Agregamos el boton a la barra
        barra.addAction(boton_nuevo)

        # Barra de estado
        self.setStatusBar(QStatusBar(self))

        # Mostramos mensaje del boton accion
        boton_nuevo.setStatusTip('Nuevo archivo')

        # Asociamos el evento click
        boton_nuevo.triggered.connect(self.click_boton_nuevo)

        # Hacemos checable el boton
        # boton_nuevo.setCheckable(True)

        # Agregamos la opcion de guardar archivo
        boton_guardar = QAction(QIcon('guardar.png'),'Guardar', self)
        barra.addAction(boton_guardar)
        boton_guardar.setStatusTip('Guardar Archivo')
        boton_guardar.triggered.connect(self.click_boton_guardar)

        barra.addSeparator()

        barra.addWidget(QCheckBox())
        barra.addWidget(QLabel('Salir'))

        menu = self.menuBar()
        menu_archivo = menu.addMenu('&Archivo')
        menu_archivo.addAction(boton_nuevo)

        # Agregamos una segunda opcion
        menu_archivo.addAction(boton_guardar)

        # Agregamos un separador
        menu_archivo.addSeparator()

        # Agregamos una tercera opcion
        boton_salir = QAction('Salir', self)
        menu_archivo.addAction(boton_salir)

        # Submenu ayuda
        boton_acerca_de = QAction(QIcon('acerca.png'), 'Acerca De', self)
        menu_ayuda = menu.addMenu('Ayuda')
        menu_ayuda.addAction(boton_acerca_de)

        boton_acerca_de.triggered.connect(self.click_boton_acerca_de)

        # Agregamos un submenu
        menu_archivo.addMenu(menu_ayuda)

    def click_boton_acerca_de(self, s):
        print(f'Acerca de... {s}')

    def click_boton_guardar(self, s):
        print(f'Guardando archivo... {s}')

    def click_boton_nuevo(self, s):
        print(f'Nuevo archivo... {s}')


if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()