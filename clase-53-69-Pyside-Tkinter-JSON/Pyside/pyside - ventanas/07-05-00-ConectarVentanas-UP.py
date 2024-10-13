from random import randint
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QMainWindow, QPushButton, QApplication, QLineEdit


class NuevaVentana(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.etiqueta = QLabel(f'Nueva ventana: {randint(0,100)}')
        layout.addWidget(self.etiqueta)
        self.setLayout(layout)

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.nueva_ventana = None
        # Solo creamos una instancia, no varias
        self.nueva_ventana = NuevaVentana()
        self.boton = QPushButton('Mostrar/Ocultar Nueva Ventana')
        self.boton.clicked.connect(self.mostrar_nueva_ventana)
        # Definimos una entrada de texto
        self.entrada_texto = QLineEdit()
        self.entrada_texto.textChanged.connect(self.nueva_ventana.etiqueta.setText)
        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.boton)
        layout.addWidget(self.entrada_texto)
        contenedor = QWidget()
        contenedor.setLayout(layout)
        self.setCentralWidget(contenedor)

    def mostrar_nueva_ventana(self, checado):
        # Debido a que ya se creo el objeto ventana, ya solo lo mostramos
        # Revisamos si ya esta visible, si es asi la ocultamos, sino la mostramos
        # No se modifica el numero aleatorio, es la misma ventana
        if self.nueva_ventana.isVisible():
            self.nueva_ventana.hide()
        else:
            self.nueva_ventana.show()

if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()