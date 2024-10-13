from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton


class NuevaVentana(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Nueva Ventana')

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Ventanas')
        self.boton = QPushButton('Mostrar nueva ventana')
        self.boton.clicked.connect(self.mostrar_nueva_ventana)
        self.setCentralWidget(self.boton)

    def mostrar_nueva_ventana(self, estado):
        self.nueva_ventana = NuevaVentana()
        self.nueva_ventana.show()

if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()