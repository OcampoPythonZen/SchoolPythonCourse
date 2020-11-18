import sys
import time

def condition_age_adventure(age: int) -> str:
    if age >= 5:
        print('Bien, pues iniciemos el juego, te vas a divertir...')
        time.sleep(4)
    else:
        print('Serias tan amable de continuar mas tarde...')


def move_player(orientation: str) -> str:
    if orientation == 'sur':
        print('Decidiste ir hacia el sur a cruzar la montaña y pasar por el desierto.')
        time.sleep(3)
        print('Se te presenta una caja donde puede elegir estas opciones...')
        time.sleep(3)
        thing = input('M (map) - B (bag) - BW (bottle water) and L (lantern), escribe la letra de tu eleccion ')
        four_option_example_adventure(thing)
    elif orientation == 'norte':
        print('Decidiste ir hacia el norte.')
    elif orientation == 'oeste':
        print('Decidiste ir hacia el oeste.')
    elif orientation == 'este':
        print('Decidiste ir hacia el este.')
    else:
        print('No reconozco la orientacion que quieres tomar, por favor intenta de nuevo.')


def four_option_example_adventure(thing: str) -> str:
    if thing == 'M':
        print('Congratulations you choose the best item to find the done way, so you WON the game')
    elif thing == 'B':
        print('Dentro de la mochila se habia escondido una serpiente. La serpiente te mordio y perdiste.')
    elif thing == 'BW':
        print('Tomaste la botella de agua y ter permitira seguir avanzando porque estas hidratado')
    elif thing == 'L':
        print('Tomasta la linterna, te servira para ir por ese camino oscuro.')
    else:
        sys.exit("FIN DEL JUEGO, NO ELEGISTE UNA OPCION DE LAS QUE TE PRESENTE :("


if __name__ == "__main__":
    print('Welcome to the Adventure Edd Game')
    print('Espero que te encuentres bien, me gustaria comenzar a conocerte...')
    time.sleep(3)
    age = int(input(
        'Me gustaria conocer tu edad para hacerle configuracion al juego e iniciar esta increible aventura... '))
    condition_age_adventure(age)
    print('Te encuentras en un mundo muy pixeleado donde todo es virtual.')
    time.sleep(3)
    print('No logras ver nada a corta distancia, necesitas tomar tu primera decision...')
    orientation = input('Cual de las cuatro direccion gustas tomar para salir de este mundo, [sur, este, oeste, norte]')
    move_player(orientation)
    # igual a  ==
    # diferente de!=
    # mayoro iguak a >=
    # menor o igual a<=
