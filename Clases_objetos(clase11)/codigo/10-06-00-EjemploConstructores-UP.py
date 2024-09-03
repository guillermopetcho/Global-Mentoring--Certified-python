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
