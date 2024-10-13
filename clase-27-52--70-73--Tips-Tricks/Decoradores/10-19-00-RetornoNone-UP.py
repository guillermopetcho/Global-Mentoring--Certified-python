# De manera explicita se regresa el valor de None
def funcion1(valor):
    if valor:
        return valor
    else:
        return None

print(funcion1(0))

# De manera implicita se regresa el valor de None
def funcion2(valor):
    if valor:
        return valor

print(funcion2(0))

def funcion3(valor):
    print(valor)
    # return None

# funcion3(15)
print(funcion3(10))