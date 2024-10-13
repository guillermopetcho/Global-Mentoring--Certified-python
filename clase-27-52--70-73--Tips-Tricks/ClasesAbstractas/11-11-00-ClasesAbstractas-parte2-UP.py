# ABC - Abstract Base Class
# Nos permite asegurar que las clases que heredan implementen los metodos
# ABC permite escribir una jerarquia de clases mas robuta y escribir codigo mas mantenible

# Ej. Sin usar ABC y los posibles problemas
from abc import ABCMeta, abstractmethod


class ClaseBase1:
    def metodo_1(self):
        raise NotImplementedError

    def metodo_2(self):
        raise NotImplementedError

class ClaseConcreta1(ClaseBase1):
    # Implementacion de la clase padre
    def metodo_1(self):
        print('Metodo 1 implementado...')

    # El metodo 2 no se va a implementar
    # Esto ya es un problema por que no se reporta la falta de implementacion

# Hay un problema, se puede instanciar la clase Base
clase_base = ClaseBase1()
# clase_base.metodo_1()

# Esto funciona segun lo esperado
clase_concreta = ClaseConcreta1()
# clase_concreta.metodo_1()
# El metodo2, se llama el metodo heradado
# clase_concreta.metodo_2()

# Vamos a resolver los detalles anteriores usando ABC (Abstract Base Class)
class ClaseBase2(metaclass=ABCMeta):
    # No tenemos la agregar la implementacion al ser un metodo abstracto
    @abstractmethod
    def metodo_1(self):
        pass

    @abstractmethod
    def metodo_2(self):
        pass

class ClaseConcreta2(ClaseBase2):
    def metodo_1(self):
        print('Metodo 1 implementado...')

    # Estamos obligados a implementar todos los metodos abstractos
    def metodo_2(self):
        print('Metodo 2 implementado...')

# Intentamos crear un objeto de la clase base
# Esto no es posible
# clase_base = ClaseBase2()

# Instanciamos la clase concreta 2
clase_concreta = ClaseConcreta2()
clase_concreta.metodo_1()
clase_concreta.metodo_2()



