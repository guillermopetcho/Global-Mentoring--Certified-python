print('*** Ciclo while ***')

# Imprimir los valores del 1 al 5
contador = 1
while contador <= 5:
    print(contador, end=' ')
    contador += 1  # contador = contador + 1


##--------------------------------------------------------------------------------------------------
##--------------------------------------------------------------------------------------------------


print('*** Ciclo for ***')

print('Recorremos los caracteres de una cadena')
cadena = 'Hola Mundo'
# iteramos los caracteres
for letra in cadena:
    print(letra, end=' ')

print('\n\nRecorremos la lista de frutas:')
frutas = ['Plátano', 'Fresa', 'Mango']
for fruta in frutas:
    print(fruta, end=' ')

##--------------------------------------------------------------------------------------------------
##--------------------------------------------------------------------------------------------------

print('*** Suma Acumulativa ***')

# Sumar los primeros 5 numeros
MAXIMO = 5
numero = 1
acumulador_suma = 0

# Empezamos a iterar
while numero <= MAXIMO:
    # Imprimir lo que se va a sumar
    print(f'(acumulador_suma + numero) -> {acumulador_suma} + {numero}')

    acumulador_suma += numero
    numero += 1

    # Imprimir el resultado de la suma parcial
    print(f'Suma parcial acumulada: {acumulador_suma}\n')

print(f'\nResultado suma acumulada: {acumulador_suma}')

##--------------------------------------------------------------------------------------------------
##--------------------------------------------------------------------------------------------------

print('*** Sistema de Administración de Cuentas ***')

salir = False
while not salir:
    print(f'''Menu:
    1. Crear cuenta
    2. Eliminar cuenta
    3. Salir''')
    opcion = int(input('Escoje una opción: '))
    if opcion == 1:
        print('Creando tu cuenta...\n')
    elif opcion == 2:
        print('Eliminado tu cuenta...\n')
    elif opcion == 3:
        print('Saliendo del sistema. Hasta pronto!\n')
        salir = True
    else:
        print('Opción inválida, proporciona otra opción...\n')
else:
    print('Terminando el sistema de Administración de Cuentas')

##--------------------------------------------------------------------------------------------------
##--------------------------------------------------------------------------------------------------

print('*** Aplicación de Cajero Automático ***')

saldo = 1000
salir = False
while not salir:
    print(f'''Operaciones que puedes realizar:
    1. Consultar Saldo
    2. Retirar
    3. Depositar
    4. Salir''')
    opcion = int(input('Escoje una opción: '))
    if opcion == 1:
        print(f'Tu saldo actual es: ${saldo:.2f}\n')
    elif opcion == 2:
        retiro = float(input('Ingresa el monto a retirar: '))
        # Validacion
        if retiro <= saldo:
            saldo -= retiro  # saldo = saldo - retiro
            print(f'Tu nuevo saldo es: ${saldo:.2f}\n')
        else:
            print(f'No cuentas con el saldo suficiente. Saldo actual es: ${saldo:.2f}\n')
    elif opcion == 3:
        deposito = float(input('Ingresa el monto a depositar: '))
        saldo += deposito  # saldo = saldo + deposito
        print(f'Tu nuevo saldo es: ${saldo:.2f}\n')
    elif opcion == 4:
        print(f'Saliendo del cajero automático. Hasta pronto!')
        salir = True
    else:
        print('Opción inválida. Selecciona otra opción\n')
else:
    print('Terminando la aplicación de Cajero Automático!')

##--------------------------------------------------------------------------------------------------
##--------------------------------------------------------------------------------------------------

print('*** Calculadora en Python ***')

operando1 = operando2 = resultado = 0
salir = False
while not salir:
    print(f'''Operaciones que puedes realizar:
    1. Suma 
    2. Resta
    3. Multiplicacion
    4. Division
    5. Salir''')
    opcion = int(input('Escoje una opción: '))
    # Vamos a solicitar el valor de los operandos
    if 1 <= opcion <= 4:
        operando1 = float(input('Dame el valor 1: '))
        operando2 = float(input('Dame el valor 2: '))
    # Revisamos el tipo de operación a realizar
    if opcion == 1:  # Suma
        resultado = operando1 + operando2
        print(f'El resultado de la suma es: {resultado:.2f}\n')
    elif opcion == 2:  # Resta
        resultado = operando1 - operando2
        print(f'El resultado de la resta es: {resultado:.2f}\n')
    elif opcion == 3:  # Multiplicacion
        resultado = operando1 * operando2
        print(f'El resultado de la multiplicación es: {resultado:.2f}\n')
    elif opcion == 4:
        resultado = operando1 / operando2
        print(f'El resultado de la divión es: {resultado:.2f}\n')
    elif opcion == 5:
        print(f'Saliendo del programa de Calculadora. Hasta pronto!')
        salir = True
    else:
        print(f'Opción inválida, selecciona otra opción...\n')

##--------------------------------------------------------------------------------------------------
##--------------------------------------------------------------------------------------------------

print('Creación y Validación de un Password ***')

password = input('Ingresa un password (debe tener al menos 6 caracteres: ')

# Validar el password
while len(password) < 6:
    print('El password no cumple con los requisitos. Debe tener al menos 6 caracteres')
    password = input('Ingresa un nuevo valor de password: ')
else:
    print('El valor de password es válido')


##--------------------------------------------------------------------------------------------------
##--------------------------------------------------------------------------------------------------

from random import randint

print('*** Juego de Adivinanzas ***')

numero_secreto = randint(1, 50)
intentos = 0
adivinanza = None
INTENTOS_MAXIMOS = 5

while adivinanza != numero_secreto and intentos < INTENTOS_MAXIMOS:
    adivinanza = int(input('Adivina el número secreto (1-50): '))
    # Agregamos una ayuda para orientar al jugador
    if adivinanza < numero_secreto:
        print('El número secreto es mayor')
    elif adivinanza > numero_secreto:
        print('El número secreto es menor')
    # Incrementamos la variable de intentos
    intentos += 1
# Conclusion del juego
if adivinanza == numero_secreto:
    print(f'Felicidades, adivinaste el número secreto en {intentos} intentos')
else:
    print(f'Lo siento, has agotado tus intentos máximos: {INTENTOS_MAXIMOS}')
    print(f'El número secreto era: {numero_secreto}')


##--------------------------------------------------------------------------------------------------
##--------------------------------------------------------------------------------------------------


print('*** Validacion Campo de un Formulario ***')

nombre_usuario = None

while not nombre_usuario:
    nombre_usuario = input('Ingresa tu nombre de usuario: ')

print(f'Nombre de usuario válido: {nombre_usuario}')




##--------------------------------------------------------------------------------------------------
##--------------------------------------------------------------------------------------------------


print('*** Función range ***')

print('Secuencia del 0 al 4: ')
# inicio = 0 (opcional)
# fin = 5 - 1 = 4
# incremento = 1 (opcional)
for i in range(5):  # fin = 5 - 1
    print(i, end=' ')


print('\n\nSecuencia del 10 al 20:')
# incremento = 1 (default y es opcional)
for i in range(10, 20 + 1):
    print(i, end=' ')

print('\n\nSecuencia del 20 al 30 de 2 en 2: ')
for i in range(20, 30 + 1, 2):
    print(i, end=' ')


##--------------------------------------------------------------------------------------------------
##--------------------------------------------------------------------------------------------------

print('*** Repetición de un Mensaje ***')

mensaje = input('Proporciona un mensaje a repetir: ')
numero_de_repeticiones = int(input('Proporciona el número de repeticiones: '))

# Iterar sobre el rango de repeticiones
for _ in range(numero_de_repeticiones):
    #print(f'{i+1} - {mensaje}')
    print(mensaje)



##--------------------------------------------------------------------------------------------------
##--------------------------------------------------------------------------------------------------

print('*** Dibujar Triángulo Simétrico ***')

numero_filas = int(input('Proporciona el número de filas: '))

# Iterar sobre cada fila del triángulo
for fila in range(1, numero_filas + 1):
    espacios_blanco = ' ' * (numero_filas - fila)
    asteriscos = '*' * (2 * fila - 1)
    print(f'{espacios_blanco}{asteriscos}')


##--------------------------------------------------------------------------------------------------
##--------------------------------------------------------------------------------------------------

print('*** break y continue ***')

# Ejemplo con break
print('Palabra break:')
for numero in range(1, 10):
    if numero % 2 == 0:  # numero par
        print(numero)
        break  # Salimos del ciclo inmediatamente

# Ejemplo con continue
print('\nPalabra continue: ')
for numero in range(1, 10):
    if numero % 2 == 1:  # numero impar
        continue
    print(numero)  # numeros pares

##--------------------------------------------------------------------------------------------------
##--------------------------------------------------------------------------------------------------