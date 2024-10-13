class Clase1:
    def __init__(self):
        print('Clase1.__init__')

    def metodo(self):
        print('Método clase1')

class Clase2(Clase1):
    def __init__(self):
        print('Clase2.__init__')

    def metodo(self):
        print('Método clase2')

class Clase3(Clase1):
    def __init__(self):
        print('Clase3.__init__')

    def metodo(self):
        print('Método clase3')

class Clase4(Clase2, Clase3):

    def metodo(self):
        print('Método clase4')

# Creamos objeto clase4
clase4 = Clase4()
# __bases__
print(Clase4.__bases__)
# mro
print(Clase4.__mro__)
# cual método se ejecuta
clase4.metodo()