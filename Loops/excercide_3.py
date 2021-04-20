"""
Escribir un programa que muestre en pantalla
el seguimiento o sombra de todo lo que el usuario introduzca
hasta que el usuario escriba exit, saldra de la sombra o ejecucion.
"""
input = input("Type Something..")

while True:
    if input == 'exit':
        break
    print(input)

