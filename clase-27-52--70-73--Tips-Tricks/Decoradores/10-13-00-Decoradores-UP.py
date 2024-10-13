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

print(saludar_funcion_a_decorar())