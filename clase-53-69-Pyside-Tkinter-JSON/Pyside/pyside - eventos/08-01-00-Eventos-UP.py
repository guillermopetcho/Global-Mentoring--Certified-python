from PySide6.QtWidgets import QApplication, QMainWindow, QLabel


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Eventos')
        self.etiqueta = QLabel('Da click en esta ventana')
        self.setCentralWidget(self.etiqueta)

    def mouseMoveEvent(self, evento):
        self.etiqueta.setText('Evento mouseMoveEvent detectado')

    def mousePressEvent(self, evento):
        self.etiqueta.setText('Evento mousePressEvent detectado')

    def mouseReleaseEvent(self, evento):
        self.etiqueta.setText('Evento mouseReleaseEvent detectado')

    def mouseDoubleClickEvent(self, evento):
        self.etiqueta.setText('Evento mouseDoubleClickEvent detectado')

if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()