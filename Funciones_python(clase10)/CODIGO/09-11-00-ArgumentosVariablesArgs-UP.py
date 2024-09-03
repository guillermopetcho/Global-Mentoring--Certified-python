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