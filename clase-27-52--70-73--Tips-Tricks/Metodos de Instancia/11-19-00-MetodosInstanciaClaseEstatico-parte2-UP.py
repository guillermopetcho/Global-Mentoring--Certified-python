# Metodos de instancia, clase y static y sus diferencias
class MiClase:

    def metodo_instancia(self):
        # Retornamos una tupla
        return 'Metodo de instancia ejecutado...', self

    @classmethod
    def metodo_clase(cls):
        # Retornar una tupla
        return 'Metodo de clase ejecutado...', cls

    @staticmethod
    def metodo_estatico():
        return 'Metodo estatico ejecutado...'

# Caso 1. Ejecutamos el metodo de instancia de manera implicita
objeto = MiClase()
print(objeto.metodo_instancia())
# Caso 2. Ejecutamos el metodo de instancia de manera explicita
print(MiClase.metodo_instancia(objeto))

# Caso 3. Ejecutamos el metodo de instancia desde la clase
print(MiClase.metodo_instancia(MiClase))

# Caso 4. Ejecutamos el metodo de clase
print(MiClase.metodo_clase())
# Caso 5. Desde las instancias podemos acceder a los metodos de clase
print(objeto.metodo_clase())

# Caso 6. Ejecutamos el metodo estatico
print(MiClase.metodo_estatico())
# Caso 7. Desde la instancia
print(objeto.metodo_estatico())

# En resumen:
# La clase no puede acceder los metodos de instancia (Caso 2)
# a menos que se proporcione una instancia
# Pero los objetos si pueden acceder a los metodos de clase y estaticos (Casos 5 y 7)
# Los metodos de clase pueden modificar el estado de la clase (variables de instancia)
# pero no tiene acceso a las variables de instancia (No tiene acceso a self)

# Los metodos de instancia puede modificar tanto el estado del objeto (variables de instancia)
# asi como el estado de la clase (variables de clase) usando self.__class__

# Los metodos estaticos no tienen acceso a cls ni self, por lo que no pueden modificar
# el estado del objeto ni el estado de la clase
# Los metodos estaticos son funciones normales pero asociadas a una clase
# que indican que su intencion no es modificar el estado de la clase ni del objeto
# ya que no tienen relacion directa con estos estados por que NO acceden a self ni cls
# Esto permite mostrar la intencion del programador de usar metodos estaticos

# Recordar que self y cls es solo un nombre que se usa por estandar, pero puede modificarse