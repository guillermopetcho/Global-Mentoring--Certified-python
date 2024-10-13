from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QApplication, QListWidget


class Componentes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Componentes')
        # Componente QListWidget se parece al combobox
        lista = QListWidget()
        # Agregamos elementos
        lista.addItem('Uno')
        lista.addItems(['Dos','Tres'])
        # Monitoreamos el cambio del elemento seleccionado, tanto el elemento con el texto
        lista.currentItemChanged.connect(self.cambio_elemento)
        lista.currentTextChanged.connect(self.cambio_texto)

        # Publicamos este componente
        self.setCentralWidget(lista)

    def cambio_elemento(self, nuevo_elemento):
        print(f'Nuevo elemento seleccionado: {nuevo_elemento.text()}')

    def cambio_texto(self, nuevo_texto):
        print(f'Nuevo texto seleccionado: {nuevo_texto}')

if __name__ == '__main__':
    app = QApplication([])
    ventana = Componentes()
    ventana.show()
    app.exec()