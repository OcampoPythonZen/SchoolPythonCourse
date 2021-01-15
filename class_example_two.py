'''
Author: Edd
Fecha: 12/02/2021
Description: Class example with a Dog class
'''

from tkinter import mainloop


class Dog():
    # Steps to create a class in python language
    # 1.- Use the keyword class, before the class name
    # 2.- Put the parenthesis after the class name at the least put the colons(:)
    # 3.- Use the identation to develop the body class with the functions

    # Class properties (vars) to use on all class scope
    color = ''
    size = ''
    legs = 4
    tail = True
    eyes = 2
    nose = True
    mouth = True
    eating_state = ['empty', 'full']

    # Todas las funciones que esten dentro de una clase se les pasa por convencion
    # el primer parametro con la palabra reservada self, significa que pertenece a esa clase.

    def __init__(self, color, size):
        '''
        inicializa los parametros de una clase
        '''
        self.color = color
        self.size = size

    def __str__(self):
        '''
        Retorna la representacion de mi objeto como string
        '''
        return f'the dog is {self.color} color, him size {self.size} and he has {self.legs} legs, he has a {self.validation_tail(self.tail)} tail'

    def validation_tail(self, tail):
        '''
        Function to validate if the Dog has a tail, obviously.
        '''
        if tail == True:
            return 1
        return 0

if __name__ == "__main__":
    edd_dog = Dog('brown','small')
    print(edd_dog)