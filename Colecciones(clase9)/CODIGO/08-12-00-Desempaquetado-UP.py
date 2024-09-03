print('*** Desempaquetado de Tuplas ***')  # unpacking

producto = ('P001', 'Camisa', 20.00)

# Desempaquetado
id, descripcion, precio = producto

#Imprimir los valores
print(f'Tupla completa: {producto}')
# Valores independientes ya desempaquetados
print(f'Producto: id = {id}, descripcion = {descripcion}, precio = {precio}')