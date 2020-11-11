# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 13:55:16 2020
@author: Edgar Ocampo
@program: ChatBot
"""
import math
import datetime
import time


def chatbot_intro():
    # Chatbot introduction
    print("Hello. I am Chappie, I am a ChatBot")
    print('I love the pi number: ', math.pi)
    print('I like animals and I love talk to you')
    name = input('What is your name:? ')
    print('Hello', name, 'Nice to meet you.')


def chatbot_food_info():
    # Chatbot food information
    food = input('What is your favorite food:? ')
    print('Wow.', 'I love', food, 'too')
    print('Were gonna talk about time...')


def chatbot_about_time():
    # About time
    time.sleep(2)
    print('Do you know the date?')
    time.sleep(2)
    date = datetime.datetime.now().year
    print(f'I can tell you the puntual year: {date}')


def chatbot_about_robot_age():
    # About robot age
    the_age = int(input('What old are you?'))
    print('Wow, I like to got the same age', the_age, ' great...')
    one_hundred = 100 - the_age
    print('You know, i will on 100 years on ', one_hundred, 'years')


if __name__ == "__main__":
    print('Hello this is the main program...')
