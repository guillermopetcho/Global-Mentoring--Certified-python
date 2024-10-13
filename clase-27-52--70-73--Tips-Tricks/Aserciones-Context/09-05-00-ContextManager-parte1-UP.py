
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
