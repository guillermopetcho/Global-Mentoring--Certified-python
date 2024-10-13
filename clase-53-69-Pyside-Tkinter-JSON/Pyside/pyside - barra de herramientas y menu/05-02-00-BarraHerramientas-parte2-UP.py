from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
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
        self.addToolBar(barra)

        # Agregamos un elemento a nuestra barra de herramientas
        boton_accion = QAction('Boton', self)
        # Agregamos el boton a la barra
        barra.addAction(boton_accion)

        # Barra de estado
        self.setStatusBar(QStatusBar(self))

        # Mostramos mensaje del boton accion
        boton_accion.setStatusTip('Este es el boton de la barra')

        # Asociamos el evento click
        boton_accion.triggered.connect(self.click_boton_barra)

        # Hacemos checable el boton
        boton_accion.setCheckable(True)

    def click_boton_barra(self, s):
        print(f'Recibiendo click {s}')

if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()