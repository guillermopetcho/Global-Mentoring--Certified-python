from PySide6.QtCore import Qt
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QMenu


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Menu Contextual')

    def contextMenuEvent(self, evento):
        menu_contextual = QMenu(self)
        boton_nuevo = QAction(QIcon('nuevo.png'),'Nuevo', self)
        boton_guardar = QAction(QIcon('guardar.png'),'Guardar',self)
        boton_salir = QAction('Salir', self)
        # Conectamos con la opcion triggered
        boton_nuevo.triggered.connect(self.click_boton_nuevo)
        boton_guardar.triggered.connect(self.click_boton_guardar)
        boton_salir.triggered.connect(self.click_boton_salir)
        menu_contextual.addAction(boton_nuevo)
        menu_contextual.addAction(boton_guardar)
        menu_contextual.addAction(boton_salir)
        # Recuperamos la posicion del cursor como posicion global de la ventana padre
        # Y ejecutamos el menu contextual
        menu_contextual.exec(evento.globalPos())

    def click_boton_nuevo(self, s):
        print('Opcion Nuevo...')

    def click_boton_guardar(self, s):
        print('Opcion Guardar...')

    def click_boton_salir(self, s):
        print('Opcion Salir...')

if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()