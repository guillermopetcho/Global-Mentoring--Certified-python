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