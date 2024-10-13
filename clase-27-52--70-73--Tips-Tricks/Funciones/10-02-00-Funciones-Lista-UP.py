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