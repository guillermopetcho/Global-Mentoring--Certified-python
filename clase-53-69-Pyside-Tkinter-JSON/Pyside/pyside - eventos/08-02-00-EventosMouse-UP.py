from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Eventos')
        self.etiqueta = QLabel('Da click en esta ventana')
        self.setCentralWidget(self.etiqueta)

    def mousePressEvent(self, evento):
        # Preguntamos por el boton del mouse que lanzo el evento
        if evento.button() == Qt.LeftButton:
            self.etiqueta.setText('mousePressEvent Boton Izquierdo')
        elif evento.button() == Qt.MiddleButton:
            self.etiqueta.setText('mousePressEvent Boton Central')
        elif evento.button() == Qt.RightButton:
            self.etiqueta.setText('mousePressEvent Boton Derecho')

    def mouseReleaseEvent(self, evento):
        if evento.button() == Qt.LeftButton:
            self.etiqueta.setText('mouseReleaseEvent Boton Izquierdo')
        elif evento.button() == Qt.MiddleButton:
            self.etiqueta.setText('mouseReleaseEvent Boton Central')
        elif evento.button() == Qt.RightButton:
            self.etiqueta.setText('mouseReleaseEvent Boton Derecho')

    def mouseDoubleClickEvent(self, evento):
        if evento.button() == Qt.LeftButton:
            self.etiqueta.setText('mouseDoubleClickEvent Boton Izquierdo')
        elif evento.button() == Qt.MiddleButton:
            self.etiqueta.setText('mouseDoubleClickEvent Boton Central')
        elif evento.button() == Qt.RightButton:
            self.etiqueta.setText('mouseDoubleClickEvent Boton Derecho')

if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()