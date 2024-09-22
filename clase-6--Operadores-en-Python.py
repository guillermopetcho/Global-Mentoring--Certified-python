# Operadores Artiméticos

a = 10
b = 3

# Suma +
suma = a + b
print(f'Suma: {suma}')

# Resta -
resta = a - b
print(f'Resta: {resta}')

# Multiplicación *
multiplicacion = a * b
print(f'Multiplicación: {multiplicacion}')

# División / (retorna un tipo float)
division = a / b
print(f'División: {division:.2f}')

# División entera (//)
division_entera = a // b
print(f'División entera: {division_entera}')

# Modulo (%) residuo de la división
modulo = a % b
print(f'Residuo de la división: {modulo}')

# Exponente (potencia) **
exponente = a ** b  # 10 elevado a la 3 = 10*10*10=1000
print(f'Exponente: {exponente}')


print("---------------------------")

print('*** Operadores de Asignación ***')
numero = 5
print(f'Valor de numero: {numero}')
numero = 10
print(f'Valor de numero: {numero}')
cadena = 'Saludos desde Python'
print(f'Valor de la cadena: {cadena}')

print("---------------------------")

print('*** Operadores de Asignación ***')
numero = 5
print(f'Valor de numero: {numero}')
numero = 10
print(f'Valor de numero: {numero}')
cadena = 'Saludos desde Python'
print(f'Valor de la cadena: {cadena}')

# Asignacion multiple
x, y, z = 5, 'Hola', -9.15
print(f'Valor de x = {x}, y = {y}, z = {z}')

# Asignacion encadenada.
a = b = c = 10
print(f'Valor a = {a}, b = {b}, c = {c}')

print("---------------------------")

print('*** Operadores de Asignación ***')
numero = 5
print(f'Valor de numero: {numero}')
numero = 10
print(f'Valor de numero: {numero}')
cadena = 'Saludos desde Python'
print(f'Valor de la cadena: {cadena}')

# Asignacion multiple
x, y, z = 5, 'Hola', -9.15
print(f'Valor de x = {x}, y = {y}, z = {z}')

# Asignacion encadenada.
a = b = c = 10
print(f'Valor a = {a}, b = {b}, c = {c}')

# Intercambio de valores de una variable, sin utilizar variables temporales
x, y = 5, 10
print(f'Valores iniciales x = {x}, y = {y}')
# Aplicando el concepto de asignacion multiple, intercambiamos valores
x, y = y, x
print(f'Invertir los valores x = {x}, y = {y}')

# Recibir multiples valores de la entrada del usuario
nombre, apellido = input('Ingresa tu nombre y apellido separados por coma: ').split(',')
print(f'Nombre: {nombre.strip()}, Apellido: {apellido.strip()}')

print("---------------------------")

print('*** Operadores Comparación (Relacionales) ***')
a, b = 7, 5
print(f'Valor inicial a: {a}, b: {b}')

# Operador igualdad ==
resultado = a == b
print(f'Resultado a == b es: {resultado}')

# Operador diferente !=
resultado = a != b
print(f'Resultado a != b es: {resultado}')

# Operador mayor que >
resultado = a > b
print(f'Resultado a > b es: {resultado}')

# Operador mayor o igual que >=
resultado = a >= b
print(f'Resultado a >= b es: {resultado}')

# Operador menor que
resultado = a < b
print(f'Resultado a < b es: {resultado}')

# Operador menor o igual que:
resultado = a <= b
print(f'Resultado a <= b es: {resultado}')

print("---------------------------")

print(f'*** Operador and ***')
# Regresa verdadero si ambos valores a evaluar son verdaderos
condicion1 = True
condicion2 = True
resultado = condicion1 and condicion2
print(f'Resultado {condicion1} and {condicion2}: {resultado}')



print("---------------------------")

print('*** Sistema Descuentos VIP ***')

NO_PRODUCTOS_DESCUENTO = 10
cantidad_productos = int(input('Cuantos productos compraste hoy? '))
tiene_membresia = input('Tienes la membresía de la tienda (Si/No)? ')

es_elegible_descuento = (cantidad_productos >= NO_PRODUCTOS_DESCUENTO
                         and tiene_membresia.strip().lower() == 'si')

print(f'Tienes acceso al descuento VIP? {es_elegible_descuento}')


print("---------------------------")

print('*** Operador lógico or ***')
condicion1 = True
condicion2 = True
# El operador or regresa True si cualquiera de los operandos es True
resultado = condicion1 or condicion2
print(f'Resultado {condicion1} or {condicion2} es: {resultado}')

print("---------------------------")

print('*** Sistema Prestamo de Libros ***')

DISTANCIA_PERMITIDA_KM = 3
tiene_credencial = input('Cuentas con credencial de estudiante (Si/No)? ')
distancia_biblioteca_km = int(input('A cuantos km vives de la biblioteca? '))

es_elegible_prestamo = (tiene_credencial.strip().lower() == 'si'
                        or distancia_biblioteca_km <= DISTANCIA_PERMITIDA_KM)

print(f'Eres elegible para prestamo de libros? {es_elegible_prestamo}')

print("---------------------------")

print('*** Operador not ***')

condicion1 = True
resultado = not condicion1
print(f'Operador not sobre {condicion1}: {resultado}')

# Revisar si una variable es cadena vacia
nombre = ''
es_cadena_vacia = not nombre
print(f'\nLa variable NO tiene ningún valor? {es_cadena_vacia}')

# Revisar si una variable no tiene ningún valor asignado
variable = None
es_variable_sin_valor = not variable
print(f'\nLa variable NO tiene ningún valor asignado? {es_variable_sin_valor}')
print("---------------------------")

# Revisar si una variable se encuentra dentro de rango entre 1 y 10
dato = int(input('Proporciona un dato entero: '))

# Revisamos si está dentro de rango
# esta_dentro_rango = 1 <= dato <= 10
# print(f'Variable está dentro de rango (entre 1 y 10)? : {esta_dentro_rango}')

# Revisamos la lógica inversa, si el dato está fuera de rango
esta_fuera_rango = not(1 <= dato <= 10)
print(f'Variable está fuera de rango (entre 1 y 10)? {esta_fuera_rango}')

print("---------------------------")

print('*** Generación Ticket de Venta ***')

precio_leche = float(input('Precio leche: '))
precio_pan = float(input('Precio pan: '))
precio_lechuga = float(input('Precio lechuga: '))
precio_platanos = float(input('Precio plátanos: '))

# Cálculo del subtotal (sin impuestos)
subtotal = precio_leche + precio_pan + precio_lechuga + precio_platanos

# Calculo con impuestos (16%)
impuesto = subtotal * 0.16

# Calculo total de la compra (con impuestos)
costo_total_compra = subtotal + impuesto
print(f'''
Subtotal: ${subtotal:.2f}
Impuesto (16%): ${impuesto:.2f}
Costo total de la compra: ${costo_total_compra:.2f}''')

print("---------------------------")


print('*** Generación Ticket de Venta ***')

precio_leche = float(input('Precio leche: '))
precio_pan = float(input('Precio pan: '))
precio_lechuga = float(input('Precio lechuga: '))
precio_platanos = float(input('Precio plátanos: '))
descuento_porcentaje = int(input('Aplicar algún descuento (%)? '))

# Cálculo del subtotal (sin impuestos)
subtotal = precio_leche + precio_pan + precio_lechuga + precio_platanos

# Aplicar el descuento
descuento = subtotal * (descuento_porcentaje/100)

# Subtotal con descuento
subtotal_con_descuento = subtotal - descuento

# Calculo con impuestos (16%)
impuesto = subtotal_con_descuento * 0.16

# Calculo total de la compra (con impuestos)
costo_total_compra = subtotal_con_descuento + impuesto
print(f'''
Subtotal: ${subtotal:.2f}
Descuento: ${descuento} ({descuento_porcentaje}%)
Subtotal con descuento: ${subtotal_con_descuento}
Impuesto (16%): ${impuesto:.2f}
Costo total de la compra: ${costo_total_compra:.2f}''')


print("---------------------------")

print('*** Valor Dentro de Rango ***')

MINIMO = 0
MAXIMO = 5

# Solicitamos un valor entre 0 y 5
dato = int(input(f'Proporciona un dato entre {MINIMO} y {MAXIMO}: '))

# Verificamos si el dato se encuentra dentro de rango
#esta_dentro_rango = dato >= MINIMO and dato <= MAXIMO
esta_dentro_rango = MINIMO <= dato <= MAXIMO
print(f'Valor está dentro de rango? {esta_dentro_rango}')


print("---------------------------")


print('*** Cáculo Área y Perímetro de un Rectángulo ***')

base = float(input('Ingresa la base del rectángulo: '))
altura = float(input('Ingresa la altura del rectángulo: '))

# Realizamos los cálculos
area = base * altura
perimetro = 2 * (base + altura)  # Aplicado la precedencia de operadores

print(f'El área del rectángulo es: {area}')
print(f'El perímetro del rectángulo es: {perimetro}')


print("---------------------------")

# 1. Paréntesis (): Los paréntesis tienen la mayor precedencia
# 2. Exponente **: Este operador calcula la potencia de un número.
# 3. Unario +, -: Estos operadores realizan operaciones unarias de positivo y negativo
# 4. Multiplicación *, División /, División entera //, Módulo %
# 5. Suma +, Resta -: Estos operadores realizan operaciones aritméticas.
# 6. Comparaciones (==, !=, >, <, >=, <=)
# 7. Operadores lógicos not, and, or
# 8. Asignación (=, +=, -=, *=, /=, entre otros)

# Ejemplo de precedencia de operadores
# 1. Division 12 / 3 = 4
# 2. Multiplicacion 2 * 3 = 6
# 3. Suma 4 + 6 = 10
# 4. Resta 10 - 1 = 9
resultado = 12 // 3 + 2 * 3 - 1
print(f'Resultado: {resultado}')


print("---------------------------")
