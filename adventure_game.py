def regresar():
    print('regresar')

def condition_food():
    food = 'tacos'
    if food == 'tacos':
        #condition body
        print('I hate the tacos')
    else:
        #else condition body
        print('I prefer the hamburguers')

def condition_age_adventure(age: int)-> str:
    if age >= 5:
        #condition body
        print('Bien, pues iniciemos el juego, te vas a divertir...')
    else:
        #else condition body
        print('Serias tan amable de continuar mas tarde...')

def move_player(orientation: str)-> str:
    if orientation == 'sur':
        print('Decidiste ir hacia el sur.')
        regresar()
    elif orientation == 'norte':
        print('Decidiste ir hacia el norte.')
    elif orientation == 'oeste':
        print('Decidiste ir hacia el oeste.')
    elif orientation == 'este':
        print('Decidiste ir hacia el este.')
    else:
        print('No reconozco la orientacion que quieres tomar, por favor intenta de nuevo.')


def four_option_example_adventure():
    my_options = ['map'.upper(),'lighter'.upper(),'bottle water'.upper(),'bag'.upper()]
    for e in my_options:
        if e == 'MAP':
            print('Congratulations you choose the best item to find the done way')
        else:
            print('You got another item...')
    

if __name__ == "__main__":
    import time
    print('Welcome to the Adventure Edd Game')
    print('Espero que te encuentres bien, me gustaria comenzar a conocerte...')
    time.sleep(3)
    age = int(input('Me gustaria conocer tu edad para hacerle configuracion al juego e iniciar. '))
    condition_age_adventure(age)
    orientation = input('Elige tecleando tu orientacion')
    move_player(orientation)
    # igual a  ==
    # diferente de!= 
    # mayoro iguak a >= 
    # menor o igual a<=
    


