# Las funciones lambda nos permiten declarar funciones anonimas
# en una sola linea de codigo
# Ejemplo normal
def sumar(a, b):
    return a + b

print(sumar(3, 5))

# Funcion lambda
sumar_lambda = lambda a, b: a + b
print(sumar_lambda(2, 4))

# Utilizando una sola linea de codigo
print((lambda a, b: a + b)(5, 6))

# Podemos usar una funcion lambda siempre que necesitemos una funcion concreta
# Ej. Ordenar una lista de tuplas, por su segundo valor proporcionando una llave (key)
lista_tuplas = [(1,'b'), (2, 'f'), (5, 'a'), (4, 'c')]
# lista_tuplas_ordenada = sorted(lista_tuplas, key=lambda tupla: tupla[0], reverse=True)
lista_tuplas_ordenada = sorted(lista_tuplas, key=lambda tupla: tupla[1], reverse=True)
print(lista_tuplas_ordenada)