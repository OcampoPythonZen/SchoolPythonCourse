'''
Author: Edd
Date: 12/01/2021
Description: This is my candy eting frog game
'''

# library importations
# comodin = "todo" = *
import random
from tkinter import Text, Tk
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
title = canvas.create_text(
    200, 200, text='The Frog Monster', fill='white', font=('Helvetica', 25))
directions = canvas.create_text(
    200, 300, text='Collect the candys but avoid the red ones', fill='white', font=('Helvetica', 15))

# setting up the score to diplay into Canvas
# int -> convierte un str a un valor entero
# str -> convierte un valor entero en str
score = 0  # int
score_display = Label(window, text='Score:' + str(score))
score_display.pack()

# Setting up the level display
level = 1  # int
#level_2 = ['basic', 'medium', 'advance']
level_display = Label(window, text='Level:' + str(level))
level_display.pack()

# create an image using the .gif file
player_image = PhotoImage(file="greenChar.gif")
# use image to create a frog at position 200, 360
mychar = canvas.create_image(200, 360, image=player_image)

# variables and lists needed for managing candy
candy_list = []  # list containing all candy created, empty at start
bad_candy_list = []  # list containing all bad candy created, empty at start
candy_speed = 2  # initial speed of falling candy.
candy_color_list = ['red', 'yellow', 'blue',
                    'green', 'purple', 'pink', 'white', 'cyan']

# Define my own functions


def make_candy():
    """
    function to create the randoms candys on Screen
    """
    # pick a random x position
    xposition = random.randint(1, 400)
    # pick a random color
    candy_color = random.choice(candy_color_list)
    # create a candy of size 30  --- at random position and color
    candy = canvas.create_oval(
        xposition, 0, xposition + 30, 30, fill=candy_color)
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
    # loop through list of candy and change y position
    for candy in candy_list:
        canvas.move(candy, 0, candy_speed)
        if canvas.coords(candy)[1] > 400:
            xposition = random.randint(1, 400)
            canvas.coords(candy, xposition, 0, xposition + 30, 30)
    # schedule this function to move candy again
    window.after(50, move_candy)


def update_score_level():
    # function updates score, level and candy_speed too.
    global score, level, candy_speed
    score = score + 1
    score_display.config(text="Score:" + str(score))
    if score > 5 and score <= 10:
        candy_speed = candy_speed + 1
        level = 2
        level_display.config(text="Level:" + str(level))
    elif score > 10:
        candy_speed = candy_speed + 1
        level = 3
        level_display.config(text="Level:" + str(level))


def end_game_over():
    #Console - print()
    # Print Canvas Label
    window.destroy()


def end_title():
    canvas.delete(title)
    canvas.delete(directions)

# check distance between 2 objects - return true if they 'touch'


def collision(item1, item2, distance):
    # xdistance = -98 = abs(xdistance) = |xdistance| = 98
    xdistance = abs(canvas.coords(item1)[0] - canvas.coords(item2)[0])
    ydistance = abs(canvas.coords(item1)[1] - canvas.coords(item2)[1])
    overlap = xdistance < distance and ydistance < distance
    return overlap


def check_hits():
    # check if it hit a bad candy - need to end game.
    for bad_candy in bad_candy_list:
        if collision(mychar, bad_candy, 30):
            game_over = canvas.create_text(200, 200, text='Game Over', fill='red', font=('Helvetica', 30))
            window.after(2000, end_game_over)
            return
    # check if hit any good candy        
    for candy in candy_list:
        if collision(mychar, candy, 30):
            canvas.delete(candy)
            candy_list.remove(candy)
            update_score_level()
    window.after(100, check_hits)

move_direction = 0  # track which direction player is moving


def check_input(event):
    global move_direction
    key = event.keysym
    if key == 'Right':
        move_direction = 'Right'
    elif key == 'Left':
        move_direction = 'Left'

# Function handles when user stop pressing arrows keys


def end_input(event):
    global move_direction
    move_direction = 'None'

# Function checks if not on edge and updates x coordinates based on right/left
def move_character():
    if move_direction == 'Right' and canvas.coords(mychar)[0] < 400:
        canvas.move(mychar, 10, 0)
    if move_direction == "Left" and canvas.coords(mychar)[0] > 0:
        canvas.move(mychar, -10, 0)
    window.after(16, move_character)  # Move character at 60 frames per second


# bind the keys to the character
canvas.bind_all('<KeyPress>', check_input)
canvas.bind_all('<KeyRelease>', end_input)

# Start game loop by scheduling all the functions
window.after(1000, end_title)
window.after(1000, make_candy)
window.after(1000, move_candy)
window.after(1000, check_hits)
window.after(1000, move_character)

window.mainloop()  # last line is the GUI main event loop
