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

# Otro ejemplo de ordenamiento usando una expresion lambda
print(list(range(-3,4)))
# Si queremos ordenar por el valor absoluto (sin considerar signo)
for valor in range(-3,4):
    print(valor, valor*valor)

# Ahora lo aplicamos a una expresion lambda
lista_ordenada = sorted(range(-3,4), key=lambda valor: valor*valor)
print(lista_ordenada)

# Las funciones lambda tambien podemos aplicar el concepto de closure
def mostrar(titulo):
    return lambda mensaje: titulo + '. ' + mensaje

mostrar_ing = mostrar('Ingeniero')
mostrar_lic = mostrar('Licenciado')
print(mostrar_ing('Carlos Lara'))
print(mostrar_lic('Armando Casas'))

