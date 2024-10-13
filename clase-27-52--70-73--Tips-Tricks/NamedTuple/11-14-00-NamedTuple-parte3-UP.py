# Namedtuples son una extension del tipo tupla
# Son una alternativa para escribir clases (atributos tipos inmutables)
# Asignar un identicador a cada elemento de la tupla
from collections import namedtuple
# Definimos una clase con atributos inmutables pero usando namedtuple
Persona1 = namedtuple('Persona1', 'nombre apellido edad')
# Creamos una instancia de la clase (se agrega un constructor por default con los atributos)
persona1 = Persona1('Juan','Perez',28)
# En automatico se crea un metodo __repr__ con los atributos proporcionados
print(persona1)

# Creamos nuestra clase con los atributos usando una lista
Persona2 = namedtuple('Persona2', ['nombre', 'apellido', 'edad'])
persona2 = Persona2('Karla', 'Gomez', 30)
print(persona2)

# Podemos acceder a los atributos de manera individual por nombre
print(f'Nombre: {persona2.nombre}')
print(f'Apellido: {persona2.apellido}')
print(f'Edad: {persona2.edad}')
# Acceder a los atributos por indice
print(f'Nombre: {persona2[0]}')
print(f'Apellido: {persona2[1]}')
print(f'Edad: {persona2[2]}')
# Podemos convertir los valores a una tupla
print(tuple(persona2))
# Podemos hacer unpacking de los elementos de la tupla
nombre, apellido, edad = persona2
print(f'Valores tupla persona: {nombre}, {apellido}, {edad}')
# Podemos hacer unpacking pansado como argumento
print(*persona2)
# Las tuplas son inmutables al igual que namedtuple
# persona2.edad = 30

# Subclases de namedtuples
class Persona3(Persona2):
    # Agregamos un nuevo metodo a la clase hija
    def convertir_mayusculas(self):
        return f'Nombre completo: {self.nombre.upper()} {self.apellido.upper()}'

persona3 = Persona3('Maria','Lara',35)
print(persona3)
print(persona3.convertir_mayusculas())

# Existe otra forma de hacer extends de la clase (la forma recomendada con namedtuple)
Persona4 = namedtuple('Persona4', Persona2._fields + ('email',))
# Creamos un objeto persona4 con el nuevo atributo de email
persona4 = Persona4('Armando','Quintero', 38, 'aquintero@mail.com')
print(persona4)

# Metodos de ayuda (built-in) en namedtuple
print(persona4._fields)
# Ej. convetir a un diccionario
diccionario_persona4 = persona4._asdict()
print(diccionario_persona4)
