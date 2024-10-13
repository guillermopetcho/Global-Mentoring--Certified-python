from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QMenu


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Menu Contextual')

    def contextMenuEvent(self, evento):
        menu_contextual = QMenu(self)
        menu_contextual.addAction(QAction('Nuevo', self))
        menu_contextual.addAction(QAction('Guardar',self))
        menu_contextual.addAction(QAction('Salir', self))
        # Recuperamos la posicion del cursor como posicion global de la ventana padre
        # Y ejecutamos el menu contextual
        menu_contextual.exec(evento.globalPos())


if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()