# Crear una clase para definir una clase de excepcion personalizada
# Ej. Validar que un nombre no pueda tener menos de 3 caracteres

# Este tipo de validacion no indica cual es el problama en especifico
def validar(nombre_completo):
    if len(nombre_completo) < 3:
        raise ValueError
    else:
        print('Validacion correcta...')

nombre = 'Pi'
# validar(nombre)

# Validacion personalizada, indica cual es el problemas, y queda autodocumentado
class NombreDesmasiadoCorto(ValueError):
    pass

def validar_mejorado(nombre_completo):
    if len(nombre_completo) < 3:
        raise NombreDesmasiadoCorto(nombre_completo)
    else:
        print('Validacion correcta...')

nombre = 'Ka'
validar_mejorado(nombre)