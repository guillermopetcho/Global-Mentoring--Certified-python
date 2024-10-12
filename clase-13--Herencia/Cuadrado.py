from FiguraGeometrica import FiguraGeometrica
from Color import Color

class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        # super().__init__(lado)
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    def calcular_area(self):
        return self.alto * self.ancho

    def __str__(self):
        return f'{FiguraGeometrica.__str__(self)} {Color.__str__(self)}'


"""
explicacion:

La clase cuadrado hereda de dos clases, FiguraGeometrica y Color
def __init__(self, lado, color): es el constructor que se encarga de inicializar tanto los atributos
geometricos como el color del cuadrado

def __init__(self, lado, color):
    FiguraGeometrica.__init__(self, lado, lado) #inicializa los atributos geometricos
    Color.__init__(self, color) #inicializa el atributo color

Esto llama al constructor de la clase Color para inicializar el atributo color de la clase base Color.

    Nota: En lugar de usar super().__init__() (que llama a los constructores de las clases base en orden de herencia), 
    aquí se llama explícitamente a los constructores de cada clase base. 
    Esto puede ser útil en casos donde se quiere un control más preciso de la herencia múltiple.

Metodo calcular_area:

    def calcular_area(self):
    return self.alto * self.ancho

como FiguraGeometrica probablemente tiene atributos alto y ancho
inicializados con el valor de lado en el constructor, el area
del cuadrado es simplemente la multiplicacion de estos dos
valores.

Metodo __str__:

este metodo controla como se representa el objeto el Cuadrado
como una cadena

def __str__(self):
    return f'{FiguraGeometrica.__str__(self)} {Color.__str__(self)}'

Este metodo combina las representaciones de cadena tanto de la
clase FiguraGeometrica como de la clase Color. En lugar de 
sobrescribir el comportamiento completamente, reutiliza el 
metodo __str__ de ambas clases bases.
    FiguraGeometrica.__str__(self) devolvera una representacion
    relacionada con las dimensiones del cuadrado.

    Color.__str__(self) devolvera la representacion del color
    (el valor del atributo _color)
Esto garantiza que la informacion del cuadrado contenga tanto
su geometria como su color.


resumen:


herencia multiple "cuadrado" hereda de FiguraGeometrica y Color.

constructor inicializa las dimensiones geometricas como el color del cuadrado
llamado explicitamente a los constructores de la clase base

metodo calcular_area: Calcula el area multiplicando alto por ancho
(ambos heredados de FiguraGeometrica).

Metodo __str__: Combina las representaciones en cadena de las 
dos clases base(FiguraGeometrica y Color)










"""