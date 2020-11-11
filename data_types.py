"""
Author: Edgar Ocampo
Program: Data Types
"""
# This is a comment

import math

# WElcome to my data types
print('Welcome to my data types python program')
pi_value = "pi is a value"  # data type is str
pi_value_2 = math.pi  # 3.141592653589793 float type
pi_value_3 = 3  # int data type
list_of_strings = ['Cris', 'Edd', 'Evan', 'Karime', 'Juanito']  # list
query_made = """SELECT * FROM STUDENTS WHERE id = 1 """

#for value in query_made:
#    list_of_strings.append(value)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[0][0])

dict_data_type = {
    "nombre": "Juan Perez",
    "nivel": "C",
    "goles": 10,
    "sueldo": 50000,
    "bono": 25000,
    "sueldo_completo": None,
    "equipo": "rojo"
}

list_of_strings.append(2)
list_of_strings.pop(1)

print(list_of_strings[3])
print(type(dict_data_type))
print(dict_data_type['sueldo'])

# input is a function that allows do a request to the user and write in keywoard by the user
#name = input('Whats your name>?')
#print("Hello, welcome to my programa on python 3", name)

# Adding two numbers
#first_number = input('Gimme the first number')
#second_number = input('Gimme the second number')
#result = int(first_number) + int(second_number)
#print('The result adding your 2 numbers is:', result)
