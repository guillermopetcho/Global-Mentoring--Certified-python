from functools import partial

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QLineEdit, QGridLayout, QPushButton


class Calculadora(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculadora')
        self.setFixedSize(235,235)
        self.componente_general = QWidget(self)
        self.setCentralWidget(self.componente_general)
        # Creamos un layout principal
        self.layout_principal = QVBoxLayout()
        self.componente_general.setLayout(self.layout_principal)
        # Metodos para crear la parte visual de la calculadora
        self._crear_area_captura()
        # Agregamos los botones
        self._crear_botones()
        # Conectamos las señales con los slots
        self._conectar_botones()

    def _crear_area_captura(self):
        self.linea_entrada = QLineEdit()
        # Modificamos algunas propiedades
        self.linea_entrada.setFixedHeight(35)
        self.linea_entrada.setAlignment(Qt.AlignRight)
        self.linea_entrada.setReadOnly(True)
        # Agregamos la linea de entrada al layout principal
        self.layout_principal.addWidget(self.linea_entrada)

    def _crear_botones(self):
        # Creamos un diccionario para definir cada boton (texto) de la calculadora
        self.botones = {}
        layout_botones = QGridLayout()
        # Texto | Posicion en el grid layout
        self.botones = {
            '7':(0,0),
            '8':(0,1),
            '9':(0,2),
            '/':(0,3),
            '4':(1,0),
            '5':(1,1),
            '6':(1,2),
            '*':(1,3),
            '1':(2,0),
            '2':(2,1),
            '3':(2,2),
            '-':(2,3),
            '0':(3,0),
            '.':(3,1),
            'C':(3,2),
            '+':(3,3),
            '=':(3,4)
        }

        # Creamos los botones y los agregamos al grid layout
        # La posicion es una tupla con dos valores (renglon-columna)
        for texto_boton, posicion in self.botones.items():
            self.botones[texto_boton] = QPushButton(texto_boton)
            self.botones[texto_boton].setFixedSize(40,40)
            # Publicamos el boton en el grid layout
            layout_botones.addWidget(self.botones[texto_boton], posicion[0],posicion[1])
        # Agregamos el layout de botones al layout principal
        self.layout_principal.addLayout(layout_botones)

    def _conectar_botones(self):
        # Recorrer cada boton del diccionario (key:value) (texto:PushButton)
        for texto_boton, boton in self.botones.items():
            if texto_boton not in {'=','C'}:
                # boton.clicked.connect(lambda: self._construir_expresion(texto_boton))
                boton.clicked.connect(partial(self._construir_expresion, texto_boton))
            # Conectamos el boton de limpiar texto (C=Clear en ingles)
            self.botones['C'].clicked.connect(self._limpiar_linea_entrada)
            # Conectamos el boton de igual (=)
            self.botones['='].clicked.connect(self._calcular_resultado)
            self.linea_entrada.returnPressed.connect(self._calcular_resultado)

    def _construir_expresion(self, texto_boton):
        expresion = self.obtener_texto() + texto_boton
        # Actualizamos la linea de entrada
        self.actualizar_texto(expresion)

    def obtener_texto(self):
        return self.linea_entrada.text()

    def actualizar_texto(self, texto):
        self.linea_entrada.setText(texto)
        self.linea_entrada.setFocus()

    def _limpiar_linea_entrada(self):
        self.actualizar_texto('')

    def _calcular_resultado(self):
        resultado = self._evaluar_expresion(self.obtener_texto())
        self.actualizar_texto(resultado)

    def _evaluar_expresion(self, expresion):
        try:
            # Utilizamos eval para evaluar la expresion
            resultado = str(eval(expresion))
        except Exception as e:
            resultado = 'Ocurrio un error'
        return resultado

if __name__ == '__main__':
    app = QApplication()
    calculadora = Calculadora()
    calculadora.show()
    app.exec()