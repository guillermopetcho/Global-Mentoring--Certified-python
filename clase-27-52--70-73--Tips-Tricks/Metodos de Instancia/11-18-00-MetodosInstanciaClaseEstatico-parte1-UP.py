# Metodos de instancia, clase y static y sus diferencias
class MiClase:

    def metodo_instancia(self):
        # Retornamos una tupla
        return 'Metodo de instancia ejecutado...', self

    @classmethod
    def metodo_clase(cls):
        # Retornar una tupla
        return 'Metodo de clase ejecutado...', cls

    @staticmethod
    def metodo_estatico():
        return 'Metodo estatico ejecutado...'
