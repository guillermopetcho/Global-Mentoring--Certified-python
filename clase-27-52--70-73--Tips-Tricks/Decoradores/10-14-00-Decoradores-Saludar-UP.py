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