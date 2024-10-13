import sys

from PySide6.QtWidgets import QApplication, QWidget


class VentanaPySide():
    def __init__(self):
        self.ventana = QWidget()
        self.ventana.setWindowTitle('Nueva Ventana PySide')
        self.ventana.resize(600, 400)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # Creamos una instancia del objeto ventana
    ventana1 = VentanaPySide()
    ventana1.ventana.show()
    # Se ejecuta la ventana
    app.exec()
