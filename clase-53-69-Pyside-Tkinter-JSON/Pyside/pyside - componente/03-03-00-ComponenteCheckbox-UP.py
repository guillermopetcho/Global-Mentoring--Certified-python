from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QApplication, QCheckBox


class Componentes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Componentes')
        # Creamos un nuevo checkbox
        checkbox = QCheckBox('Este es un checkbox')
        # Activamos el 3er estado
        # Tenemos 3 estados (0-Apagado, 1-Sin estado, 2-Encendido)
        checkbox.setTristate(True)
        # Conectar la señal de cambio de componente
        checkbox.stateChanged.connect(self.mostrar_estado)
        # Publicamos este componente
        self.setCentralWidget(checkbox)

    def mostrar_estado(self, estado):
        print('Estado checkbox:', estado)
        # Trabajamos con las constantes
        if estado == Qt.Checked:
            print('Checkbox encendido')
        elif estado == Qt.PartiallyChecked:
            print('Checkbox sin estado o parcialmente checado')
        elif estado == Qt.Unchecked:
            print('Checkbox apagado')
        else:
            print('Checkbox con estado inválido')


if __name__ == '__main__':
    app = QApplication([])
    ventana = Componentes()
    ventana.show()
    app.exec()