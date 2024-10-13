def imprimir_vector(x, y, z):
    print(f'<{x}, {y}, {z}>')

imprimir_vector(10, 3, 12)

# Desempaquetar un iterable (tupla, lista, set, etc)
tupla_vector = (8,2,15)
imprimir_vector(*tupla_vector)

lista_vector = [4,2,7]
imprimir_vector(*lista_vector)

expresion_generador = (x * x for x in range(3))
imprimir_vector(*expresion_generador)

# Desempaquetar un diccionario
diccionario_vector = {'x':10, 'y': 15, 'z':3}
imprimir_vector(**diccionario_vector)

# Pasar las llaves
imprimir_vector(*diccionario_vector)
