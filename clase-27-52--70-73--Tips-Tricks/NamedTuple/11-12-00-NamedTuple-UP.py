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