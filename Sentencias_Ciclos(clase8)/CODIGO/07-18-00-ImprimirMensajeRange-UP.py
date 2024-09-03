print('*** Repetición de un Mensaje ***')

mensaje = input('Proporciona un mensaje a repetir: ')
numero_de_repeticiones = int(input('Proporciona el número de repeticiones: '))

# Iterar sobre el rango de repeticiones
for _ in range(numero_de_repeticiones):
    #print(f'{i+1} - {mensaje}')
    print(mensaje)
    