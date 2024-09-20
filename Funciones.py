print("----------------------")
"""
Ejercicio: Calculadora de Impuestos
Crear una función para calcular el total de un pago incluyendo un impuesto aplicado.
# Formula: pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
"""

# Funcion que calcula el total de un pago incluyendo el impuesto
def calcular_total_pago(pago_sin_impuesto, impuesto):
    pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
    return pago_total

# Ejecutamos la funcion
pago_sin_impuesto = float(input('Proporcione el pago sin impuestos: '))
impuesto = float(input('Proporcione el monto del impuesto:'))
pago_con_impuesto = calcular_total_pago(pago_sin_impuesto, impuesto)
print(f'Pago con impuesto: {pago_con_impuesto}')


print("----------------------")

"""
Ejercicio: Convertidor de Temperatura
Realizar dos funciones para convertir de grados celsius a fahrenheit y viceversa.
"""

# Funcion que convierte de celsius a fahrenheit
def celsius_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

# Funcion que convierte de fahrenheit a celsius
def fahrenheit_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

# Realizamos algunas pruebas de conversion
celsius = float(input('Proporcione su valor en celsius: '))
resultado = celsius_fahrenheit(celsius)
# Imprimimos el resultado
print(f'{celsius} C a F: {resultado:.2f}')

# Realizamos la prueba de grados fahrenheit a celsius
fahrenheit = float(input('Proporcione su valor en fahrenheit: '))
resultado = fahrenheit_celsius(fahrenheit)
# Imprimimos el resultado
print(f'{fahrenheit} F a C: {resultado:0.2f}')

print("----------------------")

print('*** Funciones en Python ***')

# Definir una funcion para mandar a saludar
def saludar():  # Firma del metodo
    # Cuerpo de la funcion
    print('Saludos desde una función...')

# Programa principal, llamamos a la funcion
saludar()
saludar()
saludar()


print("----------------------")


print('*** Funciones en Python ***')

# Definir una funcion para mandar a saludar
def saludar(mensaje):
   print(f'Mensaje recibido: {mensaje}')

# Programa principal, llamamos a la funcion
saludar('Hola a todos')


print("----------------------")
print('*** Función sumar ***')

# Definimos la funcion
def sumar(a, b):
    resultado_suma = a + b
    return resultado_suma

# Llamar a la funcion
resultado_funcion = sumar(8, 5)
print(f'Resultado función sumar: {resultado_funcion}')

resultado_funcion = sumar(9, 15)
print(f'Resultado función sumar: {resultado_funcion}')

print("----------------------")

print('*** Funcion con argumentos por nombre ***')

def imprimir_persona(nombre, apellido='', edad=0):
    print(f'Persona: nombre = {nombre}, apellido = {apellido}, edad = {edad}')

# Primero llamamos la funcion pasando los argumentos de manera posicional
imprimir_persona('Ricardo', 'Quintana', 32)
# Llamar la funcion usando argumentos por nombre
imprimir_persona(nombre='Carlos', apellido='Rojas', edad=28)
# Llamar la funcion usando argumentos por nombre, pero intercambiando el orden
imprimir_persona(edad=28, apellido='Rojas', nombre='Carlos')
# Argumentos con valor por default
imprimir_persona(nombre='Carlos')
imprimir_persona(nombre='Carlos', apellido='Rojas')
imprimir_persona(apellido='Rojas', nombre='Carlos')


print("----------------------")
print('*** Regresar una tupla de valores desde una función ***')

# Definicion de la funcion
def persona_mayusculas(nombre, apellido, edad):
    print(f'Esta función regresa varios valores (tupla)')
    return nombre.upper(), apellido.upper(), edad

# Programa principal
nombre, apellido, edad = persona_mayusculas('Sandra', 'Jimenez', 42)
print(f'Resultado Persona: nombre = {nombre}, apellido = {apellido}, edad = {42}')
print("----------------------")
print('*** Obtener coordenadas x,y,z ***')

def obtener_coordenadas():
    x, y, z = 10, 20, 30
    return x, y, z

# Llamar la funcion
resultado = obtener_coordenadas()
print(resultado)

# Unpacking de la tupla
x1, y1, z1 = resultado
print(f'Coordenada x = {x1}, Coordenada y = {y1}, Coordenada z = {z1}')
print("----------------------")
print('*** Alcance de Variables ***')

# Variable global
contador_global = 0

def incrementar_contador():
    # Declaramos una variable local
    contador_local = 0
    # usar la variable global
    global contador_global
    # incrementamos la variable global
    contador_global += 1
    # incrementar la variable local
    contador_local += 1
    # Imprimimos ambos contadores
    print(f'Contador local: {contador_local}')
    print(f'Contador global: {contador_global}\n')

# Llamamos varias vece la funcion
incrementar_contador()
incrementar_contador()
incrementar_contador()

# Terminando el programa
print(f'Valor variable global: {contador_global}')


print("----------------------")
print('*** Argumentos Variables ***')

def superheroe_superpoderes(superheroe, nombre, *args):
    print(f'Superheroe: {superheroe} - {nombre} - {args}')
    # Iteramos los superpoderes
    for superpoder in args:
        print(f'\tSuperpoder: {superpoder}')

# Llamar la funcion
superheroe_superpoderes('Spiderman', 'Peter Parker', 'Instinto Arácnido', 'Teleraña')
superheroe_superpoderes('Ironam', 'Tony Stark', 'Armadura','Playboy','Millonario')

# Es opcional enviar argumentos variables
superheroe_superpoderes('Mi vecino', 'Juan Perez')
print("----------------------")
# *args - arguments - tupla
# **kwargs - keyword arguments (key,value) como un dict
print('*** Argumentos variables en forma de dict ***')

def superheroe_superpoderes(nombre, *args, **kwargs):
    print(f'Superheroe: {nombre} - {args} - Mas info: {kwargs}')

# Llamarmos la funcion
superheroe_superpoderes('Spiderman', 'Instinto Arácnido', edad=17, empresa='Marvel')
superheroe_superpoderes('Ironman', 'Armandura','Playboy', edad=45)

# Es opcional enviar argumentos variables
superheroe_superpoderes('Mi vecino', personalidad='Buena onda!')

print("----------------------")
print('*** Suma con Argumentos Variables ***')

# Funcion sumar que acepta argumentos variables
def sumar(*args):
    total = 0
    for numero in args:
        total += numero
    return total

# Llamamos a la funcion sumar
resultado = sumar(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(f'Resultado de la suma: {resultado}')


print("----------------------")
print('*** Imprimir detalles de una persona usando kwargs ***')

# Funcion que acepta argumentos variables en forma de llave-valor dict
def imprimir_detalle_persona(**kwargs):
    print('\nValores recibidos: ')
    for llave, valor in kwargs.items():
        print(f'{llave}:{valor}')

# Llamamos a la funcion
imprimir_detalle_persona(nombre='Karla', edad=30, ciudad='México')
imprimir_detalle_persona(nombre='Carlos', edad=28, ciudad='Guadalajara', puesto='Gerente')
print("----------------------")
print('*** Funcion par ***')

# Funcion para saber si un numero es par o no
def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False


# Llamamos a la funcion
if __name__ == '__main__':
    numero = int(input('Proporciona un valor numérico: '))
    print(f'Número par? {es_par(numero)}')


print("----------------------")
print('*** Imprimir del 1 al 5 de forma recursiva ***')

# definir la funcion recursiva
def funcion_recursiva(numero):
    # Caso Base
    if numero == 1:
        print(numero, end=' ')  # 1
    else: # Caso recursivo
        funcion_recursiva(numero - 1)
        print(numero, end=' ')

# Programa principal
funcion_recursiva(5)
print("----------------------")
print('*** Factorial del Número 5 ***')

# Definimos la funcion factorial recursiva
def factorial_recursiva(numero):
    # Caso base, factorial 0! = 1, 1! = 1
    if numero == 0 or numero == 1:
        print(f'Resultado factorial parcial {numero} es: 1')
        return 1
    else: # Caso recursivo
        factorial_parcial = numero * factorial_recursiva(numero - 1)
        print(f'Resultado factorial parcial {numero} es: {factorial_parcial}')
        return factorial_parcial

numero = 5
resultado = factorial_recursiva(numero)
print(f'El factorial de {numero} es: {resultado}')
print("----------------------")
print('*** Potencia número usando funciones recursivas ***')

def potencia(base, exponente):
    # Caso base
    if exponente == 0:
        return 1
    else:  # Caso recursivo
        return base * potencia(base, exponente - 1)

print(f'2 elevado a la 3: {potencia(2, 3)}')
print(f'5 elevado a la 0: {potencia(5, 0)}')
print(f'4 elevado a la 5: {potencia(4, 5)}')
print("----------------------")
print('*** Sistema de Inventarios (con funciones) ***')

# Inventario del almacen
inventario = [
    {'id': 1, 'nombre': 'Camisa', 'precio': 25.99, 'cantidad': 50},
    {'id': 2, 'nombre': 'Pantalones', 'precio': 39.99, 'cantidad': 30},
    {'id': 3, 'nombre': 'Zapatos', 'precio': 49.99, 'cantidad': 20}
]

# Funcion para mostrar el inventario
def mostrar_inventario():
    print('--- Inventario del Almacén ---')
    for producto in inventario:
        print(f'Id: {producto.get('id')}, Nombre: {producto.get('nombre')},'
              f'Precio: ${producto.get('precio')}, Cantidad: {producto.get('cantidad')}')

def agregar_producto():
    pass

def buscar_producto_por_id():
    pass


# Programa principal
if __name__ == '__main__':
    while True:
        print(f'''\n--- Menú ---
        1. Mostrar inventario
        2. Agregar nuevo producto
        3. Buscar producto por id
        4. Salir''')
        opcion = int(input('Proporciona una opción (1-4): '))
        # Revisamos las opciones del menu
        if opcion == 1:  # Mostrar el inventario
            mostrar_inventario()
        elif opcion == 2:  # Agregar nuevo producto
            agregar_producto()
        elif opcion == 3:  # Buscar producto por id
            buscar_producto_por_id()
        elif opcion == 4:  # Salir
            print('Hasta luego!')
            break
        else:
            print('Opción inválida, proporciona una opción válida')

print("----------------------")
print('*** Sistema de Inventarios (con funciones) ***')

# Inventario del almacen
inventario = [
    {'id': 1, 'nombre': 'Camisa', 'precio': 25.99, 'cantidad': 50},
    {'id': 2, 'nombre': 'Pantalones', 'precio': 39.99, 'cantidad': 30},
    {'id': 3, 'nombre': 'Zapatos', 'precio': 49.99, 'cantidad': 20}
]

# Funcion para mostrar el inventario
def mostrar_inventario():
    print('--- Inventario del Almacén ---')
    for producto in inventario:
        print(f'Id: {producto.get('id')}, Nombre: {producto.get('nombre')},'
              f'Precio: ${producto.get('precio')}, Cantidad: {producto.get('cantidad')}')

def agregar_producto():
    # pass
    print('--- Agregar Nuevo Producto ---')
    id = int(input('Id: '))
    nombre = input('Nombre: ')
    precio = float(input('Precio: '))
    cantidad = int(input('Cantidad: '))
    nuevo_producto = {'id': id, 'nombre':nombre,
                      'precio': precio, 'cantidad': cantidad}
    inventario.append(nuevo_producto)
    print('Producto agregado al inventario')

def buscar_producto_por_id():
    pass


# Programa principal
if __name__ == '__main__':
    while True:
        print(f'''\n--- Menú ---
        1. Mostrar inventario
        2. Agregar nuevo producto
        3. Buscar producto por id
        4. Salir''')
        opcion = int(input('Proporciona una opción (1-4): '))
        # Revisamos las opciones del menu
        if opcion == 1:  # Mostrar el inventario
            mostrar_inventario()
        elif opcion == 2:  # Agregar nuevo producto
            agregar_producto()
        elif opcion == 3:  # Buscar producto por id
            buscar_producto_por_id()
        elif opcion == 4:  # Salir
            print('Hasta luego!')
            break
        else:
            print('Opción inválida, proporciona una opción válida')

print("----------------------")
print('*** Sistema de Inventarios (con funciones) ***')

# Inventario del almacen
inventario = [
    {'id': 1, 'nombre': 'Camisa', 'precio': 25.99, 'cantidad': 50},
    {'id': 2, 'nombre': 'Pantalones', 'precio': 39.99, 'cantidad': 30},
    {'id': 3, 'nombre': 'Zapatos', 'precio': 49.99, 'cantidad': 20}
]

# Funcion para mostrar el inventario
def mostrar_inventario():
    print('--- Inventario del Almacén ---')
    for producto in inventario:
        print(f'Id: {producto.get('id')}, Nombre: {producto.get('nombre')},'
              f'Precio: ${producto.get('precio')}, Cantidad: {producto.get('cantidad')}')

def agregar_producto():
    # pass
    print('--- Agregar Nuevo Producto ---')
    id = int(input('Id: '))
    nombre = input('Nombre: ')
    precio = float(input('Precio: '))
    cantidad = int(input('Cantidad: '))
    nuevo_producto = {'id': id, 'nombre':nombre,
                      'precio': precio, 'cantidad': cantidad}
    inventario.append(nuevo_producto)
    print('Producto agregado al inventario')

def buscar_producto_por_id():
    print('--- Buscar Producto por Id ---')
    id_buscar = int(input('Ingresa el id a buscar: '))
    for producto in inventario:
        if producto.get('id') == id_buscar:
            print('\nInformación del producto encontrado: ')
            print(f'Id: {producto.get('id')}, Nombre: {producto.get('nombre')},'
                  f'Precio: ${producto.get('precio')}, '
                  f'Cantidad: {producto.get('cantidad')}')
            return
    print('\nProducto NO encontrado')


# Programa principal
if __name__ == '__main__':
    while True:
        print(f'''\n--- Menú ---
        1. Mostrar inventario
        2. Agregar nuevo producto
        3. Buscar producto por id
        4. Salir''')
        opcion = int(input('Proporciona una opción (1-4): '))
        # Revisamos las opciones del menu
        if opcion == 1:  # Mostrar el inventario
            mostrar_inventario()
        elif opcion == 2:  # Agregar nuevo producto
            agregar_producto()
        elif opcion == 3:  # Buscar producto por id
            buscar_producto_por_id()
        elif opcion == 4:  # Salir
            print('Hasta luego!')
            break
        else:
            print('Opción inválida, proporciona una opción válida')

print("----------------------")
print('*** Sistema Máquina de Snacks ***')

# Definimos la lista de snacks inicial
snacks = [
    {'id': 1, 'nombre': 'Papas', 'precio': 30},
    {'id': 2, 'nombre': 'Refresco', 'precio': 50},
    {'id': 3, 'nombre': 'Sandwich', 'precio': 120}
]

# Lista de productos (vacia). Son los snacks ya comprados
productos = []

def mostrar_snacks():
    pass

def comprar_snack():
    pass

def mostrar_ticket():
    pass


# Programa principal
if __name__ == '__main__':
    # Creamos el menu
    while True:
        print(f'''Menú:
        1. Mostrar Snacks
        2. Comprar Snack
        3. Mostrar ticket
        4. Salir''')
        opcion = int(input('Escoge una opción: '))
        if opcion == 1:
            mostrar_snacks()
        elif opcion == 2:
            comprar_snack()
        elif opcion == 3:
            mostrar_ticket()
        elif opcion == 4:
            print('Regresa pronto!')
            break
        else:
            print('Opción inválida, proporciona otra opción!')
print("----------------------")
print('*** Sistema Máquina de Snacks ***')

# Definimos la lista de snacks inicial
snacks = [
    {'id': 1, 'nombre': 'Papas', 'precio': 30},
    {'id': 2, 'nombre': 'Refresco', 'precio': 50},
    {'id': 3, 'nombre': 'Sandwich', 'precio': 120}
]

# Lista de productos (vacia). Son los snacks ya comprados
productos = []

def mostrar_snacks():
    print('--- Snacks Disponibles ---')
    for snack in snacks:
        print(f'\tId: {snack.get('id')} -> {snack.get('nombre')} '
              f'- ${snack.get('precio')}')

def comprar_snack():
    pass

def mostrar_ticket():
    pass


# Programa principal
if __name__ == '__main__':
    # Creamos el menu
    while True:
        print(f'''Menú:
        1. Mostrar Snacks
        2. Comprar Snack
        3. Mostrar ticket
        4. Salir''')
        opcion = int(input('Escoge una opción: '))
        if opcion == 1:
            mostrar_snacks()
        elif opcion == 2:
            comprar_snack()
        elif opcion == 3:
            mostrar_ticket()
        elif opcion == 4:
            print('Regresa pronto!')
            break
        else:
            print('Opción inválida, proporciona otra opción!')
print("----------------------")
print('*** Sistema Máquina de Snacks ***')

# Definimos la lista de snacks inicial
snacks = [
    {'id': 1, 'nombre': 'Papas', 'precio': 30},
    {'id': 2, 'nombre': 'Refresco', 'precio': 50},
    {'id': 3, 'nombre': 'Sandwich', 'precio': 120}
]

# Lista de productos (vacia). Son los snacks ya comprados
productos = []

def mostrar_snacks():
    print('--- Snacks Disponibles ---')
    for snack in snacks:
        print(f'\tId: {snack.get('id')} -> {snack.get('nombre')} '
              f'- ${snack.get('precio')}')

def buscar_snack_por_id(id_buscar):
    for snack in snacks:
        if snack.get('id') == id_buscar:
            return snack
    # Si llegamos al final y no se encontro el snack regresa None
    return None

def comprar_snack():
    id_snack = int(input('Qué snack quieres comprar (id): '))
    snack_encontrado = buscar_snack_por_id(id_snack)
    if snack_encontrado is not None:
        productos.append(snack_encontrado)
        print(f'Snack agregado: {snack_encontrado}')
    else:
        print(f'Snack NO encontrado con el id: {id_snack}')

def mostrar_ticket():
    pass


# Programa principal
if __name__ == '__main__':
    # Creamos el menu
    while True:
        print(f'''Menú:
        1. Mostrar Snacks
        2. Comprar Snack
        3. Mostrar ticket
        4. Salir''')
        opcion = int(input('Escoge una opción: '))
        if opcion == 1:
            mostrar_snacks()
        elif opcion == 2:
            comprar_snack()
        elif opcion == 3:
            mostrar_ticket()
        elif opcion == 4:
            print('Regresa pronto!')
            break
        else:
            print('Opción inválida, proporciona otra opción!')
print("----------------------")
print('*** Sistema Máquina de Snacks ***')

# Definimos la lista de snacks inicial
snacks = [
    {'id': 1, 'nombre': 'Papas', 'precio': 30},
    {'id': 2, 'nombre': 'Refresco', 'precio': 50},
    {'id': 3, 'nombre': 'Sandwich', 'precio': 120}
]

# Lista de productos (vacia). Son los snacks ya comprados
productos = []

def mostrar_snacks():
    print('--- Snacks Disponibles ---')
    for snack in snacks:
        print(f'\tId: {snack.get('id')} -> {snack.get('nombre')} '
              f'- ${snack.get('precio')}')

def buscar_snack_por_id(id_buscar):
    for snack in snacks:
        if snack.get('id') == id_buscar:
            return snack
    # Si llegamos al final y no se encontro el snack regresa None
    return None

def comprar_snack():
    id_snack = int(input('Qué snack quieres comprar (id): '))
    snack_encontrado = buscar_snack_por_id(id_snack)
    if snack_encontrado is not None:
        productos.append(snack_encontrado)
        print(f'Snack agregado: {snack_encontrado}')
    else:
        print(f'Snack NO encontrado con el id: {id_snack}')

def mostrar_ticket():
    ticket = f'\t--- Ticket de Venta ---'
    total = 0
    for producto in productos:
        ticket += f'\n\t- {producto.get('nombre')} - ${producto.get('precio')}'
        total += producto.get('precio')
    ticket += f'\n\tTOTAL -> ${total}'
    print(ticket)


# Programa principal
if __name__ == '__main__':
    # Creamos el menu
    while True:
        print(f'''Menú:
        1. Mostrar Snacks
        2. Comprar Snack
        3. Mostrar ticket
        4. Salir''')
        opcion = int(input('Escoge una opción: '))
        if opcion == 1:
            mostrar_snacks()
        elif opcion == 2:
            comprar_snack()
        elif opcion == 3:
            mostrar_ticket()
        elif opcion == 4:
            print('Regresa pronto!')
            break
        else:
            print('Opción inválida, proporciona otra opción!')
print("----------------------")
print(f'*** Calculadora con Funciones ***')

def mostrar_menu():
    print(f'''Operaciones que puedes realizar:
    1. Suma
    2. Resta
    3. Multiplicación
    4. División
    5. Salir''')
    return int(input('Escoge una opción: '))

def ejecutar_operacion(opcion, salir):
    pass


# Programa principal
if __name__ == '__main__':
    salir = False
    while not salir:
        opcion = mostrar_menu()
        salir = ejecutar_operacion(opcion, salir)
print("----------------------")
print(f'*** Calculadora con Funciones ***')

def mostrar_menu():
    print(f'''Operaciones que puedes realizar:
    1. Suma
    2. Resta
    3. Multiplicación
    4. División
    5. Salir''')
    return int(input('Escoge una opción: '))

def pedir_valores():
    operando1 = float(input('Dame el valor 1: '))
    operando2 = float(input('Dame el valor 2: '))
    return operando1, operando2

def ejecutar_operacion(opcion, salir):
    # Solicitar los valores de los operandos
    if 1 <= opcion <= 4:
        operando1, operando2 = pedir_valores()
    resultado = 0
    if opcion == 1:  # Sumar
        resultado = operando1 + operando2
        print(f'El resultado de la suma es: {resultado}\n')
    elif opcion == 2:  # Restar
        resultado = operando1 - operando2
        print(f'El resultado de la resta es: {resultado}\n')
    elif opcion == 3:  # Multiplicación
        resultado = operando1 * operando2
        print(f'El resultado de la multiplicación es: {resultado}\n')
    elif opcion == 4:  # División
        resultado = operando1 / operando2
        print(f'El resultado de la división es: {resultado}\n')
    elif opcion == 5:  # Salir
        print('Saliendo del programa de calculadora, hasta pronto!')
        salir = True
    else:
        print('Opción inválida, selecciona otra opción...\n')
    return salir


# Programa principal
if __name__ == '__main__':
    salir = False
    while not salir:
        opcion = mostrar_menu()
        salir = ejecutar_operacion(opcion, salir)
print("----------------------")
print("----------------------")
print("----------------------")
print("----------------------")
print("----------------------")
print("----------------------")
print("----------------------")
print("----------------------")
print("----------------------")
print("----------------------")
print("----------------------")
print("----------------------")
print("----------------------")
print("----------------------")
print("----------------------")
