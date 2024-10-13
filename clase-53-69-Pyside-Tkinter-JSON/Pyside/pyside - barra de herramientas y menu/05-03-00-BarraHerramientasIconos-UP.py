from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QMainWindow, QApplication, QLabel, QToolBar, QStatusBar


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

    def click_boton_nuevo(self, s):
        print(f'Nuevo archivo {s}')


if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()