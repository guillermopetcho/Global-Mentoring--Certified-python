import mysql.connector

personas_db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='admin',
    database='personas_db'
)

cursor = personas_db.cursor()
cursor.execute('SELECT id, nombre, apellido, edad FROM personas')
resultado = cursor.fetchall()
for persona in resultado:
    print(persona)

personas_db.close()
