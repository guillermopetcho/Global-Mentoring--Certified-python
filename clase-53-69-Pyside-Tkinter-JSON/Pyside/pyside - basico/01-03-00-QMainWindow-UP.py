import sys

from PySide6.QtWidgets import QApplication, QMainWindow

# Clase base de Qt (PySide)
# Se encarga de procesar los eventos (event loop)
app = QApplication()
# Crear un objeto ventana
# Cualquier componente puede ser una ventana en PySide
# ventana = QPushButton('Botón PySide')
ventana = QMainWindow()
# Cambiar el título
ventana.setWindowTitle('Hola Mundo con PySide')
# Modificamos el tamaño de la ventana
ventana.resize(600, 400)
# Mostrar la ventana
ventana.show()
# Se ejecuta la aplicación
sys.exit(app.exec())

