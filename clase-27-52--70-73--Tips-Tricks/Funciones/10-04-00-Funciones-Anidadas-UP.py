# Las funciones en python son ciudadanos de primera clase
def mayusculas(texto):
    return texto.upper()

# Uso normal de una funcion
print(mayusculas('Hola'))

# Uso de una funcion como un objeto
# Asignar la referencia de la funcion a una variable, sin los parentesis
variable_funcion = mayusculas
print(f'Funcion mayusculas: {mayusculas}')
print(f'Variable funcion: {variable_funcion}')

# Utilizamos la variable funcion en cualquier momento
print(variable_funcion('Nuevo texto'))

# Para demostrar que las funciones son objetos, eliminamos la referencia original
# del mayusculas

# Aun asi, podemos utilizar la funcion con la variable_funcion
print(variable_funcion('Saludos...'))
# print(mayusculas('Ya se elimino....'))

# Podemos saber el nombre por default que se le asigna a una funcion
print(f'Nombre por default de la funcion: {variable_funcion.__name__}')
print(mayusculas('Nombre por default'))

#############################
# Como almacenar una funcion es una estructura de datos (list)
lista_funciones = [mayusculas, variable_funcion, str.upper]
print(lista_funciones)

for funcion in lista_funciones:
    print(funcion, funcion('Saludos desde la funcion'))

# O podemos acceder directamente a la funcion que deseemos
print(lista_funciones[1]('Saludos desde variable_funcion'))

#####################
# Podemos pasar funciones a otras funciones
# Este tipo de funciones se conocen como higher-order functions
def saludar(argumento_funcion):
    # Usamos la funcion que recibimos como argumento y devolvemos la referencia
    referencia_funcion_retornada = argumento_funcion('Hola, saludos desde mi funcion')
    print(referencia_funcion_retornada)

# Llamamos la funcion saludar, pasamos la referencia de una funcion como argumento
saludar(mayusculas)

# Podemos pasar una nueva implementacion de la funcion que pasamos como argumento
def minusculas(texto):
    return texto.lower()

saludar(minusculas)

# El clasico ejemplo de higher-order functions es la funcion map
# Esta funcion toma una funcion como referencia, y un iterable, llama a la funcion
# en cada elemento del iterable proporcionado
print(list(map(mayusculas, ['texto1', 'texto2', 'texto3'])))
print(list(map(minusculas, ['Texto1', 'Texto2', 'Texto3'])))

###################
# Funciones Anidadas
def mostrar(texto):
    # Definicion de la funcion interna o anidada
    def convetir_minusculas(t):
        return t.lower()
    # Una vez definida la funcion interna, la mandamos llamar
    return convetir_minusculas(texto)

# Cada vez que se llama la funcion mostrar
# se crea la funcion interna convetir_minusculas
print(mostrar('Desde funcion anidada...'))

# No podemos utilizar la funcion interna desde fuera de la funcion externa
# convetir_minusculas('texto1')
# mostrar.convertir_minusculas('texto1')