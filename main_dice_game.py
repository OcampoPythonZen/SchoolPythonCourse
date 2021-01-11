from dice_game import DiceGame

import time

if __name__ == "__main__":
    # play es la instanciacion de la clase DiceGame
    play = DiceGame()

    # step 1 in main program area - start game
    number_dice = int(input('Enter number of dice rolls:'))
    ready = input('Ready to start? Hit any key to continue')

    # step 2 in main program are - roll dice
    # User turn to roll
    user_rolls = play.roll_dice(number_dice)
    print('User first roll:', user_rolls)

    # step 3 in main program
    time.sleep(3)
    computer_rolls = play.roll_dice(number_dice)
    print('Computer fisrt roll:', computer_rolls)

    # step 4 in main program
    time.sleep(2)
    print('FINAL STEP TO SHOW THE WINNER...')
    play.find_winner_versus_computer(udice=user_rolls, cdice=computer_rolls)

