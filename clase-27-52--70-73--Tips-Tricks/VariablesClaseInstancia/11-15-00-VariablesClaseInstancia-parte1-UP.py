# Diferencia entre variables de clase y de instancia (objeto)
class Perro:
    no_patas = 4 # <- Variable de Clase

    def __init__(self, nombre):
        self.nombre = nombre # <- Variable de instancia (del objeto)

# Definimos algunos objetos
layla = Perro('Layla')
venus = Perro('Venus')
# Cada objeto tiene su propio atributo de nombre
print(layla.nombre, venus.nombre)

# La variable de clase se puede acceder con el nombre de la clase o con los objetos
print(layla.no_patas, venus.no_patas, Perro.no_patas)

# Si tratamos de acceder la variable de instancia desde la clase no es posible
# print(Perro.nombre)