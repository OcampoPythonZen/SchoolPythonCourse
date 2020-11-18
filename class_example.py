'''
Title: Class Example
Author: Edgar
Fecha 17-11-20
'''

class Car():
    '''
    Example of Car Class.
    step 1: Use the keyword class 
    step 2: Give a name to the class usinf the Capitalize type
    step 3: put the parenthesis
    step 4: put the double points after parethesis
    step 5: use the identation to put the body of the class
    '''
    
    # properties class.
    _color = None #None- Keyword es un tipo de dato que significa que no tiene valor
    #Es decir similar a otros lenguajes con la palabra null.
    _numero_llantas = 4 #variable asignada desde el incio con un valor especifico - int
    _num_puertas = None # 2, 3, 4, 5. depensiendo que tipo de carro
    _transmision = None
    _en_marcha = False # 1 o 0 -- boolean quiere decir que solo acepta dos valores: True or False


    def __init__(self, color, numero_llantas, num_puertas, transmision):
        self._color = color
        self._numero_llantas = numero_llantas
        self._num_puertas = num_puertas
        self._transmision = transmision

    def arrancar(self):
        self._en_marcha = True
        return f'Tu Auto ha arrancado, la marcha esta en: {self._en_marcha}'

    def apagar_marcha(self):
        self._en_marcha = False
        return f'Tu auto ahora se encuentra apagado, la marcha esta en {self._en_marcha}'

    def info_auto(self):
        print(
            f'Tu auto es de color {self._color}, tiene {self._numero_llantas} llantas y su transmision es {self._transmision} y {self._num_puertas} puertas')


if __name__ == "__main__":
    evan_car = Car('Rojo', 4, 4, 'automatica')
    evan_car.info_auto()
    print(evan_car.arrancar())

    cris_car = Car('Rosita', 4, 5, 'automatico')
    cris_car.info_auto()

    ed_car = Car('Neon', 4, 4, 'estandar')
    ed_car.info_auto()
