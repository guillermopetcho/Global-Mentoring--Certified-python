print(f'*** Sentencia if ***')

edad = 10
if edad >= 18:
    print(f'Eres mayor de edad. Tienes {edad} años')
#     print()
#     print()
# print()
# print()

print("---------------------------------------------------------------------")
print(f'*** Sentencia if ***')

edad = 30
if edad >= 18:
    print(f'Eres mayor de edad. Tienes {edad} años')
else:
    print(f'Eres menor de edad. Tienes {edad} años')


print("---------------------------------------------------------------------")
print('*** Revisión Valor Positivo ***')

numero = int(input('Proporciona un número: '))

if numero > 0:
    print(f'Es positivo: {numero}')
elif numero < 0:
    print(f'Es negativo: {numero}')
else:
    print(f'Es cero {numero}')
print("---------------------------------------------------------------------")
print('*** Sistema Tienda en Línea con Descuentos ***')

# Codiciones
MONTO_COMPRA_DESC = 1000

monto_compra = float(input('Cual fue el monto de tu compra? '))
es_miembro = input('Eres miembro de la tienda (Si/No)? ')

descuento = 0
# Verificar cada caso, con los datos proporcionados
if monto_compra >= MONTO_COMPRA_DESC and es_miembro.strip().lower() == 'si':
    descuento = 0.1  # Descuento del 10%
elif es_miembro.strip().lower() == 'si':
    descuento = .05  # Descuento del 5%
elif monto_compra >= MONTO_COMPRA_DESC:
    descuento = .03  # Descuento del 3%
else:
    descuento = 0

# Hacemos los cálculos respectivos para obtener el monto final
if descuento != 0:
    monto_descuento = monto_compra * descuento
    monto_final = monto_compra - monto_descuento
    print(f'\nFelicidades, has obtenido un descuento del {descuento * 100:.0f}%')
    print(f'Monto de la compra: ${monto_compra:.2f}')
    print(f'Monto del descuento: ${monto_descuento:.2f}')
    print(f'Monto final de la compra con descuento: ${monto_final:.2f}')
else:
    print('\nNo obtuviste ningún tipo de descuento')
    print('Te invitamos a hacerte miembro de la tienda')
    print(f'Monto final de la compra: ${monto_compra:.2f}')
print("---------------------------------------------------------------------")
print('*** Bienvenidos al Sistema Bancario ***')

salir_sistema_txt = input('Deseas salir del sistema (Si/No)? ')
salir_sistema = salir_sistema_txt.strip().lower() == 'si'

if not salir_sistema:
    print('Continuamos dentro del sistema')
else:
    print('Salimos del sistema')

print("---------------------------------------------------------------------")
print('*** Bienvenidos a la Casa de los Espejos ***')

edad = int(input('Cuál es tu edad? '))
tienes_miedo_oscuridad = input('Tienes miedo a la oscuridad (Si/No)? ')
tienes_miedo_oscuridad = tienes_miedo_oscuridad.strip().lower() == 'si'

if not tienes_miedo_oscuridad and edad >= 10:
    print('Puedes entrar a la Casa de los Espejos')
else:
    print('Lo siento, la Casa de los Espejos podría darte miedo')

print("---------------------------------------------------------------------")
print(f'*** Operador Ternario ***')

edad = int(input('Cual es tu edad? '))

es_adulto = 'Si' if edad >= 18 else 'No'
print(f'Es un adulto? {es_adulto}')

print("---------------------------------------------------------------------")
print('*** Aplicación de Salud y Fitness ***')

# Constantes
META_PASOS_DIARIO = 10000
CALORIAS_POR_PASO = 0.04 # Valor aproximado, son kilocalorias

# Pedimos los valores al usuario
nombre_usuario = input('Cuál es tu nombre? ')
pasos_diarios = int(input('Cuántos pasos has caminado hoy? '))

# Verificar si el usuario alcanzó la meta de pasos diarios
meta_alcanzada = pasos_diarios >= META_PASOS_DIARIO
meta_alcanzada_txt = 'Sí' if meta_alcanzada else 'No'
# Calculamos las calorias quemadas
calorias_quemadas = pasos_diarios * CALORIAS_POR_PASO

# Mostramos la información
print(f'\nUsuario: {nombre_usuario}')
print(f'Pasos dados hoy: {pasos_diarios}')
print(f'Calorías quemadas: {calorias_quemadas} kcal')
print(f'Meta de pasos diario alcanzada: {meta_alcanzada_txt}')
print(f'La meta de pasos diarios es de: {META_PASOS_DIARIO} pasos')
print("---------------------------------------------------------------------")
print('*** Sistema de Reserva de Hotel ***')

# Variables del hotel
tarifa_diaria_sin_vista_mar = 150.50
tarifa_diaria_con_vista_mar = 190.50

# Pedimos la informacion al usuario
nombre_cliente = input('Nombre del Cliente: ')
dias_estadia = int(input('Días de estadía: '))
vista_al_mar_txt = input('Con vista al mar (Si/No)? ')
vista_al_mar = vista_al_mar_txt.strip().lower() == 'si'

# Cálculo del costo total de la estancia
if vista_al_mar:
    costo_total = dias_estadia * tarifa_diaria_con_vista_mar
else:
    costo_total = dias_estadia * tarifa_diaria_sin_vista_mar

# Mostramos los detalles de la reserva
print('\n--------- Detalles de la Reservación ------------')
print(f'Cliente: {nombre_cliente}')
print(f'Días de estadía: {dias_estadia}')
print(f'Costo total: ${costo_total:.2f}')
print(f'Habitación con vista al mar: {'Sí' if vista_al_mar else 'No'}')
print("---------------------------------------------------------------------")
print('*** El mayor de dos números ***')

numero1 = int(input('Proporciona el número 1: '))
numero2 = int(input('Proporciona el número 2: '))

# El mayor de dos números
if numero1 > numero2:
    print(f'El número 1 es mayor: {numero1}')
else:
    print(f'El número 2 es mayor: {numero2}')
print("---------------------------------------------------------------------")
print('*** Estación del Año ***')

mes = int(input('Proporciona el valor del mes (1-12): '))
estacion = None
# Revisión del mes proporcionado
if mes == 1 or mes == 2 or mes == 12:
    estacion = 'Invierno'
elif mes == 3 or mes == 4 or mes == 5:
    estacion = 'Primavera'
elif mes == 6 or mes == 7 or mes == 8:
    estacion = 'Verano'
elif mes == 9 or mes == 10 or mes == 11:
    estacion = 'Otoño'
else:
    estacion = 'Estación desconocida'
# Imprimir el resultado
print(f'La estación para el mes {mes} es {estacion}')

print("---------------------------------------------------------------------")
print('*** Sistema de Calificaciones ***')

calificacion = float(input('Proporciona una calificación entre 0 y 10: '))
calificacion_letra = None
# Revisamos si está en los siguientes rangos
if 9 <= calificacion <= 10:
    calificacion_letra = 'A'
elif 8 <= calificacion < 9:
    calificacion_letra = 'B'
elif 7 <= calificacion < 8:
    calificacion_letra = 'C'
elif 6 <= calificacion < 7:
    calificacion_letra = 'D'
elif 0 <= calificacion < 6:
    calificacion_letra = 'F'
else:
    calificacion_letra = 'Calificacion incorrecta'

# Imprimir el resultado
print(f'Calificación {calificacion} es equivalente a {calificacion_letra}')
print("---------------------------------------------------------------------")
print('*** Sistema de Envíos ***')

# Definimos las tarifas de envío por kilogramo
TARIFA_NACIONAL = 10
TARIFA_INTERNACIONAL = 20

# Solicitamos los valores de destino y peso al usuario
destino = input('Ingresa el destino del paquete (nacional/internacional): ')
peso = float(input('Ingresa el peso del paquete (en kg): '))

# Cálculo del envío del paquete
costo_envio = None
destino = destino.strip().lower()
if destino == 'nacional':
    costo_envio = peso * TARIFA_NACIONAL
elif destino == 'internacional':
    costo_envio = peso * TARIFA_INTERNACIONAL
else:
    print('Destino no válido. Ingresa el valor de nacional o internacional')

# Mostramos el costo de envío sólo si es un valor válido
if costo_envio is not None:
    print(f'El costo de envío del paquete es: ${costo_envio:.2f}')
print("---------------------------------------------------------------------")
print('*** Sistema de Autenticación ***')

USUARIO_VALIDO = 'admin'
PASSWORD_VALIDO = '123'

usuario = input('Ingresa tu usuario: ')
password = input('Ingresa tu password: ')

if usuario == USUARIO_VALIDO and password == PASSWORD_VALIDO:
    print('Bienvenido al Sistema')
elif usuario == USUARIO_VALIDO:
    print('Password incorrecto, favor de corregirlo!')
elif password == PASSWORD_VALIDO:
    print('Usuario incorrecto, favor de corregirlo!')
else:
    print('Usuario y password incorrectos, favor de corregirlos!')

print("---------------------------------------------------------------------")

