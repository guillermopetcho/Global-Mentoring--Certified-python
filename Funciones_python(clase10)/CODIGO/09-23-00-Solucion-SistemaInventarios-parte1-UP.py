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
