from contextlib import contextmanager

with open('prueba.txt','w') as archivo:
    archivo.write('hola desde Python')

# Esto es equivalente a:
# archivo = open('prueba.txt','w')
# try:
#     archivo.write('hola desde Python')
# finally:
#     archivo.close()

# Esto NO es equivalente
archivo = open('prueba.txt', 'w')
archivo.write('hola sin with')
# Esto no asegura el cierre de recursos en caso de error
archivo.close()

# Manejo de Context Manager en Clases
# 1. Implementando el protocolo con las funciones (__enter__) y (__exit__)
# 2. Utilizando la libreria de contextlib

# Veamos la opcion 1
class ManejoArchivos:
    def __init__(self, nombre):
        self.nombre = nombre

    def __enter__(self):
        self.archivo = open(self.nombre, 'w')
        return self.archivo

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.archivo:
            self.archivo.close()

# Este metodo es un generador, en primer lugar adquiere el recurso
# posteriomente suspende temporalmente la ejecucion al utilizar yield
# cuando de ser utilizado este metodo, regresa a la ejecucion y cierra el recurso
@contextmanager
def manejador_archivos(nombre):
    try:
        archivo = open(nombre, 'w')
        yield archivo
    finally:
        archivo.close()

if __name__ == '__main__':
    # Prueba implementando el protocolo de Context Manager
    with ManejoArchivos('prueba.txt') as archivo:
        archivo.write('prueba desde ManejoArchivo')

    # Prueba con la libreria contextlib
    with manejador_archivos('prueba.txt') as archivo:
        archivo.write('prueba desde decorador')
        archivo.write('\nadios')