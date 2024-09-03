print('*** Operaciones con Set ***')

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

union = a | b
print(f'Union a | b: {union}')

interseccion = a & b
print(f'Intersección a & b {interseccion}')

diferencia = a - b
print(f'Diferencia a - b {diferencia}')