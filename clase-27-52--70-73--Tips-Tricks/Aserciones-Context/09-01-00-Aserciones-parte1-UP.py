# Tip. Las aserciones nos puedes ayudar a depurar nuestros programas de errores
# que no nos podemos recuperar

# Ejemplo 1. Revisamos si la division es entre 0
def dividir(a, b):
    # Nos aseguramos que el valor de b no es cero para poder continuar
    assert b != 0, 'División entre cero'
    print(f'Resultado division: {a/b}')


if __name__ == '__main__':
    # Prueba Ejemplo 1. Division entre cero
    dividir(10,0)
