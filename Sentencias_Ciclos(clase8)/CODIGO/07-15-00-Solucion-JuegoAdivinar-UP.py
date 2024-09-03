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