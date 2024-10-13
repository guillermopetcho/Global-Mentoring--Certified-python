# Los decoradores permiten extender y modificar el comportamiento de las funciones
# Ejemplos comunes: logging, seguridad, caching
# Un decorador es codigo reutilizable
# Primer ejemplo de un decorador
def decorador_envolvente(funcion_a_decorar):
    # Recibir la funcion y regresarla
    print('Estamos dentro de la funcion decoradora')
    return funcion_a_decorar

# Ahora utilicemos este decorador
def saludar():
    return 'Saludos desde mi funcion...'

# Llamamos manualmente el decorador (no es lo comun en Python)
funcion_retornada = decorador_envolvente(saludar)
print(funcion_retornada)

@decorador_envolvente
def saludar_funcion_a_decorar():
    return 'Saludos desde funcion a decorar...'

# La funcion devuelta por el decorador se ejecuta de manera inmediata, sin llamarla
print(saludar_funcion_a_decorar())

# Decorador que convierte el texto a mayusculas
def mayusculas(funcion_a_decorar):
    def envolvente():
        # Mandamos a llamar la funcion original (closure)
        print('antes de la llamada a la funcion a decorar...')
        resultado_original = funcion_a_decorar()
        print('despues de la llamada a la funcion a decorar...')
        resultado_modificado = resultado_original.upper()
        return resultado_modificado
    return envolvente

@mayusculas
def saludar_minusculas():
    return 'hola..'

# La funcion devuelta por el decorador (envolvente) se ejecuta de manera inmediata
print(saludar_minusculas())

###########################
# Decoradores multiples
# <strong><em>Hola</em></strong>
def negritas(funcion):
    def funcion_envolvente():
        return '<strong>' + funcion() + '</strong>'
    return funcion_envolvente

def enfatizar(funcion):
    def funcion_envolvente():
        return '<em>' + funcion() + '</em>'
    return funcion_envolvente

@negritas
@enfatizar
def saludar_html():
    return 'Hola con HTML'

print(saludar_html())

##################
# Decoradores con Argumentos
# *args y **kwargs
def decorador_con_argumentos(funcion):
    def funcion_envolvente(*args, **kwargs):
        print('Se esta ejecutando decorador')
        print('args: ', args)
        print('kwargs: ', kwargs)
        # Modificar los argumentos antes de enviarlos
        lista_arg = []
        for indice, valor_tupla in enumerate(args):
            lista_arg.append(args[indice].upper())
        # Agregamos mas elementos a la lista
        lista_arg.append('nuevo arg 1')
        lista_arg.append('nuevo arg 2')
        # Agregamos informacion al diccionario
        kwargs['valor1'] = 'Nuevo valor 1'
        kwargs['valor2'] = 'Nuevo valor 2'
        # Propagamos los parametros a la funcion original
        # return funcion(*args, **kwargs)
        # Propagar los valores modificados
        return funcion(*lista_arg, **kwargs)
    return funcion_envolvente

@decorador_con_argumentos
def funcion_saludar(titulo, nombre, *args, **kwargs):
    # Imprimir titulo con el nombre
    print(f'{titulo}. {nombre}')
    # Imprimimos los argumentos variables
    print('args: ', args)
    print('kwargs: ', kwargs)

funcion_saludar('Ingeniera', 'Maria Quiroz')