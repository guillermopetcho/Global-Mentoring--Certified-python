import sys

from PySide6.QtWidgets import QMainWindow, QApplication


class VentanaPySide(QMainWindow):
    def __init__(self):
        # Llamamos al método init de la clase padre
        super().__init__()
        self.setWindowTitle('POO con PySide')
        self.resize(600,400)

if __name__ == '__main__':
    app = QApplication([])
    # Creamos un objeto de tipo ventana
    ventana = VentanaPySide()
    ventana.show()
    # Ejecutamos la ventana
    sys.exit(app.exec())