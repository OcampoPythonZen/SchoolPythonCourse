'''
Fecha: 26/11/2020
Author: Ed
Program: Dice Game
'''

import random
import time


class DiceGame():

    def roll_dice(self, n: int) -> list:
        '''
        This function give us a random number, its depend for the parameter n. n = times number
        '''
        dice = []
        # Add random numbers between 1 and 6 to the list [dice]
        for i in range(n):
            dice.append(random.randint(1, 6))
        return dice

    def find_winner_beetween_us(self, chucho_dice: list, edgar_dice: list, hector_dice: list) -> str:
        total_chucho = sum(chucho_dice)
        print('Chucho Total:', total_chucho)
        total_edgar = sum(edgar_dice)
        print('Edgar Total:', total_edgar)
        total_hector = sum(hector_dice)
        print('Hector Total:', total_hector)
        if total_chucho > total_edgar and total_chucho > total_hector:
            print('Chucho WON!')
        elif total_edgar > total_chucho and total_edgar > total_hector:
            print('Edgar WON!')
        elif total_hector > total_chucho and total_hector > total_edgar:
            print('Hector WON!')
        else:
            print('Sorry, this is a tie beetween Us...')

    def find_winner_versus_computer(self, cdice: list, udice: list) -> str:
        '''
        This fucntion is to decide the final winner
        take one param list per player
        '''
        computer_total = sum(cdice)
        user_total = sum(udice)
        print('Computer total:', computer_total)
        print('User total:', user_total)
        if user_total > computer_total:
            print('User wins')
        elif user_total < computer_total:
            print('Computer wins')
        else:
            print('It is a tie!')

    def computer_strategy(self, n):
        """
        create computer choices : roll everything again
        """
        print('Computer is thinking...')
        time.sleep(3)
        choices = ''  # start with empty choices
        for i in range(n):
            choices = choices + 'r'
            print('position:', i)
        return choices

    def computer_strategy_2(self, n):
        """
        create computer strategy chices if roll < 5
        """
        print('Computer is thinking')
        time.sleep(3)
        choices = ''  # start with empty choices
        for i in range(n):
            computer_rolls = []
            if computer_rolls[i] < 5:
                choices = choices + 'r'
            else:
                choices = choices + '-'
        return choices