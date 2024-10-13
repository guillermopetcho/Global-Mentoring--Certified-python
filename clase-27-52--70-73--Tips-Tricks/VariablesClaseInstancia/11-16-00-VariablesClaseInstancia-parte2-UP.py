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

# Si queremos modificar el no_patas para todos los perros
Perro.no_patas = 5
print(layla.no_patas, venus.no_patas, Perro.no_patas)

# Si queremos modificar el no_patas para un solo perro
venus.no_patas = 6 # Se crea una variable de instancia (oculta a la variable de clase)
print(layla.no_patas, venus.no_patas, Perro.no_patas)

# Imprimimos el valor de la variable de instancia y ademas la variable de clase
print(venus.no_patas, venus.__class__.no_patas)

# Si creamos una variable desde la clase
Perro.nombre = 'Clase Perro'
print(layla.nombre, venus.nombre, Perro.nombre)

# Si definimos una variable de clase que no esta en los objetos
Perro.no_orejas = 2
print(layla.no_orejas, venus.no_orejas, Perro.no_orejas)