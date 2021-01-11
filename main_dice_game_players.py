from dice_game import DiceGame
from time import sleep as duerme_tantito

if __name__ == "__main__":
    # FIND WINNER BETTWEEEN PLAYERS.
    play = DiceGame()
    number_dice = int(input('Enter number of dice rolls: '))
    ready = input('Ready to start? Hit any key to continue')

    # DECLARE PLAYERS
    player_1 = play.roll_dice(number_dice)
    print('Player_1 first roll:', player_1)
    duerme_tantito(1)
    player_2 = play.roll_dice(number_dice)
    print('Player_2 first roll:', player_2)
    duerme_tantito(1)
    player_3 = play.roll_dice(number_dice)
    print('Player_3 first roll:', player_3)

    # FINAL STEP
    duerme_tantito(3)
    print('FINAL STEP TO SHOW THE WINNER...')
    play.find_winner_beetween_us(
        chucho_dice=player_1, edgar_dice=player_2, hector_dice=player_3)
