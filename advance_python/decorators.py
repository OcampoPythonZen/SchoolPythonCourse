'''
Author : Ed
Topic: Decorators on Python
Description : El proposito de este ejercicio es 
demostrar y comprender el uso de decoradores,
siendo este un tema principal pero avanzado en python.
'''

from time import sleep as duerme

def decorador(func):
    def nueva_funcion():
        print('---- El perro ladra y dice: --------')
        func()
    return nueva_funcion

@decorador
def saluda():
    print('Hola soy el perro')

@decorador
def despedida():
    print('Adios soy el perrito')

if __name__ == '__main__':
    saluda()
    duerme(2)
    despedida()