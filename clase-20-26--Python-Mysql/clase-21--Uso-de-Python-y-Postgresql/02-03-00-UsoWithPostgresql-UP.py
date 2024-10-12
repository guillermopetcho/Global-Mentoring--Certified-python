import psycopg2

conexion = psycopg2.connect(user='postgres',password='admin',host='127.0.0.1',port='5432',database='test_db')






try:
    with conexion: # with se encarga de cerrar la conección
        with conexion.cursor() as cursor: # with se encarga de cerrar el cursor
            sentencia = 'SELECT * FROM persona'
            cursor.execute(sentencia)
            registros = cursor.fetchall()
            print(registros)
except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close() #tenemos que cerrar la conección manualmente con el finally que siempre se ejecuta