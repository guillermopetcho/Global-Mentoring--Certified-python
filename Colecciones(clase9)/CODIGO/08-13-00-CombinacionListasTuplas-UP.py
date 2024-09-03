print('*** Combinación de Listas y Tuplas ***')

# definir una lista que almacena tuplas de productos
productos = [
    ('P001', 'Camiseta', 20.00),
    ('P002', 'Jeans', 30.00),
    ('P003', 'Sudadera', 40.00)
]

# Imprimir la informacion de cada producto
# y ademas calculamos el precio total
precio_total = 0

print('Información de los productos: ')
for producto in productos:
    #print(producto)
    id, descripcion, precio = producto  # unpacking
    print(f'Producto: id = {id}, descripcion = {descripcion}, precio = ${precio}')
    precio_total += precio # producto[2]
print(f'Precio total de los productos: ${precio_total}')