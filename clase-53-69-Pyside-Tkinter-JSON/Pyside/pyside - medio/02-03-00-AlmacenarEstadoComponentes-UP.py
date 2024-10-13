# Signals y slots
import sys

from PySide6.QtWidgets import QMainWindow, QPushButton, QApplication


class VentanaPrincipal(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Signals y Slots')
        # Boton
        boton = QPushButton('Click aquí')
        # Conectamos el evento checado (por default es False)
        boton.setCheckable(True)
        # Conectamos otro slot al evento checar
        boton.clicked.connect(self.evento_checar)
        # Conectamos el evento (signal) click con el slot (evento_click)
        boton.clicked.connect(self.evento_click)
        # Publicamos el botón
        self.setCentralWidget(boton)

    def evento_checar(self, checar):
        self.boton_checado = checar
        print('Checado?', self.boton_checado)

    # Creamos el método (slot) que procesa o consume el evento (signal)
    def evento_click(self):
        print('Has hecho click')
        # Accedemos al estado del boton (checado)
        print('Botón checado desde evento click?', self.boton_checado)

if __name__ == '__main__':
    # Creamos el objeto aplicación
    app = QApplication([])
    # Creamos una instancia de nuestra clase
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())