
def decorador(fun):
    def funcion_interna(self, mensaje, mensaje2):
        print('Hola!...')
        fun(self, mensaje, mensaje2)
    return funcion_interna


def add_another_var(fun):
    def add(self, a, b):
        another_value = int(
            input('Cual seria el otro numero a sumar que necesita? '))
        final_resul = a + b + another_value
        return final_resul
        fun(self, a, b)
    return add


class Animal(object):

    def saludar(self):
        print('Soy clase base de todos estos Animales')


class Perro(Animal):

    @decorador
    def saluda(self, mensaje, mensaje2):
        print(
            f'Soy la clase {self.__class__.__name__}. mensaje 1: {mensaje} y mensaje2: {mensaje2}')


class Gato(Animal):
    @decorador
    def saluda(self, mensaje, mensaje2):
        print(
            f'Soy la clase {self.__class__.__name__}. mensaje 1: {mensaje} y mensaje2: {mensaje2}')


# Agregar la clase que contiene nuestras operaciones a afectar con nuestros decoradores
# Colocar dentro de los parametros de la clase "object" que significa que no heredara de otras clases
# siendo esta la clase base de nuestro ejemplo.
class OperacionesBasicas(object):

    @add_another_var
    def suma(self, a: int, b: int) -> int:
        '''
        Funcion suma que va a hacer afectada por un decorador que cree dentro de mi archivo
        contiene dos parametros para poder realizar la suma de esos dos parametros
        '''
        result = a+b
        return result

    # @add_another_var
    def resta(self, a: int, b: int, c: int) -> int:
        '''
        Funcion resta que va a hacer afectada por un decorador que cree dentro de mi archivo
        contiene dos parametros para poder realizar la resta de esos dos parametros
        '''
        result = (a-b)-c
        return result


if __name__ == '__main__':
    #dog = Perro()
    #dog.saluda('Me sientro feliz de ser un perro.', 'bueno, adios...')
    # print('--------------')
    #cat = Gato()
    #cat.saluda('Miauu tengo hambre...', 'bueno adios...')
    calc = OperacionesBasicas()
    print('La suma total con el tercer operador de mi decorador es: ', calc.suma(3, 3))
    print('La resta total con el tercer operador de mi decorador es: ',
          calc.resta(3, 3, 3))
