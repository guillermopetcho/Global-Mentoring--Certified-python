# __str__ su objetivo es que la informacion sea legible para el usuario
# __repr__ su objetivo es que la informacion no sea ambigua
# se utilizar para hacer debugging (formato tipo constructor)
# La implementacion por default del metodo str llama a repr

class Auto:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

# Por default solo es muestra el nombre de la clase y id del objeto (direccion memoria)
audi_a3 = Auto('audi', 'A3', 'rojo')
print(f'Audi: {audi_a3}')

