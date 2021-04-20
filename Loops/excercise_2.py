"""
Escribir un programa que pida al usuario un numero
entero (int) y muesr por la pantalla un triangulo rectangulo
con el simbolo de asteriscos ejemplo
"""
u=int(input('De qué tamaño deseas tu triángulo'))
for i in range(u):
    for l in range(i+1):
        print('*',end='')
    print('')    