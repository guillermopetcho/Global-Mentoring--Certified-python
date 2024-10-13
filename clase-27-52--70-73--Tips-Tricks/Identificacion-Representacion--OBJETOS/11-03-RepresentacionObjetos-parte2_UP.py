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

class AutoStr:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def __str__(self):
        return f'str: Marca: {self.marca}, Modelo: {self.modelo}, Color: {self.color}'

    # def __repr__(self):
    #     return f'repr: Marca: {self.marca}, Modelo: {self.modelo}, Color: {self.color}'

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'{self.marca!r}, {self.modelo}, {self.color!r})')

audi_a1 = AutoStr('Audi', 'a1', 'blanco')
# Tenemos diferentes formas de imprimir el objeto
print(audi_a1)
print(audi_a1.__str__())
print(str(audi_a1))
print('{}'.format(audi_a1))
print(f'{audi_a1}')

# Sin embargo es mas recomendable usar __repr__ en lugar de __str__
# Ej. cualquier coleccion utiliza repr en lugar de str para mostrar la informacion
print([audi_a1])
# Tambien usando !r
print(f'{audi_a1!r}')

# Tambien manualmente podemos escoger que metodo utilizar
print(str(audi_a1))
print(repr(audi_a1))