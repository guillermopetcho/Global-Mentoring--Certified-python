# Signals son notificaciones emitidas por los widgets
# Slots permite recibir y procesar esos eventos o notificaciones
import sys

from PySide6.QtWidgets import QMainWindow, QPushButton, QApplication


class VentanaPrincipal(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Signals y Slots')
        boton = QPushButton('Click aquí')
        boton.setCheckable(True)
        # Conectamos el evento (signal) click con el slot (evento_click)
        boton.clicked.connect(self.evento_click)

        # Publicamos el botón en la ventana
        self.setCentralWidget(boton)

    # Creamos el método (slot) que procesa o consume el evento (signal)
    def evento_click(self):
        print('Has hecho click...')


if __name__ == '__main__':
    # Creamos la aplicación
    app = QApplication([])
    # Creamos una instancia de nuestra clase
    ventana = VentanaPrincipal()
    ventana.show()

    # Ejecutamos la aplicación
    sys.exit(app.exec())