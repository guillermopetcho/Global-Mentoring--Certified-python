from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow, QLabel, QApplication


class Componentes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Componentes')
        self.setFixedSize(500, 600)
        # Creamos un componente de tipo etiqueta (Label)
        etiqueta = QLabel('Hola')
        etiqueta.setPixmap(QPixmap('layla.jpg'))
        etiqueta.setScaledContents(True)
        # Publicamos este componente
        self.setCentralWidget(etiqueta)


if __name__ == '__main__':
    app = QApplication([])
    ventana = Componentes()
    ventana.show()
    app.exec()