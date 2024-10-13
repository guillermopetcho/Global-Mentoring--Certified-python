# ABC - Abstract Base Class
# Nos permite asegurar que las clases que heredan implementen los metodos

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
clase_concreta.metodo_1()
# El metodo2, se llama el metodo heradado
# clase_concreta.metodo_2()
