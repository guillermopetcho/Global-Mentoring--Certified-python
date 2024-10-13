import json
import urllib.request

# Debido a cambios en la libreria ahora se deben pasar algunos cabeceros html
peticion = urllib.request.Request(
    'http://globalmentoring.com.mx/api/clima.json',
    data=None,
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
)
respuesta = urllib.request.urlopen(peticion)
# print(respuesta)
cuerpo_respuesta = respuesta.read()
#print(cuerpo_respuesta)
# Procesamos la respuesta json
json_respuesta = json.loads(cuerpo_respuesta.decode('utf-8'))
# print(json_respuesta)
# Ejercicio 1. Acceder a la descripción del clima
# descripcion_clima = json_respuesta.get('clima')[0].get('descripcion')
descripcion_clima = json_respuesta['clima'][0]['descripcion']
print(f'Descripción clima: {descripcion_clima}')
# Ejercicio 2. Mostrar la temperatura mínima y máxima
temp_min = json_respuesta.get('principal').get('temp_min')
print(f'Temperatura mínima: {temp_min}')
temp_max = json_respuesta.get('principal').get('temp_max')
print(f'Temperatura máxima: {temp_max}')