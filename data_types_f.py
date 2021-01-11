'''
Author: Edgar Ocampo
Date: 07/01/2021
Topic: Data types, Functions and comment example.
'''
# keywords o palabras reservadas de python: Son palabras
# reservadas por python que utiliza el lenguaje.
# Example: def, int, float, this, self, for, class, import, etc.

# How to create a function
# 1.- usar la -palabra clave def dar un espacio, enseguida del nombre de mi funcion
# 2.- despues del nombre poner parentesis y dos puntos
# 3.- darle enter y dentro de la identación escribir el cuerpo de esta

# 'str o cadena de texto o string o caracter' -> str
# integer valores negativos y positivos de una sola cifra, numeroes reales -> int
# numeros flotantes o float son numeros con punto flotante, decimales. -> float
# listas o list son coleccion de datos de un tipo o varios -> var = [1,'dos', 3.3] -> list
# range o variable de rango que genera los valores con una variable incial, de salto y variable final
# range(1,1000,5) comienza en uno, termina en diez y salta de de dos en dos.
# set=() list=[] dict={}


def str_data_type() -> str:
    '''
    This is a function to show the 'str' data type
    '''
    a = 'a'
    full_name = "edgar omar ocampo bernal"
    print('This is the type of:', a, "Type:", type(a))
    print('This is the type of:', full_name, "Type:", type(full_name))


def list_data_type(parameter: list) -> int:
    """
    This a function to show the list type and pass a list as parameter to calculate the length.
    """
    print('Thi is your list var:', parameter)
    # len() function to calculate the length of a variable
    return len(parameter)


def my_fisrt_function() -> str:
    # function without parameters
    print('thi is my first function to show how to do it.')


def range_data_type():
    """
    This is a function to show the range data type
    """
    from_one_until_ten = range(0, 100, 5)
    # for -> ciclo que genera tareas repetitivas.
    # for target_list in expression_list: -> syntaxis
    for element in from_one_until_ten:
        print(element)


def addition(a: int, b: int) -> int:
    '''
    This is a function to do a addition of two values
    a = first value to add as parameter
    b = second value to add as parameter
    '''
    return a + b


def sub(a: int, b: int) -> int:
    '''
    This is a function to do a subtraction of two values
    a = first value to add as parameter
    b = second value to add as parameter
    '''
    return a - b


def mul(a: int, b: int) -> int:
    '''
    This is a function to do a multiplication of two values
    a = first value to add as parameter
    b = second value to add as parameter
    '''
    return a * b


def div(a: float, b: float) -> float:
    '''
    This is a function to do a divition of two values
    a = first value to add as parameter
    b = second value to add as parameter
    '''
    return a / b


# Explain the main menu on python...
# the main menu execute at the first time when We run a pytho file
if __name__ == "__main__":
    # How to call my function?
    # write the name before the phartentesis
    # my_fisrt_function()
    #print('Addition:', addition(2, 20))
    #print('Subtraction:', sub(10, 1))
    #print('Multiplication:', mul(9, 9))
    #print('Division:', div(9.0, 3.0))
    # str_data_type()
    #parameter = ['fer', 34, 'edgar', 3.141516, 'polanco','cute', range(0,7)]
    #print(list_data_type(parameter), ' elements')
    range_data_type()
