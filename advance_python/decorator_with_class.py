
def decorador(fun):
    def funcion_interna(self, mensaje, mensaje2):
        print('Hola!...')
        fun(self, mensaje, mensaje2)
    return funcion_interna


def add_another_var(fun):
    def add(self, a, b):
        # logica
        another_value = int(input('Cual es el valor que vas a agregar a la operacion?: '))
        final_result = a+ b + another_value
        return final_result
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


class OperacionesBasicas(object):
    @add_another_var
    def suma(self, a: int, b: int) -> int:
        result = a+b
        return result

    def resta(self, a: int, b: int) -> int:
        result = a-b
        return result


if __name__ == '__main__':
    #dog = Perro()
    #dog.saluda('Me sientro feliz de ser un perro.', 'bueno, adios...')
    # print('--------------')
    #cat = Gato()
    #cat.saluda('Miauu tengo hambre...', 'bueno adios...')
    calc = OperacionesBasicas()
    print(calc.suma(6, 6))
