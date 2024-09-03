class Aritmetica:

    def __init__(self, operando1=None, operando2=None):
        self._operando1 = operando1
        self._operando2 = operando2

    def sumar(self):
        resultado = self._operando1 + self._operando2
        print(f'Resultado suma: {resultado}')

    def restar(self):
        resultado = self._operando1 - self._operando2
        print(f'Resultado resta: {resultado}')

    def multiplicar(self):
        resultado = self._operando1 * self._operando2
        print(f'Resultado multiplicación: {resultado}')

    def dividir(self):
        resultado = self._operando1 / self._operando2
        print(f'Resultado división: {resultado}')

    @property
    def operando1(self):
        return self._operando1

    @operando1.setter
    def operando1(self, operando1):
        self._operando1 = operando1

    @property
    def operando2(self):
        return self._operando2

    @operando2.setter
    def operando2(self, operando2):
        self._operando2 = operando2

# Programa principal
if __name__ == '__main__':
    print('*** Ejemplo Clase Artimética ***')
    aritmetica1 = Aritmetica(5, 7)
    print('Primer objeto')
    print(f'Valor operando1 del objeto artimetica1: {aritmetica1.operando1}')
    print(f'Valor operando2 del objeto artimetica1: {aritmetica1.operando2}')
    aritmetica1.sumar()
    aritmetica1.restar()
    aritmetica1.operando1 = 9
    aritmetica1.operando2 = 15
    print(f'Valor operando1 del objeto artimetica1: {aritmetica1.operando1}')
    print(f'Valor operando2 del objeto artimetica1: {aritmetica1.operando2}')
    aritmetica1.sumar()
    aritmetica1.restar()

    # Segundo objeto
    print('Segundo objeto')
    aritmetica2 = Aritmetica(12, 16)
    print(f'Valor operando1 del objeto artimetica2: {aritmetica2.operando1}')
    print(f'Valor operando2 del objeto artimetica2: {aritmetica2.operando2}')
    print()
    aritmetica2.sumar()
    aritmetica2.restar()
    # Tercer objeto
    print('Tercer objeto')
    aritmetica3 = Aritmetica(7)
    aritmetica3.operando2 = 9
    aritmetica3.sumar()
    # Cuarto objeto
    print('Cuarto objeto')
    aritmetica4 = Aritmetica()
    aritmetica4.operando1 = 2
    aritmetica4.operando2 = 8
    aritmetica4.sumar()
    # Quinto objeto
    print('Quinto objeto')
    aritmetica5 = Aritmetica(operando2=4, operando1=3)
    aritmetica5.sumar()
