print("----------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------")
print("----------------------Conversion de tipos de datos--------------------------------")
print("----------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------")

# Convertir de cadena a numero
numero_cadena = '10'
numero_entero = int(numero_cadena)
print(f'Valor numérico en cadena: {numero_cadena}')
print(f'Cadena a entero: {numero_entero}')

# Convertir de cadena a flotante
numero_cadena = '3.14'
numero_flotante = float(numero_cadena)
print(f'Cadena a flotante: {numero_flotante}')

# Convertir de numero a cadena
numero_entero = 25
numero_cadena = str(numero_entero)
print(f'Numero a cadena: {numero_cadena}')


print("----------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------")
print("-----------------------------Convertir a booleano---------------------------------")
print("----------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------")


# Convertir a booleano
# Tipo bool es Falso en los siguientes casos:
# REGRESA TRUE != 0, REGRESA TRUE != cadena vacia, REGRESA TRUE != None
# REGRESA FALSE == 0, REGRESA FALSE == cadena vacia, REGRESA FALSE == None

# Convertir a booleano
numero_entero = 0
booleano = bool(numero_entero)
print(f'Valor booleano de 0: {booleano}')  # False, incluye 0, 0.0

numero_entero = 5
booleano = bool(numero_entero)
print(f'Valor booleano de 5: {booleano}')  # True

cadena = '' # El largo de la cadena es 0,
booleano = bool(cadena)
print(f'Valor booleano de cadena vacía: {booleano}')  # Falso, incluye colecciones vacias

cadena = 'Cadena con valor'
booleano = bool(cadena)
print(f'Valor booleano de cadena NO vacía: {booleano}') # True

variable = None
booleano = bool(variable)
print(f'Valor booleano de None: {booleano}') # False


print("----------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------")
print("-----------------------------Concatenacion y suma de int--------------------------")
print("----------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------")


# Ejemplo tipos datos

# Ejemplo de contactenacion o suma de valores
numero1_cadena = '10'
print(f'Número 1 en cadena: {numero1_cadena}')
numero2_cadena = '20'
print(f'Número 2 en cadena: {numero2_cadena}')
resultado = numero1_cadena + numero2_cadena
print(f'Concatenacion: {resultado}')

# Convertimos a tipos enteros
numero1_entero = int(numero1_cadena)
numero2_entero = int(numero2_cadena)
resultado = numero1_entero + numero2_entero
print(f'Suma: {resultado}')

print("----------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------")
print("--------------------Entrada de datos por consola----------------------------------")
print("----------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------")


# Entrada de datos por consola
nombre = input('Introduce tu nombre: ')
print(f'Recibiendo el valor de nombre: {nombre}')

# Pedir la edad al usuario (entra como cadena, y lo convertimos a numero)
edad = int(input('Introduce tu edad: '))
print(f'Tu edad es: {edad}, y en un año tendras {edad + 1}')

print("----------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------")
print("-------------------EJERCICIO DE EMPLEADOS COMPLETO--------------------------------")
print("----------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------")

print('*** Sistema de Empleados ***')
nombre_empleado = input('Nombre del empleado: ')
edad_empleado = int(input('Edad del empleado: '))
salario_empleado = float(input('Salario del empleado: '))
es_jefe_departamento = input('Es jefe departamento (Si/No)? ')

# Vamos a convertir a un tipo bool la variable es_jefe_departamento
es_jefe_departamento = es_jefe_departamento.lower() == 'si'

# Imprimir los valores del Empleado
print('\nDatos del Empleado')
print(f'Nombre: {nombre_empleado}')
print(f'Edad: {edad_empleado}')
print(f'Salario: {salario_empleado:.2f}')
print(f'Es Jefe de Departamento? {es_jefe_departamento}')

print("----------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------")
print("---------------------EJERCICIO DE RECETAS DE COCINA COMPLETO----------------------")
print("----------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------")

print(f'*** Recetas de Cocina ***')
nombre_receta = input('Ingresa el nombre: ')
ingredientes = input('Ingresa los ingredientes: ')
tiempo_preparacion = int(input('Ingresa el tiempo de preparación (min): '))
dificultad_preparacion = input('Ingresa la dificultad: ')
print('-------------------------------')
print(f'Nombre receta: {nombre_receta}')
print(f'Ingredientes: {ingredientes}')
print(f'Tiempo de preparación: {tiempo_preparacion}')
print(f'Dificultad: {dificultad_preparacion}')

print("----------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------")
print("----------------Valores aleatorios con la funcion randint-------------------------")
print("----------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------")

#LIBRERIA RANDOM (VALORES ALEATORIOS)
from random import randint

# Generar un numero aleatorio entre 1 y 10
numero = randint(1, 10)
print(f'Numero aleatorio entre 1 y 10: {numero}')

# Simular un dado de seis caras
dado = randint(1, 6)
print(f'Resultado de lanzar el dado: {dado}')

print("----------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------")
print("-------------------------Sistema Generador de ID Único----------------------------")
print("----------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------")

#LIBRERIA RANDOM (VALORES ALEATORIOS) from random import randint

nombre = input('Cual es tu nombre?:')
apellido = input('Cual es tu apellido? ')
anio_nacimiento = input('Cual es tu año de nacimiento (YYYY)?:') # Y - year

# Normalizar los valores
nombre_2 = nombre.strip().upper()[0:2]
apellido_2 = apellido.strip().upper()[0:2]
anio_nacimiento_2 = anio_nacimiento.strip()[2:] # Tambien puede ser [2:4]

# Generar el valor aleatorio
aleatorio = randint(1000, 9999)

# Generamos el valor de id unico
id_unico = f'{nombre_2}{apellido_2}{anio_nacimiento_2}{aleatorio}'

print(f'''\nHola {nombre},
    Tu nuevo número de identificación (ID) generado por el sistema es:
    {id_unico}
    Felicidades!''')

print("----------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------")
print("----------------------Sistema Generador de Emails---------------------------------")
print("----------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------")


nombre = input('Cual es tu nombre? ')
apellidos = input('Cuales son tus apellidos? ')
empresa = input('Nombre de tu empresa? ')
extension_dominio = input('Extension del dominio de tu empresa? ')

# Normalizamos los valores recibidos
nombre = nombre.strip().lower().replace(' ','.')
apellidos = apellidos.strip().lower().replace(' ', '.')
empresa = empresa.strip().lower().replace(' ', '')
extension_dominio = extension_dominio.strip().lower().replace(' ', '')

# Generar el email
email = f'{nombre}.{apellidos}@{empresa}{extension_dominio}'

print(f'''
Tu nuevo email generado por el sistema es:
    {email}
    Felicidades!''')

