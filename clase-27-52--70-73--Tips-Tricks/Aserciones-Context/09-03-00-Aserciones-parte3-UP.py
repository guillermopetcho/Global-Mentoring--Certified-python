# Tip. Las aserciones nos pueden ayudar a depurar nuestros programas de errores que no podemos recuperarnos
# no son sustituto del manejo de excepciones, sino un complemente para errores irrecuperables
# Las aserciones son una expresion booleana, si es verdadera el programa continua normalmente
# si es falso se lanza una excepcion, con un mensaje de manera opcional

# Ejemplo 1. Revisamos si la division es entre 0
def dividir(a, b):
    # Nos aseguramos que el valor de b no es cero para poder continuar
    assert b != 0, 'División entre cero'
    print(f'Resultado division: {a / b}')

# Ejemplo 2. Realizamos el calculo del promedio de una lista de calificaciones
def obtener_promedio(calificaciones):
    # Si la lista de calificaciones esta vacia no deberia continuar el programa
    assert len(calificaciones) != 0, 'Lista de calificaciones vacia'
    print(f'El promedio de calificaciones es: {sum(calificaciones)/len(calificaciones)}')

# Ejemplo 3. Realizamos un descuento al producto proporcionado
def aplicar_descuento(productos, descuento):
    precio_con_descuento = productos['precio'] * (1.0 - descuento)
    print(f'Nuevo precio del producto: {precio_con_descuento:0.2f}')
    assert 0<= precio_con_descuento <= productos['precio'], f'Descuento Invalido {precio_con_descuento:0.2f}'
    print('Descuento valido...')

if __name__ == '__main__':
    # Prueba Ejemplo 1. Division entre cero
    # dividir(10, 0)
    dividir(10,2)

    # Prueba Ejemplo 2. Calculo promedio de calificaciones
    calificaciones = [10,8,7,9]
    # calificaciones = []
    obtener_promedio(calificaciones)

    # Prueba Ejemplo 3. Aplicar descuento a un producto
    productos = {'nombre':'Camisa', 'precio':1500}
    # aplicar_descuento(productos, 1.2)
    aplicar_descuento(productos, .10)