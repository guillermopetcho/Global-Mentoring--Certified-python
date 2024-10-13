from PySide6.QtGui import QPalette, QColor
from PySide6.QtWidgets import QWidget, QMainWindow, QApplication, QVBoxLayout, QHBoxLayout, QGridLayout, QStackedLayout, \
    QPushButton


class Color(QWidget):
    def __init__(self, nuevo_color):
        super().__init__()
        # Indicamos que se puede agregar un color de fondo
        self.setAutoFillBackground(True)
        paletaColores = self.palette()
        # Creamos el componente de color de fondo aplicando el nuevo color
        paletaColores.setColor(QPalette.Window, QColor(nuevo_color))
        # Aplicamos el nuevo color al componente
        self.setPalette(paletaColores)

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Layouts en PySide')
        # Creamos los layouts
        layout_principal = QVBoxLayout()
        layout_botones = QHBoxLayout()
        self.layout_tipo_stack = QStackedLayout()
        # Agregamos los layout hijos al layout principal
        layout_principal.addLayout(layout_botones)
        layout_principal.addLayout(self.layout_tipo_stack)

        # Creamos los botones
        boton_rojo = QPushButton('Rojo')
        # Publicar este boton en el layout de botones
        layout_botones.addWidget(boton_rojo)
        # Publicamos el color rojo al layout de tipo stack
        self.layout_tipo_stack.addWidget(Color('red'))

        # Creamos el boton azul
        boton_azul = QPushButton('Azul')
        layout_botones.addWidget(boton_azul)
        self.layout_tipo_stack.addWidget(Color('blue'))

        # Creamos el boton amarillo
        boton_amarillo = QPushButton('Amarillo')
        layout_botones.addWidget(boton_amarillo)
        self.layout_tipo_stack.addWidget(Color('yellow'))

        # Creamos un componente generico para poder publicar el layout
        componente = QWidget()
        componente.setLayout(layout_principal)
        self.setCentralWidget(componente)

if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()