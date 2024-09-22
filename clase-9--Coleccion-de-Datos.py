print('*** Manejo de Listas ***')

mi_lista = [1, 2, 3, 4, 5]
print(f'{mi_lista} -> Lista original')

# Largo de una lista
print(f'Largo de la lista: {len(mi_lista)}')

# Acceder a los elementos de la lista por indice
print(f'Accedemos al valor del indice 4: {mi_lista[4]}')
print(f'Accedemos al valor del indice -1: {mi_lista[-1]}')


print("----------------------------------")

print('*** Manejo de Listas ***')

mi_lista = [1, 2, 3, 4, 5]
print(f'{mi_lista} -> Lista original')

# Largo de una lista
print(f'Largo de la lista: {len(mi_lista)}')

# Acceder a los elementos de la lista por indice
print(f'Accedemos al valor del indice 4: {mi_lista[4]}')
print(f'Accedemos al valor del indice -1: {mi_lista[-1]}')

# Modificar los elementos de una lista
mi_lista[1] = 10
print(f'Modificamos el valor del indice 1: {mi_lista[1]}')

# Agregar un nuevo elemento al final de la lista
mi_lista.append(6)
print(f'{mi_lista} -> Se agregó el elemento 6')

# Añadir un nuevo elemento en un indice especifico
mi_lista.insert(2, 15)
print(f'{mi_lista} -> Se añadió el valor de 15 en el índice 2')
print("----------------------------------")


print('*** Manejo de Listas ***')

mi_lista = [1, 2, 3, 4, 5]
print(f'{mi_lista} -> Lista original')

# Largo de una lista
print(f'Largo de la lista: {len(mi_lista)}')

# Acceder a los elementos de la lista por indice
print(f'Accedemos al valor del indice 4: {mi_lista[4]}')
print(f'Accedemos al valor del indice -1: {mi_lista[-1]}')

# Modificar los elementos de una lista
mi_lista[1] = 10
print(f'Modificamos el valor del indice 1: {mi_lista[1]}')

# Agregar un nuevo elemento al final de la lista
mi_lista.append(6)
print(f'{mi_lista} -> Se agregó el elemento 6')

# Añadir un nuevo elemento en un indice especifico
mi_lista.insert(2, 15)
print(f'{mi_lista} -> Se añadió el valor de 15 en el índice 2')

# Eliminar elementos de una lista
# usando el metodo remove
mi_lista.remove(5)
print(f'{mi_lista} -> Se removió el valor 5')
# Removemos por indice con el metodo pop
mi_lista.pop(1) # Remueve el elemento del indice 1
print(f'{mi_lista} -> Se eliminó el índice 1')
# Eliminar usando la palabra del
del mi_lista[2]
print(f'{mi_lista} -> Se eliminó el índice 2')

# Obtener sublistas
sublista = mi_lista[1:3]  # genera una sublista del indice 1 al 2 (3 no se incluye)
print(f'Sublista [1:3]: {sublista}')
print("----------------------------------")


print(f'*** Iterar Listas ***')

nombres = ['Karla', 'Juan', 'Laura']

for nombre in nombres:
    print(nombre)

lista_heterogenea = [100, True, 'Ivonne']
print()
for elemento in lista_heterogenea:
    print(elemento)

print("----------------------------------")

print('*** Playlist de Canciones ***')

# Creamos la lista vacia
lista_reproduccion = []

numero_canciones = int(input('Cuantas canciones deseas agregar? '))

# iteramos cada elemento de la lista para agregar un nuevo elemento
for indice in range(numero_canciones):
    cancion = input(f'Proporciona la cancion {indice + 1}: ')
    lista_reproduccion.append(cancion)

# Ordenar la lista en orden alfabetico. sort
#lista_reproduccion.sort(reverse=True)
lista_reproduccion.sort()

# Mostar la lista lista iterando sus elementos
print('\nIteramos el playlist')
for cancion in lista_reproduccion:
    print(f'- {cancion}')
print("----------------------------------")

print('*** Promedio de Calificaciones ***')

total_calificaciones = int(input('Proporciona el numero de calificaciones a evaluar: '))
calificaciones = []

# iterar las calificaciones
for indice in range(total_calificaciones):
    calificacion = float(input(f'Calificación[{indice}] = '))
    calificaciones.append(calificacion)

# Imprimimos las calificaciones proporcionadas
print(f'\nLas calificaciones proporcionadas son: {calificaciones}')

# Calculamos el promedio de las calificaciones
# sum(iterable)
suma_calificaciones = sum(calificaciones)
promedio = suma_calificaciones / total_calificaciones
print(f'\nPromedio de las calificaciones: {promedio:.2f}')
print("----------------------------------")
print('*** Manejo de Tuplas ***')

mi_tupla = (1, 2, 3, 4, 5)
print(mi_tupla)
# No podemos modificar una tupla
#mi_tupla[0] = 10
#mi_tupla.append(6)

# Iteramos los elementos de una tupla
for elemento in mi_tupla:
    print(elemento, end=' ')

# Crear una tupla para una coordenada x,y
coordenadas = (3, 5)
# Accedemos a cada elemento de la tupla
print(f'\nCoordenada en el eje x: {coordenadas[0]}')
print(f'Coordenada en el eje y: {coordenadas[1]}')

# Crear una tupla unitaria
tupla_un_elemento = 10,
print(f'Tupla de un elemento: {tupla_un_elemento}')

# Tupla anidada
tuplas_anidada = (1, (2,3), (4,5))
print(f'Segundo elemento tupla anidada: {tuplas_anidada[1]}')
print("----------------------------------")
print('*** Desempaquetado de Tuplas ***')  # unpacking

producto = ('P001', 'Camisa', 20.00)

# Desempaquetado
id, descripcion, precio = producto

#Imprimir los valores
print(f'Tupla completa: {producto}')
# Valores independientes ya desempaquetados
print(f'Producto: id = {id}, descripcion = {descripcion}, precio = {precio}')
print("----------------------------------")
print('*** Combinación de Listas y Tuplas ***')

# definir una lista que almacena tuplas de productos
productos = [
    ('P001', 'Camiseta', 20.00),
    ('P002', 'Jeans', 30.00),
    ('P003', 'Sudadera', 40.00)
]

# Imprimir la informacion de cada producto
# y ademas calculamos el precio total
precio_total = 0

print('Información de los productos: ')
for producto in productos:
    #print(producto)
    id, descripcion, precio = producto  # unpacking
    print(f'Producto: id = {id}, descripcion = {descripcion}, precio = ${precio}')
    precio_total += precio # producto[2]
print(f'Precio total de los productos: ${precio_total}')
print("----------------------------------")
print('*** Manejo de Sets ***')
# Crear un conjunto
mi_set = {1, 2, 3, 4, 5, 4}
print(f'Mi set: {mi_set}')

# Agregar elementos al set
mi_set.add(6)
mi_set.add(7)

# Intentamos agregar un elemento duplicado
mi_set.add(3)

# Eliminar un elemento del conjunto
mi_set.remove(4)
print(f'Mi set modificado: {mi_set}')

# Iterar los elementos del set
for elemento in mi_set:
    print(elemento, end=' ')

# Comprobar si existe un elemento en el set
print(f'\nExiste el valor de 1 en el set? {1 in mi_set}')

# Obtener la longitud del set
print(f'Longitud del conjunto: {len(mi_set)}')
print("----------------------------------")
print('*** Operaciones con Set ***')

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

union = a | b
print(f'Union a | b: {union}')

interseccion = a & b
print(f'Intersección a & b {interseccion}')

diferencia = a - b
print(f'Diferencia a - b {diferencia}')
print("----------------------------------")
print('*** Lista de Suscriptores ***')

suscriptores = {'luisa@mail.com', 'marcos@mail.com', 'elena@mail.com'}
print(f'Lista de suscriptores inicial: {suscriptores}')

# Verifica si un nuevo suscriptor ya está en la lista
nuevo_suscriptor = 'karla@mail.com'
if nuevo_suscriptor in suscriptores:
    print(f'El nuevo suscriptor ya está en la lista {nuevo_suscriptor}')
else:
    suscriptores.add(nuevo_suscriptor)
    print(f'El nuevo suscriptor se ha agregado a la lista {nuevo_suscriptor}')
print(f'Lista de suscriptores: {suscriptores}')

# Eliminamos un suscriptor
suscriptor_eliminar = 'elena@mail.com'
suscriptores.remove(suscriptor_eliminar)
print(f'El suscriptor {suscriptor_eliminar} ha sido eliminado de la lista')
print(f'Lista de suscriptores: {suscriptores}')

# Verificamos la cantidad total de suscriptores
print(f'Cantidad total suscriptores: {len(suscriptores)}')

# Mostramos todos los suscriptores
print(f'--- Lista de Suscriptores ---')
for suscriptor in suscriptores:
    print(f'- {suscriptor}')
print("----------------------------------")
print('*** Diccionarios en Python ***')

# Creamos un dict de persona con clave y valor
persona = {
    'nombre': 'Sergio',
    'edad': 30,
    'ciudad': 'México'
}
print(f'Diccionario de persona: {persona}')

# Acceder a los elementos del diccionario
print(f'Nombre: {persona['nombre']}')
print(f'Edad: {persona.get('edad')}')
print(f'Ciudad: {persona.get('ciudad')}')
print("----------------------------------")
print('*** Diccionarios en Python ***')

# Creamos un dict de persona con clave y valor
persona = {
    'nombre': 'Sergio',
    'edad': 30,
    'ciudad': 'México'
}
print(f'Diccionario de persona: {persona}')

# Acceder a los elementos del diccionario
print(f'Nombre: {persona['nombre']}')
print(f'Edad: {persona.get('edad')}')
print(f'Ciudad: {persona.get('ciudad')}')

# Modificar un valor del diccionario
persona['edad'] = 35
print(f'Diccionario de persona: {persona}')

# Agregar un nuevo elemento
persona['profesion'] = 'Ingeniero'
print(f'Diccionario de persona: {persona}')

# Eliminar un elemento
del persona['ciudad']
print(f'Diccionario de persona: {persona}')

persona.pop('profesion')
print(f'Diccionario de persona: {persona}')

# Iterar los elementos de un dict (llave, valor)
for llave, valor in persona.items():
    print(f'Llave: {llave}, Valor: {valor}')

# Obtener los valores
print(f'\nValores del diccionario: ')
for valor in persona.values():
    print(f'- Valor: {valor}')

# Obtener las llaves
print(f'Impresión de las llaves del diccionario:')
for llave in persona.keys():
    print(f'- {llave}')
print("----------------------------------")
print('*** Agenda de Contactos ***')

agenda = {
    'Carlos': {
        'telefono': '55667711',
        'email': 'carlos@mail.com',
        'direccion': 'Calle Principal 132'
    },
    'María': {
        'telefono': '99887733',
        'email': 'maria@mail.com',
        'direccion': 'Avenida Central 456'
    },
    'Pedro': {
        'telefono': '55139078',
        'email': 'pedro@mail.com',
        'direccion': 'Plaza Mayor 789'
    }
}

print(agenda)

print("----------------------------------")
print('*** Agenda de Contactos ***')

agenda = {
    'Carlos': {
        'telefono': '55667711',
        'email': 'carlos@mail.com',
        'direccion': 'Calle Principal 132'
    },
    'María': {
        'telefono': '99887733',
        'email': 'maria@mail.com',
        'direccion': 'Avenida Central 456'
    },
    'Pedro': {
        'telefono': '55139078',
        'email': 'pedro@mail.com',
        'direccion': 'Plaza Mayor 789'
    }
}

print(agenda)

# Acceder a la informacion de un contacto en especifico
print(f'''Información del contacto de María:
    Teléfono: {agenda['María']['telefono']}
    Email: {agenda.get('María').get('email')}
    Dirección: {agenda.get('María').get('direccion')}''')

# Agregar un nuevo contacto
agenda['Ana'] = {
    'telefono': '55678392',
    'email': 'ana@mail.com',
    'direccion':'Calle Salvador Diaz 321'
}

print(agenda)

# Eliminar un contacto existente
agenda.pop('Pedro')
#del agenda['Pedro']
print(agenda)

# Mostramos los contactos de la agenda
print('\nContactos en la Agenda')
for nombre, detalles in agenda.items():
    print(f'''Nombre: {nombre}
    Teléfono: {detalles.get('telefono')}
    Email: {detalles.get('email')}
    Dirección: {detalles.get('direccion')}
''')
print("----------------------------------")
print('*** Listas y Diccionarios ***')

personas = [
    {
        'nombre': 'Regina',
        'apellido': 'Flores',
        'edad': 21
    },
    {
        'nombre': 'Alejandro',
        'apellido': 'Reyes',
        'edad': 32
    }
]

print(personas)

# Acceder a un diccionario desde una lista
print(f'''Detalle del primer elemento de la lista:
    Nombre: {personas[0].get('nombre')}
    Apellido: {personas[0].get('apellido')}
    Edad: {personas[0].get('edad')}''')

# Recorrer los elementos de la lista
print()
for contador, persona in enumerate(personas):
    print(f'{contador} - Persona: {persona}')
    #print(f'Detalle: Nombre: {persona.get('nombre')}, Apellido: {persona.get('apellido')}')
print("----------------------------------")
print('*** Sistema de Inventarios ***')

inventario = []

numero_productos = int(input('Cuantos productos deseas agregar al inventario? '))

for indice in range(numero_productos):
    print(f'Proporciona los valores del producto {indice + 1}')
    nombre = input('Nombre: ')
    precio = float(input('Precio: '))
    cantidad = int(input('Cantidad: '))
    # Creamos el diccionario con el detalle del producto
    producto = {'id': indice, 'nombre': nombre, 'precio': precio, 'cantidad': cantidad}
    # Agregamos el nuevo producto al inventario
    inventario.append(producto)

# Mostrar el inventario inicial
print(f'\nInventario inicial: {inventario}')
print("----------------------------------")
print('*** Sistema de Inventarios ***')

inventario = []

numero_productos = int(input('Cuantos productos deseas agregar al inventario? '))

for indice in range(numero_productos):
    print(f'Proporciona los valores del producto {indice + 1}')
    nombre = input('Nombre: ')
    precio = float(input('Precio: '))
    cantidad = int(input('Cantidad: '))
    # Creamos el diccionario con el detalle del producto
    producto = {'id': indice, 'nombre': nombre, 'precio': precio, 'cantidad': cantidad}
    # Agregamos el nuevo producto al inventario
    inventario.append(producto)

# Mostrar el inventario inicial
print(f'\nInventario inicial: {inventario}')

# Buscar un producto por id
id_buscar = int(input('\nIngresa el ID del producto a buscar: '))
producto_encontrado = None
for producto in inventario:
    if producto.get('id') == id_buscar:
        producto_encontrado = producto
        break

if producto_encontrado is not None:
    print('Información de producto encontrado: ')
    print(f'''Id: {producto_encontrado.get('id')}
    Nombre: {producto_encontrado.get('nombre')}
    Precio: {producto_encontrado.get('precio')}
    Cantidad: {producto_encontrado.get('cantidad')}''')
else:
    print(f'Producto con id {id_buscar} NO encontrado')

# Mostrar el inventario detallado
print(f'\n--- Inventario Detallado ---')
for producto in inventario:
    print(f'''Id: {producto.get('id')}
    Nombre: {producto.get('nombre')}
    Precio: ${producto.get('precio'):.2f}
    Cantidad: {producto.get('cantidad')}''')
print("----------------------------------")
print('*** Compresion de Listas ***')

# Una lista con el cuadrado de cada numero
numeros = [1, 2, 3, 4, 5]
cuadrados = [x**2 for x in numeros]
print(cuadrados)

# Lista de numeros pares
numeros = range(10+1)
pares = [x for x in numeros if x % 2 == 0]
print(pares)

# Lista saludando a cada nombre
nombres = ['Ana', 'Jerónimo', 'Carlos']
saludando = [f'Hola {nombre}' for nombre in nombres]
print(saludando)
print("----------------------------------")
