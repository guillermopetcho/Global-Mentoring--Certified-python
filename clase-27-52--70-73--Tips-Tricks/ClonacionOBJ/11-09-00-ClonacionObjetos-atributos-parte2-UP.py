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

# Clase Rectangulo utiliza dos puntos (superior izquierdo e inferior derecho)
class Rectangulo:
    def __init__(self, sup_izq, inf_der):
        self.sup_izq = sup_izq
        self.inf_der = inf_der

    def __repr__(self):
        return f'Rectangulo({self.sup_izq!r}, {self.inf_der!r})'

rect_a = Rectangulo(Punto(0,1), Punto(3,4))
# Copia superficial (shallow)
rect_b = copy.copy(rect_a)
print(f'Copia superficial rectangulos')
print(f'Rectangulo a: {rect_a}')
print(f'Rectangulo b: {rect_b}')
# debido a que la copia fue superficial, un cambio en un punto afecta al otro rectangulo
rect_a.inf_der.y = 6
print(f'Cambio en un punto afecta al otro rectangulo (shallow copy)')
print(f'Rectangulo a: {rect_a}')
print(f'Rectangulo b: {rect_b}')

# Creacion copia profunda (deep copy)
rect_c = copy.deepcopy(rect_a)
# Modificamos un valor en un punto, no afecta al otro rectangulo (copia profunda)
rect_c.sup_izq.x = 2
rect_a.sup_izq.y = 3
print(f'Cambio en un punto NO afecta al otro rectangulo (deep copy)')
print(f'Rectangulo a: {rect_a}')
print(f'Rectangulo c: {rect_c}')
