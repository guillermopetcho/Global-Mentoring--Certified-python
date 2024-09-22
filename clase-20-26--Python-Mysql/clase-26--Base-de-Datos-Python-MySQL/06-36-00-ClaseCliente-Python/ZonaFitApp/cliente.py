class Cliente:
    def __init__(self, id, nombre, apellido, membresia):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.membresia = membresia

    def __str__(self):
        return (f'Id: {self.id}, Nombre: {self.nombre}, '
                f'Apellido: {self.apellido}, Membresia: {self.membresia}')