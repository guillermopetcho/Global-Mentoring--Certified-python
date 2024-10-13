# 2. Nuevo Estilo de formato de cadenas en Python
nombre = 'Juan'
mi_cadena = 'Hola, {}'.format(nombre)
print(mi_cadena)

# Podemos convertir enteros a hexadecimales
error = 500
cadena_hexadecimal = 'Error en hexadecimal: {error:x}'.format(error=error)
print(cadena_hexadecimal)
# Ejemplo entero a flotante
entero = 50
cadena_flotante = 'Numero flotante: {entero:0.2f}'.format(entero=entero)
print(cadena_flotante)

# Podemos hacer lo mismo, pero usando String Interpolation (f-string literal)
mi_cadena = f'Hola, {nombre}'
print(mi_cadena)
# Mandar a imprimir directamente
print(f'Hola, {nombre}')
# Este es el mismo ejemplo de hexadecimal con String Interpolation
print(f'Error hexadecimal: {error:x}')
# El mismo ejemplo de impresion de entero a flotante
print(f'Numero flotante: {entero:.2f}')
# Podemos incluir expresiones o llamadas a funciones
a = 10
b = 3
print(f'Dividimos y damos formato: {a/b:.2f}')