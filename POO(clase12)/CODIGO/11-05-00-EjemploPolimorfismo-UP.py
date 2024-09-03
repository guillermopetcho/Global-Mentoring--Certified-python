# Polimorfismo
class Animal:
    def hacer_sonido(self):
        print('Hago un pitido')

class Perro(Animal):
    # pass
    def hacer_sonido(self):
        print('Puedo ladrar')

class Gato(Animal):
    def hacer_sonido(self):
        print('Puedo maullar')

print('*** Ejemplo Polimorfismo ***')
print('Clase Padre Animal: ')
animal1 = Animal()
animal1.hacer_sonido()
# Definimos un objeto de la clase Perro
print('\nClase Hija Perro: ')
perro1 = Perro()
perro1.hacer_sonido()  # Polimorfismo
# Definimos un objeto de la clase Gato
print('\nClase Hija Gato: ')
gato1 = Gato()
gato1.hacer_sonido()