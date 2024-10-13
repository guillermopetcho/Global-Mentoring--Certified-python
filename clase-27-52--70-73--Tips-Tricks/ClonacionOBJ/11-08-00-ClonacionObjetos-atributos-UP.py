import copy

# Copia de atributos de objetos

# Definimos una clase de tipo Punto 2D
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Punto({self.x!r}, {self.y!r})'

    def __eq__(self, otro):
        return isinstance(otro, Punto) and self.x == otro.x and self.y == otro.y

punto_a = Punto(2,3)
punto_b = copy.copy(punto_a)
# Copia poco profunda (shallow), son distintos objetos
print(f'Copia poco profunda (shallow)')
print(f'Punto a: {punto_a}')
print(f'Punto b: {punto_b}')
print(f'Son objetos con el mismo contenido:? {punto_a == punto_b}')
print(f'Son los mismo objetos (misma referencia)?: {punto_a is punto_b}')
