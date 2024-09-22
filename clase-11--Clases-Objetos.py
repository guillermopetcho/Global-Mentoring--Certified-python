#####################################################################################
#####################################################################################
#####################################################################################
#####################################################################################
#####################################################################################

# Definicion de una clase
class Persona:

    def inicializar_persona(self, nombre, apellido):
        # Creamos los atributos de la clase
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_persona(self):
        print(f'''Persona: 
        Nombre: {self.nombre}
        Apellido: {self.apellido}''')


#####################################################################################
#####################################################################################
#####################################################################################
#####################################################################################
#####################################################################################

# Definicion de una clase
class Persona:

    def inicializar_persona(self, nombre, apellido):
        # Creamos los atributos de la clase
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_persona(self):
        print(f'''Persona: 
        Nombre: {self.nombre}
        Apellido: {self.apellido}''')

# Creacion de objetos
if __name__ == '__main__':
    # Creacion de un primer objeto
    persona1 = Persona()  # Crea un objeto vacio en memoria
    persona1.inicializar_persona('Layla', 'Acosta')
    persona1.mostrar_persona()

#####################################################################################
#####################################################################################
#####################################################################################
#####################################################################################
#####################################################################################


# Definicion de una clase
class Persona:

    def inicializar_persona(self, nombre, apellido):
        # Creamos los atributos de la clase
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_persona(self):
        print(f'''Persona: 
        Nombre: {self.nombre}
        Apellido: {self.apellido}''')

# Creacion de objetos
if __name__ == '__main__':
    # Creacion de un primer objeto
    persona1 = Persona()  # Crea un objeto vacio en memoria
    persona1.inicializar_persona('Layla', 'Acosta')
    persona1.mostrar_persona()

    # Creamos un segundo objeto
    persona2 = Persona() # Crea un objeto vacio en memoria
    persona2.inicializar_persona('Ian', 'Sánchez')
    persona2.mostrar_persona()


#####################################################################################
#####################################################################################
#####################################################################################
#####################################################################################
#####################################################################################


# Definicion de una clase
class Persona:

    #  Constructor
    def __init__(self, nombre, apellido):
        # Creamos los atributos de la clase
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_persona(self):
        print(f'''Persona: 
        Nombre: {self.nombre}
        Apellido: {self.apellido}''')


# Creacion de objetos
if __name__ == '__main__':
    # Creacion de un primer objeto
    persona1 = Persona('Layla', 'Acosta')  # Crea un objeto vacio en memoria
    persona1.mostrar_persona()

    # Creamos un segundo objeto
    persona2 = Persona('Ian', 'Sánchez') # Crea un objeto vacio en memoria
    #persona2.inicializar_persona('Ian', 'Sánchez')
    persona2.mostrar_persona()


#####################################################################################
#####################################################################################
#####################################################################################
#####################################################################################
#####################################################################################


# Definicion de una clase
class Persona:

    #  Constructor
    def __init__(self, nombre, apellido):
        # Creamos los atributos de la clase
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_persona(self):
        print(f'''Persona: 
        Nombre: {self.nombre}
        Apellido: {self.apellido}''')
        print(f'Dir. mem self: {id(self)}')
        print(f'Dir. mem hex self: {hex(id(self))}')


# Creacion de objetos
if __name__ == '__main__':
    # Creacion de un primer objeto
    persona1 = Persona('Layla', 'Acosta')  # Crea un objeto vacio en memoria
    persona1.mostrar_persona()
    print(f'Dir. mem persona1: {id(persona1)}')
    print(f'Dir. mem hex persona1: {hex(id(persona1))}')

    # Creamos un segundo objeto
    persona2 = Persona('Ian', 'Sánchez') # Crea un objeto vacio en memoria
    #persona2.inicializar_persona('Ian', 'Sánchez')
    persona2.mostrar_persona()
    print(f'Dir. mem persona2: {id(persona2)}')
    print(f'Dir. mem hex persona2: {hex(id(persona2))}')


#####################################################################################
#####################################################################################
#####################################################################################
#####################################################################################
#####################################################################################

class Aritmetica:
    def __init__(self, operando1, operando2):
        self.operando1 = operando1
        self.operando2 = operando2

    def sumar(self):
        resultado = self.operando1 + self.operando2
        print(f'Resultado suma: {resultado}')

    def restar(self):
        resultado = self.operando1 - self.operando2
        print(f'Resultado resta: {resultado}')

    def multiplicar(self):
        resultado = self.operando1 * self.operando2
        print(f'Resultado multiplicación: {resultado}')

    def dividir(self):
        resultado = self.operando1 / self.operando2
        print(f'Resultado división: {resultado}')


# Programa principal
if __name__ == '__main__':
    print('*** Ejemplo Clase Artimética ***')
    aritmetica1 = Aritmetica(5, 7)
    aritmetica1.sumar()
    aritmetica1.restar()
    # Segundo objeto
    aritmetica2 = Aritmetica(12, 16)
    print()
    aritmetica2.sumar()
    aritmetica2.restar()


#####################################################################################
#####################################################################################
#####################################################################################
#####################################################################################
#####################################################################################

class Aritmetica:
    # Python solamente toma el ultimo constructor
    # def __init__(self, operando1):
    #     self.operando1 = operando1

    def __init__(self, operando1=None, operando2=None):
        self.operando1 = operando1
        self.operando2 = operando2

    def sumar(self):
        resultado = self.operando1 + self.operando2
        print(f'Resultado suma: {resultado}')

    def restar(self):
        resultado = self.operando1 - self.operando2
        print(f'Resultado resta: {resultado}')

    def multiplicar(self):
        resultado = self.operando1 * self.operando2
        print(f'Resultado multiplicación: {resultado}')

    def dividir(self):
        resultado = self.operando1 / self.operando2
        print(f'Resultado división: {resultado}')


# Programa principal
if __name__ == '__main__':
    print('*** Ejemplo Clase Artimética ***')
    aritmetica1 = Aritmetica(5, 7)
    print('Primer objeto')
    aritmetica1.sumar()
    aritmetica1.restar()
    # Segundo objeto
    print('Segundo objeto')
    aritmetica2 = Aritmetica(12, 16)
    print()
    aritmetica2.sumar()
    aritmetica2.restar()
    # Tercer objeto
    print('Tercer objeto')
    aritmetica3 = Aritmetica(7)
    aritmetica3.operando2 = 9
    aritmetica3.sumar()
    # Cuarto objeto
    print('Cuarto objeto')
    aritmetica4 = Aritmetica()
    aritmetica4.operando1 = 2
    aritmetica4.operando2 = 8
    aritmetica4.sumar()
    # Quinto objeto
    print('Quinto objeto')
    aritmetica5 = Aritmetica(operando2=4, operando1=3)
    aritmetica5.sumar()



#####################################################################################
#####################################################################################
#####################################################################################
#####################################################################################
#####################################################################################

#10-12-00-Ejemplo-Encapsulamiento-UP

# Definimos la clase coche
class Coche:

    def __init__(self, marca, modelo, color):
        self.marca = marca # Atributo publico
        self._modelo = modelo # Atributo protegido
        self.__color = color # Atributo privado

    def conducir(self):
        print(f'''Conduciendo el coche:
        Marca: {self.marca}
        Modelo: {self._modelo}
        Color: {self.__color}''')


# Programa principal
if __name__ == '__main__':
    # Creacion de un primer coche
    coche1 = Coche('Toyota', 'Yaris', 'Azul')
    coche1.conducir()
    # No deberiamos acceder a los atributos que no sean publicos
    coche1.marca = 'Toyota 2'
    coche1._modelo = 'Yaris 2'  # Esto no es una buena practica
    coche1.__color = 'Azul 2'  # igoro la modificacion
    coche1._Coche__color = 'Azul 3'  # Es una mala practica
    coche1.conducir()

#####################################################################################
#####################################################################################
#####################################################################################
#####################################################################################
#####################################################################################


# Definimos la clase coche
class Coche:

    def __init__(self, marca, modelo, color):
        self._marca = marca # Atributo protegido
        self._modelo = modelo # Atributo protegido
        self._color = color # Atributo protegido

    def conducir(self):
        print(f'''Conduciendo el coche:
        Marca: {self._marca}
        Modelo: {self._modelo}
        Color: {self._color}''')

    def get_marca(self):
        return self._marca

    def set_marca(self, marca):
        self._marca = marca

    def get_modelo(self):
        return self._modelo

    def set_modelo(self, modelo):
        self._modelo = modelo

    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color


# Programa principal
if __name__ == '__main__':
    # Creacion de un primer coche
    coche1 = Coche('Toyota', 'Yaris', 'Azul')
    coche1.conducir()
    # No deberiamos acceder a los atributos que no sean publicos
    coche1.set_marca('Toyota 2')
    coche1.set_modelo('Yaris 2')
    coche1.set_color('Azul 2')
    coche1.conducir()


#####################################################################################
#####################################################################################
#####################################################################################
#####################################################################################
#####################################################################################

"""
Atributos de instancia: Son únicos para cada objeto. Definidos con self.atributo dentro de __init__.
Atributos de clase: Son compartidos por todos los objetos de la clase. Definidos fuera de los métodos.
Atributos privados: Son atributos que se pretenden proteger del acceso externo. Se identifican con __atributo.
"""

# Definimos la clase coche
class Coche:

    def __init__(self, marca, modelo, color):
        self._marca = marca # Atributo protegido
        self._modelo = modelo # Atributo protegido
        self._color = color # Atributo protegido

    def conducir(self):
        print(f'''Conduciendo el coche:
        Marca: {self._marca}
        Modelo: {self._modelo}
        Color: {self._color}''')

    # def get_marca(self):
    #     return self._marca

    @property # Definir el metodo get de manera mas pythonica
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color


# Programa principal
if __name__ == '__main__':
    # Creacion de un primer coche
    coche1 = Coche('Toyota', 'Yaris', 'Azul')
    coche1.conducir()
    # No deberiamos acceder a los atributos que no sean publicos
    coche1.marca = 'Toyota 2'
    coche1.modelo = 'Yaris 2'
    coche1.color = 'Azul 2'
    coche1.conducir()
    # Atributo de marca del coche 1
    coche1.marca = 'Toyota 3'
    print(f'Atributo marca coche1: {coche1.marca}')



#####################################################################################
#####################################################################################
#####################################################################################
#####################################################################################
#####################################################################################

# Definimos la clase coche
class Coche:

    def __init__(self, marca, modelo, color):
        self._marca = marca # Atributo protegido
        self._modelo = modelo # Atributo protegido
        self._color = color # Atributo protegido

    def conducir(self):
        print(f'''Conduciendo el coche:
        Marca: {self._marca}
        Modelo: {self._modelo}
        Color: {self._color}''')

    # def get_marca(self):
    #     return self._marca

    @property # Definir el metodo get de manera mas pythonica
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color


# Programa principal
if __name__ == '__main__':
    # Creacion de un primer coche
    coche1 = Coche('Toyota', 'Yaris', 'Azul')
    coche1.conducir()
    # No deberiamos acceder a los atributos que no sean publicos
    coche1.marca = 'Toyota 2'
    coche1.modelo = 'Yaris 2'
    coche1.color = 'Azul 2'
    # Intentar agregar un nuevo atributo
    setattr(coche1, 'nuevo_atributo', 'Valor nuevo atributo')
    coche1.nuevo_atributo2 = 'Valor nuevo atributo 2'
    print(f'Atributos del coche1: {coche1.__dict__}')
    coche1.conducir()
    print(coche1.nuevo_atributo)
    print(f'Nuevo atributo coche1 {coche1.nuevo_atributo2}')
    # Segundo objeto
    coche2 = Coche('Chevrolet', 'Trax', 'Blanco')
    coche2.conducir()
    print(f'Atributos del coche2: {coche2.__dict__}')
    #print(f'Nuevo atributo coche2 {coche2.nuevo_atributo}')
    #print(f'Nuevo atributo coche2 {coche2.nuevo_atributo2}')




#####################################################################################
#####################################################################################
#####################################################################################
#####################################################################################
#####################################################################################




class Aritmetica:

    def __init__(self, operando1=None, operando2=None):
        self._operando1 = operando1
        self._operando2 = operando2

    def sumar(self):
        resultado = self._operando1 + self._operando2
        print(f'Resultado suma: {resultado}')

    def restar(self):
        resultado = self._operando1 - self._operando2
        print(f'Resultado resta: {resultado}')

    def multiplicar(self):
        resultado = self._operando1 * self._operando2
        print(f'Resultado multiplicación: {resultado}')

    def dividir(self):
        resultado = self._operando1 / self._operando2
        print(f'Resultado división: {resultado}')

    @property
    def operando1(self):
        return self._operando1

    @operando1.setter
    def operando1(self, operando1):
        self._operando1 = operando1

    @property
    def operando2(self):
        return self._operando2

    @operando2.setter
    def operando2(self, operando2):
        self._operando2 = operando2

# Programa principal
if __name__ == '__main__':
    print('*** Ejemplo Clase Artimética ***')
    aritmetica1 = Aritmetica(5, 7)
    print('Primer objeto')
    print(f'Valor operando1 del objeto artimetica1: {aritmetica1.operando1}')
    print(f'Valor operando2 del objeto artimetica1: {aritmetica1.operando2}')
    aritmetica1.sumar()
    aritmetica1.restar()
    aritmetica1.operando1 = 9
    aritmetica1.operando2 = 15
    print(f'Valor operando1 del objeto artimetica1: {aritmetica1.operando1}')
    print(f'Valor operando2 del objeto artimetica1: {aritmetica1.operando2}')
    aritmetica1.sumar()
    aritmetica1.restar()

    # Segundo objeto
    print('Segundo objeto')
    aritmetica2 = Aritmetica(12, 16)
    print(f'Valor operando1 del objeto artimetica2: {aritmetica2.operando1}')
    print(f'Valor operando2 del objeto artimetica2: {aritmetica2.operando2}')
    print()
    aritmetica2.sumar()
    aritmetica2.restar()
    # Tercer objeto
    print('Tercer objeto')
    aritmetica3 = Aritmetica(7)
    aritmetica3.operando2 = 9
    aritmetica3.sumar()
    # Cuarto objeto
    print('Cuarto objeto')
    aritmetica4 = Aritmetica()
    aritmetica4.operando1 = 2
    aritmetica4.operando2 = 8
    aritmetica4.sumar()
    # Quinto objeto
    print('Quinto objeto')
    aritmetica5 = Aritmetica(operando2=4, operando1=3)
    aritmetica5.sumar()





#####################################################################################
#####################################################################################
#####################################################################################
#####################################################################################
#####################################################################################




class Persona:

    atributo_clase = 0

    def __init__(self, atributo_instancia):
        self.atributo_instancia = atributo_instancia

# Programa principal
if __name__ == '__main__':
    print(f'*** Atributos de Clase ***')
    print(f'Atributo de Clase: {Persona.atributo_clase}')
    # Modificamos el atributo de clase
    Persona.atributo_clase = 10
    print(f'Atributo de Clase: {Persona.atributo_clase}')

    # Creamos un objeto persona1
    persona1 = Persona(15)
    print(f'Atributo de Clase desde persona1: {persona1.atributo_clase}')
    print(f'Atributo de instancia desde persona1: {persona1.atributo_instancia}')

    # Creamos un objeto persona2
    persona2 = Persona(30)
    print(f'Atributo de Clase desde persona2: {persona2.atributo_clase}')
    print(f'Atributo de instancia desde persona2: {persona2.atributo_instancia}')



#####################################################################################
#####################################################################################
#####################################################################################
#####################################################################################
#####################################################################################




class Persona:
    # Atributo clase
    contador_personas = 0

    def __init__(self, nombre, apellido):
        # Incrementamos el valor del atributo de clase
        Persona.contador_personas += 1
        self.id = Persona.contador_personas
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_persona(self):
        print(f'Persona: {self.id}, {self.nombre}, {self.apellido}')

if __name__ == '__main__':
    print('*** Ejemplo Contador de Objetos de tipo Persona ***')
    persona1 = Persona('Gerardo', 'Perez')
    persona1.mostrar_persona()

    # Segundo objeto
    persona2 = Persona('Daniel', 'Sanchez')
    persona2.mostrar_persona()

    # Imprimir el valor del contador de objetos de personas
    print(f'Contador objetos Persona: {Persona.contador_personas}')


#####################################################################################
#####################################################################################
#####################################################################################
#####################################################################################
#####################################################################################

class Persona:
    # Atributo clase
    contador_personas = 0

    def __init__(self, nombre, apellido):
        # Incrementamos el valor del atributo de clase
        Persona.contador_personas += 1
        self.id = Persona.contador_personas
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_persona(self):
        print(f'Persona: {self.id}, {self.nombre}, {self.apellido}')

    @staticmethod
    def get_contador_personas_estatico():
        print('Método estático')
        return Persona.contador_personas

    @classmethod
    def get_contador_personas_clase(cls):
        print('Método de clase')
        return cls.contador_personas


if __name__ == '__main__':
    print('*** Ejemplo Contador de Objetos de tipo Persona ***')
    persona1 = Persona('Gerardo', 'Perez')
    persona1.mostrar_persona()

    # Segundo objeto
    persona2 = Persona('Daniel', 'Sanchez')
    persona2.mostrar_persona()

    # Imprimir el valor del contador de objetos de personas
    print(f'Contador objetos Persona: {Persona.contador_personas}')
    print(f'Contador objetos Persona (persona1): {persona1.contador_personas}')
    print(f'Contador objetos Persona (static): {Persona.get_contador_personas_estatico()}')
    print(f'Contador objetos Persona (clase): {Persona.get_contador_personas_clase()}')



#####################################################################################
#####################################################################################
#####################################################################################
#####################################################################################
#####################################################################################

class Empleado:

    contador_empleados = 0

    def __init__(self, nombre, departamento):
        self.nombre = nombre
        self.departamento = departamento
        Empleado.contador_empleados += 1

    @classmethod
    def obtener_total_empleados(cls):
        return cls.contador_empleados


#####################################################################################
#####################################################################################
#####################################################################################
#####################################################################################
#####################################################################################

from sistema_empleados.empleado import Empleado


class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []

    def contratar_empleado(self, nombre, departamento):
        empleado = Empleado(nombre, departamento)
        self.empleados.append(empleado)

    def obtener_numero_empleados_departamento(self, departamento):
        contador_empleados_por_departamento = 0
        for empleado in self.empleados:
            if empleado.departamento == departamento:
                contador_empleados_por_departamento += 1
        return contador_empleados_por_departamento


#####################################################################################
#####################################################################################
#####################################################################################
#####################################################################################
#####################################################################################



class Libro:
    def __init__(self, titulo, autor, genero):
        self._titulo = titulo
        self._autor = autor
        self._genero = genero

    @property
    def titulo(self):
        return self._titulo

    @property
    def autor(self):
        return self._autor

    @property
    def genero(self):
        return self._genero



#####################################################################################
#####################################################################################
#####################################################################################
#####################################################################################
#####################################################################################

class Biblioteca:

    def __init__(self, nombre):
        self._nombre = nombre
        self._libros = []

    def agregar_libro(self, libro):
        self._libros.append(libro)

    def buscar_libros_por_autor(self, autor):
        for libro in self._libros:
            if libro.autor.lower() == autor.lower():
                self.mostrar_libro(libro)

    def buscar_libros_por_genero(self, genero):
        for libro in self._libros:
            if libro.genero.lower() == genero.lower():
                self.mostrar_libro(libro)

    def mostrar_todos_los_libros(self):
        print(f'\nTodos los libros de la biblioteca {self._nombre}')
        for libro in self._libros:
            self.mostrar_libro(libro)

    def mostrar_libro(self, libro):
        print(f'Libro -> Título: {libro.titulo}, Autor: {libro._autor}, '
              f'Género: {libro.genero}')

    @property
    def nombre(self):
        return self._nombre

    @property
    def libros(self):
        return self._libros


#####################################################################################
#####################################################################################
#####################################################################################
#####################################################################################
#####################################################################################


