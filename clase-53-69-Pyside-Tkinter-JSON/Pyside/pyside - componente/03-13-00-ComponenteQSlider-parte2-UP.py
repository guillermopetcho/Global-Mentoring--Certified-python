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

        # Conectamos a las señales
        componente.valueChanged.connect(self.cambio_valor)
        componente.sliderMoved.connect(self.slider_cambio_posicion)
        componente.sliderPressed.connect(self.slider_presionado)
        componente.sliderReleased.connect(self.slider_liberado)

        # Publicamos este componente
        self.setCentralWidget(componente)

    def cambio_valor(self, nuevo_valor):
        print(f'Nuevo valor: {nuevo_valor}')

    def slider_cambio_posicion(self, nueva_posicion):
        print(f'Nueva posicion: {nueva_posicion}')

    def slider_presionado(self):
        print('Slider presionado')

    def slider_liberado(self):
        print('Slider liberado')

if __name__ == '__main__':
    app = QApplication([])
    ventana = Componentes()
    ventana.show()
    app.exec()