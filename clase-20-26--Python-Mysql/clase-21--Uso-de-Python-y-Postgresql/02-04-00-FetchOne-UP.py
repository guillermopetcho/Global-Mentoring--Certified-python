import psycopg2

conexion = psycopg2.connect(user='postgres',password='admin',host='127.0.0.1',port='5432',database='test_db')
#proceso de registro individual
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'SELECT * FROM persona WHERE id_persona = %s'
            id_persona = input('Proporciona el valor id_pesona: ') #podemos hacer un input para que el usuario proporcione el valor
            cursor.execute(sentencia, (id_persona,)) #hacemos la sentencia
            registros = cursor.fetchone() #obtenemos el primer registro
            print(registros)
except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()