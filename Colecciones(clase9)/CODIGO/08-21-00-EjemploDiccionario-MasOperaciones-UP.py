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