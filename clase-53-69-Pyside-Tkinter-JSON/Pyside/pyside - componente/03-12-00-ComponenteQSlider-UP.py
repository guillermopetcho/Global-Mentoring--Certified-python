from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QApplication, QSpinBox, QDoubleSpinBox, QSlider


class Componentes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Componentes')
        # QSlider es para valores numericos enteros en un slider (deslizadora)
        # componente = QSlider(Qt.Horizontal)
        componente = QSlider()
        # componente.setMinimum(-5)
        # componente.setMaximum(8)
        componente.setRange(-5,8)

        # Publicamos este componente
        self.setCentralWidget(componente)


if __name__ == '__main__':
    app = QApplication([])
    ventana = Componentes()
    ventana.show()
    app.exec()