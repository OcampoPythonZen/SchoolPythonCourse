"""
Escribir un programa que muestre en pantalla
el seguimiento o sombra de todo lo que el usuario introduzca
hasta que el usuario escriba exit, saldra de la sombra o ejecucion.
"""
# while true permite ejecutar un buble o loop indeterminadas veces
# break nos permite cortar o finalizar ese bucle o loop indeterminado
while True:
    phrase = input("Type down your text: ")
    if phrase == "exit()":
        break
    print(phrase)