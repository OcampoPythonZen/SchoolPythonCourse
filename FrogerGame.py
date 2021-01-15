'''
Author: Edd
Date: 12/01/2021
Description: This is my candy eting frog game
'''

# library importations
# comodin = todo = *
import random
from tkinter import Tk
from tkinter import Canvas
from tkinter import Label
from tkinter import PhotoImage
# function dir show the classes and functions library
# print(dir(random))

# make Window
window = Tk()
window.title('Froger Game. - Eating Candys')

# create a space ti put the objects on the screen
canvas = Canvas(window, width=400, height=400, bg='black')
canvas.pack()

# set up welcome screen with title and directions
title = canvas.create_text(200, 200, text='The Frog Monster', fill='white', font=('Helvetica', 25))
directions = canvas.create_text(200, 300, text='Collect the candys but avoid the red ones', fill='white', font=('Helvetica', 15))

# setting up the score to diplay into Canvas
# int -> convierte un str a un valor entero
# str -> convierte un valor entero en str
score = 0 # int
score_diplay = Label(window, text = 'Score:' + str(score))


# Setting up the level display 
level = 1 # int
#level_2 = ['basic', 'medium', 'advance']
level_diplay = Label(window, text = 'Level:' + str(level))

# create an image using the .gif file
player_image = PhotoImage(file="greenChar.gif")
# use image to create a frog at position 200, 360
mychar = canvas.create_image(200, 360, image = player_image)

# variables and lists needed for managing candy
candy_list = [] # list containing all candy created, empty at start
bad_candy_list = [] # list containing all bad candy created, empty at start
candy_speed = 2 # initial speed of falling candy.
candy_color_list = ['red', 'yellow', 'blue', 'green', 'purple', 'pink', 'white', 'cyan']

# Define my own functions

def make_candy():
    """
    function to create the randoms candys on Screen
    """
    # pick a random x position
    xposition = random.randint(1,400)
    # pick a random color
    candy_color = random.choice(candy_color_list)
    # create a candy of size 30  --- at random position and color
    candy = canvas.create_oval(xposition, 0, xposition + 30, 30, fill = candy_color)
     # add candy to list -> candy_list
    candy_list.append(candy)
    # if color of candy is red - add it to bad_candy_list -> 'red'
    if candy_color == candy_color_list[0]:
        bad_candy_list.append(candy)
    # schedule this function to make candy again
    window.after(1000, make_candy)


def move_candy():
    '''
    # function moves candy downwards, and schedules call to move_candy
    '''
    pass