import sys

from PySide6.QtWidgets import QApplication, QWidget

# Clase base de Qt (PySide)
# Se encarga de procesar los eventos (event loop)
app = QApplication()
# Crear un objeto ventana
ventana = QWidget()
# Cambiar el título
ventana.setWindowTitle('Hola Mundo con PySide')
# Modificamos el tamaño de la ventana
ventana.resize(600, 400)
# Mostrar la ventana
ventana.show()
# Se ejecuta la aplicación
sys.exit(app.exec())

