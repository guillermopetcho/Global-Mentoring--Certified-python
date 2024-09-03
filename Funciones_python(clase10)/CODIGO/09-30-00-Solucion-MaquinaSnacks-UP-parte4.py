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