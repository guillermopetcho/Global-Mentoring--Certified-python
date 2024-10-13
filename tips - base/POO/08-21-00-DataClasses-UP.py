from dataclasses import dataclass
from typing import ClassVar


@dataclass
class Persona:
    nombre: str
    apellido: str
    contador_personas: ClassVar[int] = 0

    def __post_init__(self):
        if not self.nombre:
            raise ValueError(f'Valor nombre vacío: {self.nombre}')

persona1 = Persona('Juan','Perez')
print(f'{persona1!r}')
# Variable de clase
print(f'Variable clase: {Persona.contador_personas}')
# Variables de instancia
print(f'Variables de instancia: {persona1.__dict__}')
# Variable con valores vacíos
persona_vacia = Persona('Karla','')
print(f'Persona vacía: {persona_vacia}')