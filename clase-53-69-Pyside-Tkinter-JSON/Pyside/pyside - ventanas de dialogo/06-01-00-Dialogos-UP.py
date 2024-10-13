from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton, QDialog


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Dialogos')
        # Agregamos un boton
        boton = QPushButton('Mostrar dialogo')
        boton.clicked.connect(self.click_boton)

        # Publicamos el boton
        self.setCentralWidget(boton)

    def click_boton(self, s):
        print(f'Click sobre boton: {s}')
        # Creamos el dialogo
        dialogo = QDialog(self)
        dialogo.setWindowTitle('Ayuda')
        # Crea un nuevo event loop
        # Se bloquea la ventana padre (ventana modal)
        # y solo podemos interactuar con la nueva ventana
        # Para ejecutar la ventana modal
        dialogo.exec()


if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()