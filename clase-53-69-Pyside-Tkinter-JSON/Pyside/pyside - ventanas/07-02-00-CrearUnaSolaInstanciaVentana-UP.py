from random import randint

from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QVBoxLayout, QLabel


class NuevaVentana(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Nueva Ventana')
        layout = QVBoxLayout()
        self.etiqueta = QLabel(f'Nueva Ventana: {randint(0,100)}')
        layout.addWidget(self.etiqueta)
        self.setLayout(layout)

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.nueva_ventana = None
        self.setWindowTitle('Ventanas')
        self.boton = QPushButton('Mostrar nueva ventana')
        self.boton.clicked.connect(self.mostrar_nueva_ventana)
        self.setCentralWidget(self.boton)

    def mostrar_nueva_ventana(self, estado):
        if self.nueva_ventana is None:
            self.nueva_ventana = NuevaVentana()
            self.nueva_ventana.show()

if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()