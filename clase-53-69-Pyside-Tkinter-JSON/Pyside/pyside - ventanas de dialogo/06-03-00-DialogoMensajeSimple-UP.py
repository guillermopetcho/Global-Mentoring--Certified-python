from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton, QDialog, QDialogButtonBox, QVBoxLayout, QLabel, \
    QMessageBox


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Dialogos')
        # Agregamos un boton
        boton = QPushButton('Mostrar dialogo')
        boton.clicked.connect(self.click_boton)

        # Publicamos el boton
        self.setCentralWidget(boton)

    def click_boton(self, s):
        print(f'Click sobre boton: {s}')
        # Creamos el dialogo
        dialogo = QMessageBox(self)
        dialogo.setWindowTitle('Dialogo Simple')
        dialogo.setText('Ventana de Dialogo Simple')
        valor_retornado = dialogo.exec()
        # Imprimir el valor retornado
        print(f'Valor retornado: {valor_retornado}')
        if valor_retornado == QMessageBox.Ok:
            print('Regreso el valor Ok')
        else:
            print('Regreso un valor distinto de Ok')



if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()