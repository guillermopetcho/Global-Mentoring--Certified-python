from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QApplication, QSpinBox


class Componentes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Componentes')
        # QSpinBox
        numero = QSpinBox()
        # Establecer valor minimo y el valor maximo
        # numero.setMinimum(-5)
        # numero.setMaximum(8)
        numero.setRange(-5,8)
        # Establecemos prefijo y sufijo
        numero.setPrefix('$')
        numero.setSuffix('c')
        # Establecemos el salto (step)
        numero.setSingleStep(3)

        # Publicamos este componente
        self.setCentralWidget(numero)


if __name__ == '__main__':
    app = QApplication([])
    ventana = Componentes()
    ventana.show()
    app.exec()