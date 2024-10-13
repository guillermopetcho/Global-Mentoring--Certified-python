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

