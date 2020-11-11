'''
Title: Class Example
Autho: Edgar
Fecha 04-11-20
'''


class Car():

    _color = None
    _numero_llantas = 4
    _num_puertas = None
    _transmision = None
    _en_marcha = False

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

    ed_car = Car('NEon', 4, 4, 'estandar')
    ed_car.info_auto()
