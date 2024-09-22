"""#############################################################################################"""
"""#############################################################################################"""
"""#############################################################################################"""

"""
░░▄███▄███▄
░░█████████
░░▒▀█████▀░
░░▒░░▀█▀
░░▒░░█░
░░▒░█
░░░█
░░█░░░░███████
░██░░░██▓▓███▓██▒
██░░░█▓▓▓▓▓▓▓█▓████
██░░██▓▓▓(◐)▓█▓█▓█
███▓▓▓█▓▓▓▓▓█▓█▓▓▓▓█
▀██▓▓█░██▓▓▓▓██▓▓▓▓▓█
░▀██▀░░█▓▓▓▓▓▓▓▓▓▓▓▓▓█
░░░░▒░░░█▓▓▓▓▓█▓▓▓▓▓▓█
░░░░▒░░░█▓▓▓▓█▓█▓▓▓▓▓█
░▒░░▒░░░█▓▓▓█▓▓▓█▓▓▓▓█
░▒░░▒░░░█▓▓▓█░░░█▓▓▓█
░▒░░▒░░██▓██░░░██▓▓██
████████████████████████
█▄─▄███─▄▄─█▄─█─▄█▄─▄▄─█
██─██▀█─██─██─█─███─▄█▀█
▀▄▄▄▄▄▀▄▄▄▄▀▀▄▄▄▀▀▄▄▄▄▄▀

"""
"""#############################################################################################"""
"""
░██████╗░██╗░░░██╗██╗██╗░░░░░██╗░░░░░███████╗
██╔════╝░██║░░░██║██║██║░░░░░██║░░░░░██╔════╝
██║░░██╗░██║░░░██║██║██║░░░░░██║░░░░░█████╗░░
██║░░╚██╗██║░░░██║██║██║░░░░░██║░░░░░██╔══╝░░
╚██████╔╝╚██████╔╝██║███████╗███████╗███████╗
░╚═════╝░░╚═════╝░╚═╝╚══════╝╚══════╝╚══════╝                                                   """
"""#############################################################################################"""


"""-----------------------Cadenas en Python--------------------------------"""
print("---------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------")
print("-----------------------Cadenas dentro de Python ---------------------------------")
print("---------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------")
cadena1 = 'Hola Mundo'
cadena2 = "Python es genial"
cadena3 = '''Este es un ejemplo
            de multiples lineas
            en una cadena'''


print("Imprimimos las cadenas que creamos")
print("La funcion print imprime una cadena")
print(cadena1)
print(cadena2)
print("Con las triples comillas se puede imprimir multiples lineas")
print(cadena3)



print("\n")#salto de linea
print("---------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------")
print("-----------------------Manejo de indice en una cadena----------------------------")
print("---------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------")


print(cadena1)
# Recuperar el primer caracter
primer_caracter = cadena1[0]  # Recupera 'H'
print(primer_caracter)
ultimo_caracter = cadena1[7]  # Recupera 'o'
print(ultimo_caracter)


print("\n")#salto de linea
print("---------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------")
print("-------------------Se puede multiplicar la cadena por un numero -----------------")
print("---------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------")

print('*** Multiplicación de Cadenas 4 veces***')

veces = 4
resultado = cadena1 * veces
print(resultado)



print("\n")#salto de linea
print("---------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------")
print("------------------- Como imprimir caracteres especiales -------------------------")
print("---------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------")

# Caracteres Especiales
print('Hola \nMundo')  # \n salto de linea
print('\t\tPython \t\tes genial') # \t agrega un tabulador
print('Juan\' "Perez')
print("Karla \" Gomez")
print('Caracter \\ diagonal invertida')


print("\n")#salto de linea
print("---------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------")
print("------------------------- Concatenacion de Cadenas ------------------------------")
print("---------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------")

# Concatenacion de Cadenas
concatenacion = cadena1 + ' ' + cadena2
print(concatenacion)

# Utilizando el metodo join
concatenacion = ''.join([cadena1, ' ', cadena2])
print(concatenacion)


print("\n")#salto de linea
print("---------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------")
print("---------------------------- Formateo de cadenas --------------------------------")
print("---------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------")

nombre = 'Juan'
edad = 30

# f-string
"""
f-string o formatted string literal en Python. 
Esta es una forma conveniente, legible de incorporar variables y expresiones dentro de cadenas de texto.
"""
mensaje = f'Hola, me llamo {nombre} y tengo {edad} años.'
print(mensaje)

# metodo format
mensaje = 'Hola, me llamo {} y tengo {} años.'.format(nombre, edad)
print(mensaje)


print("\n")#salto de linea
print("---------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------")
print("----------------------------- Largo de una cadena--------------------------------")
print("---------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------")


largo_cadena = len(cadena1)
print(f'Cadena original: {cadena1}')
print(f'Largo de la cadena: {largo_cadena}')


print("\n")#salto de linea
print("---------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------")
print("-------------------------- Manejo de subcadenas --------------------------------")
print("---------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------")

#hola mundo
#0123456789

# Subcadenas
# Obtenemos la subcadena de hola [inicio:fin (sin incluirlo)]
subcadena_hola = cadena1[0:3]
print(f'Subcadena de hola: {subcadena_hola}')

# Obtene la subcadena de mundo
subcadena_mundo = cadena1[5:9]
print(f'Subcadena de mundo: {subcadena_mundo}')


print("\n")#salto de linea
print("---------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------")
print("------------------- Buscar subcadenas en una cadena ---------------------------")
print("---------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------")


# Buscar subcadenas
indice = cadena1.find('mundo')
print(f'Indice de la subcadena mundo: {indice}')

# Obtener el indice de la subcadena de Hola
indice = cadena1.find('Hola')
print(f'Indice  la subcadena de Hola: {indice}')

print("\n")#salto de linea

print("---------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------")
print("--------------------------- Reemplazar subcadenas -------------------------------")
print("---------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------")

cadena = 'Hola, mundo!'
print(f'Cadena original: {cadena}')
nueva_cadena = cadena.replace('mundo', 'a todos')
print(f'Nueva cadena reemplazada: {nueva_cadena}' )

# Sustituir hola por adios
nueva_cadena = cadena.replace('Hola', 'Adios')
print(f'Nueva cadena reemplazada: {nueva_cadena}')

print("\n")#salto de linea

print("---------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------")
print("---------------------------- Separar cacenas (split) ----------------------------")
print("---------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------")

datos = 'Hola Mundo'
lista = datos.split() # por default separa cada elemento por espacios en blanco
print(lista)

datos = 'Juan,30,México'
lista = datos.split(',')
print(lista)


print("---------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------")
print("------------------- Son las posibilidades dentro de Python ----------------------")
print("---------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------")

print("---------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------")
print("------------------- Los codigos de Python son del curso -------------------------")
print("---------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------")

print("\n")#salto de linea
print("---------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------")
print("------------------------- EJERCICIO DE GENERAR EMAIL ----------------------------")
print("---------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------")
print("\n")#salto de linea
print("\n")#salto de linea

# Generador de  emails
print('-------------------TENEMOS EL NOMBRE DEL USUARIO----------------------------------')

print("\n")#salto de linea

# Nombre completo del usuario
nombre_completo = 'Eduaro, Bruno Meza '
print(f'Nombre usuario: {nombre_completo}')
# Procesar o normalizar el nombre del usuario
# Limpiamos los espacios en blanco al inicio y al final
print('--------QUITAMOS LOS ESPACIOS EN BLANCO AL INICIO Y AL FINAL---------------------')
print('--------QUITAMOS TODOS LOS SIGNOS Y PONEMOS PUNTOS-------------------------------')
print("\n")#salto de linea

nombre_normalizado = nombre_completo.strip()
# Reemplazar los espacios en blanco por puntos
nombre_normalizado = nombre_normalizado.replace(' ', '.')
nombre_normalizado = nombre_normalizado.replace(',', '.')
# Convertimos a minusculas
nombre_normalizado = nombre_normalizado.lower()
print(f'Nombre usuario normalizado: {nombre_normalizado}')

print('------- EL NOMBRE DE LA EMPRESA ES EL SIGUIENTE----------------------------------')


# Datos de la empresa
nombre_empresa = ' Patito Juan '
print(f'\nNombre empresa: {nombre_empresa}')


print('----------------QUITAMOS TODOS LOS SIGNOS Y PONEMOS PUNTOS-----------------------')
print("\n")#salto de linea
print("\n")#salto de linea
extension_dominio = '.com.ar'
print(f'Extensión del dominio: {extension_dominio}')
# Quitamos los espacios en blanco y convertimos a mayusculas
nombre_empresa_normalizado = nombre_empresa.replace(' ', '').lower()
dominio_email_normalizado = f'@{nombre_empresa_normalizado}{extension_dominio}'
print(f'Dominio del email normalizado: {dominio_email_normalizado}')

print('---IMPRIMOS LAS DOS CADENAS PEGADAS PARA QUE PAREZCA UN EMAL JAJA-------')
# Creamos el email final
email = f'{nombre_normalizado}{dominio_email_normalizado}'
print('---SE CREA EL EMAIL CORRECTO-----------')
print(f'\nEmail final generado: {email}')