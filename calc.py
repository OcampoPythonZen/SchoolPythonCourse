'''
Las funciones se crean con la palabra reservada def
enseguida del nombre de la funcion (sin espacios), entre parentresis sus parametros
despues el tipo de dato que retorna y al final los dos puntos
con la identacion correspondiente, y dentro de esta el cuerpo de la funcion.
La manera correcta de llamar a la funcion es: escribiendo su nombre con los parentisis.
'''

def my_first_function():
    print('This is my first function')


def suma(a: int, b: int) -> int:
    '''
    regresa la suma de dos numeros
    '''
    return a + b


def resta(a: int, b: int) -> int:
    '''
    regresa la resta de dos numeros
    '''
    return a - b


def multiplicacion(a: int, b: int) -> int:
    '''
    regresa la multiplicacion de dos numeros
    '''
    return a * b


def division(a: int, b: int) -> float:
    '''
    regresa la division de dos numeros
    '''
    return a / b


if __name__ == "__main__":
    """ print('El resultado de la suma es:', suma(2, 2))
    print('El resultado de la resta es:', resta(2, 2))
    print('El resultado de la multiplicacion es:', multiplicacion(2, 2))
    print('El resultado de la division es:', division(2, 2)) """
    my_first_function()

