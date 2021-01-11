'''
Title: Class Example
Author: Edgar
Fecha 17-11-20
'''


def cualquiera():
    return f'This is a function into class_example has cualquiera name'


class Rabbit():

    def compare(self, parametro):
        if parametro == 'parametro':
            return parametro

    _color = None
    _nombre = None
    _camada = range(5, 8)
    _patas = 4
    _ojos = 2
    _orejas = 2
    _esta_lleno = False
    _roe = False
    _esta_saltando = 'No esta saltanfo el conejo, esta sobre sus 4 patas'

    def __init__(self, color, nombre):
        self._color = color
        self._nombre = nombre

    def salta(self):
        self._esta_saltando = 'Ahora tu conejo ha dado un salto'

    def comer(self):
        self._esta_saltando = True

    def roe(self):
        self._roe = True

    def __str__(self):
        return f'Tienes un hermoso conejo de nombre {self._nombre}, tiene un color {self._color} el cual tiene {self._patas} y {self._ojos} ojos y {self._orejas} hermosas orejas'


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
    _color = None  # None- Keyword es un tipo de dato que significa que no tiene valor
    # Es decir similar a otros lenguajes con la palabra null.
    _numero_llantas = 4  # variable asignada desde el incio con un valor especifico - int
    _num_puertas = None  # 2, 3, 4, 5. dependiendo que tipo de carro
    _transmision = None
    # 1 o 0 -- boolean quiere decir que solo acepta dos valores: True or False
    _en_marcha = False

    def __init__(self, color, numero_llantas, num_puertas, transmision):
        '''
        __init__ inicializador de mi clase que toma los parametros al instanciar mi clase.
        siempre que tenga un funcion dentro de una clase, necesito la palabra reservada self.
        dentro del inicializador necesito igualar mis propiedad de la clase con el parametro que
        recibe la clase.
        '''
        self._color = color  # Asignar el color del parametro recibido a la propiedad de mi clase
        # Asignar numero de llantas del parametro recibido a la propiedad de mi clase
        self._numero_llantas = numero_llantas
        # Asignar numero de puertas del parametro recibido a la propiedad de mi clase
        self._num_puertas = num_puertas
        # Asignar la transmision del auto por parametro recibido a la propiedad o valor de mi clas
        self._transmision = transmision

    def arrancar(self):
        '''
        Para usar las propiedades o variables de la clase utilizare tambien la palabra reservada self
        '''
        self._en_marcha = True
        # f'' imprimir un str formateado e incluyo los valores dentro de {}
        return f'Tu Auto ha arrancado, la marcha esta en: {self._en_marcha}'

    def apagar_marcha(self):
        '''
        cada funcion de la clase debe llevar la palabra reservada self como parametro
        '''
        self._en_marcha = False
        return f'Tu auto ahora se encuentra apagado, la marcha esta en {self._en_marcha}'

    def info_auto(self):
        print(
            f'Tu auto es de color {self._color}, tiene {self._numero_llantas} llantas y su transmision es {self._transmision} y cuenta con {self._num_puertas} puertas')
