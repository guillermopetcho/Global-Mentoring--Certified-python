# Signals y slots
import sys

from PySide6.QtWidgets import QMainWindow, QPushButton, QApplication


class VentanaPrincipal(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Signals y Slots')
        # Boton
        self.boton = QPushButton('Click aquí')
        # Asociamos la señal de click al slot evento_click
        self.boton.clicked.connect(self.evento_click)
        # Conectar a la señal de cambio de título
        self.windowTitleChanged.connect(self.cambio_titulo_aplicacion)
        # Publicamos el botón
        self.setCentralWidget(self.boton)

    def evento_click(self):
        # Cambiar el texto del botón y el título de la ventana
        self.boton.setText('Nuevo texto botón')
        self.boton.setEnabled(False)
        self.setWindowTitle('Nuevo título de la Aplicación')
        print('evento_click')

    def cambio_titulo_aplicacion(self, nuevo_titulo):
        print(f'Nuevo título aplicación: {nuevo_titulo}')


if __name__ == '__main__':
    # Creamos el objeto aplicación
    app = QApplication([])
    # Creamos una instancia de nuestra clase
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())